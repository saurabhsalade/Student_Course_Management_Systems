import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

# Function to connect to MySQL database
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sahil@123",
            database="udemy_courses"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error connecting to database: {err}")
        return None

# Function to add a course to the database
def add_course(course_id,course_name, instructor_name, price):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO courses (course_id,course_name, instructor_name, price) VALUES (%s,%s, %s, %s)"
        data = (course_id,course_name, instructor_name, price)
        try:
            cursor.execute(query, data)
            conn.commit()
            messagebox.showinfo("Success", "Course added successfully!")
        except mysql.connector.Error as err:
            conn.rollback()
            messagebox.showerror("Error", f"Error adding course: {err}")
        conn.close()

# Function to add a student to the database
def add_student(student_name, email, course_name, language):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO students (student_name, email, course_name, language) VALUES (%s, %s, %s, %s)"
        data = (student_name, email, course_name, language)
        try:
            cursor.execute(query, data)
            conn.commit()
            messagebox.showinfo("Success", "Student added successfully!")
        except mysql.connector.Error as err:
            conn.rollback()
            messagebox.showerror("Error", f"Error adding student: {err}")
        conn.close()


def view_info(tree):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        query = ("select s.student_id, s.student_name,s.course_name,c.instructor_name,s.language,c.price from courses c join "
                 "students s on c.course_name=s.course_name")
        cursor.execute(query)


        for row in cursor.fetchall():
            tree.insert("", "end", values=row)



# Function to create the GUI for adding a course
def create_course_gui():
    course_window = tk.Toplevel(root)
    course_window.title("Add Course")
    course_window.geometry('1366x768')

    tk.Label(course_window, text="Course id:",width=20, height=2).pack()
    course_id_entry = tk.Entry(course_window)
    course_id_entry.pack(pady=10)

    tk.Label(course_window, text="Course Name:",width=20, height=2).pack()
    course_name_entry = tk.Entry(course_window)
    course_name_entry.pack(pady=10)

    tk.Label(course_window, text="Instructor Name:",width=20, height=2).pack()
    instructor_name_entry = tk.Entry(course_window)
    instructor_name_entry.pack(pady=10)

    tk.Label(course_window, text="Price:",width=20, height=2).pack()
    price_entry = tk.Entry(course_window)
    price_entry.pack(pady=10)

    def add_course_to_db():
        course_id=course_id_entry.get()
        course_name = course_name_entry.get()
        instructor_name = instructor_name_entry.get()
        price = price_entry.get()
        add_course(course_id,course_name, instructor_name, price)
        course_window.destroy()

    tk.Button(course_window, text="Add Course", command=add_course_to_db,bg='lightblue',width=20, height=2).pack()
    def destroy():
        course_window.destroy()
    close_button = tk.Button(course_window, text="Close Window", command=destroy,width=20, height=2)
    close_button.pack(pady=10)

# Function to create the GUI for adding a student
def create_student_gui():
    student_window = tk.Toplevel(root)
    student_window.title("Add Student")
    student_window.geometry('1366x768')

    tk.Label(student_window, text="Student Name:",width=20, height=2).pack()
    student_name_entry = tk.Entry(student_window)
    student_name_entry.pack(pady=10)

    tk.Label(student_window, text="Email:",width=20, height=2).pack()
    email_entry = tk.Entry(student_window)
    email_entry.pack(pady=10)

    tk.Label(student_window, text="Course Name:",width=20, height=2).pack()

    def fetch_course_name():
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT course_name FROM courses")
            course_name = [row[0] for row in cursor.fetchall()]
            conn.close()
            return course_name
        else:
            return []

    # Populate course names dropdown from database
    course_name = fetch_course_name()

    if course_name:
        selected_course = tk.StringVar(student_window)
        selected_course.set(course_name[0])  # Set default value to the first course in the list

        course_name_option_menu = tk.OptionMenu(student_window, selected_course, *course_name)
        course_name_option_menu.pack(pady=10)
    else:
        tk.Label(student_window, text="No courses found").pack()

    tk.Label(student_window, text="Language:",width=20, height=2).pack()
    language_entry = tk.Entry(student_window)
    language_entry.pack(pady=10)

    def add_student_to_db():
        student_name = student_name_entry.get()
        email = email_entry.get()
        course_name = selected_course.get()
        language = language_entry.get()
        add_student(student_name, email, course_name, language)
        student_window.destroy()

    tk.Button(student_window, text="Add Student", command=add_student_to_db, bg='lightblue',width=20, height=2).pack()
    def destroy():
        student_window.destroy()
    close_button = tk.Button(student_window, text="Close Window", command=destroy,width=20, height=2)
    close_button.pack(pady=10)


def view_info_gui():
    view_window = tk.Toplevel(root)
    view_window.title("View Data")
    view_window.geometry('1366x768')
    global tree
    tree = ttk.Treeview(view_window)
    tree["columns"] = ("student_id", "student_name", "s.course_name","instructor_name","language","price")
    tree.heading("student_id", text="Student ID")
    tree.heading("student_name", text="student_name")
    tree.heading("s.course_name", text="course_name")
    tree.heading("instructor_name", text="instructor_name")
    tree.heading("language",text="language")
    tree.heading("price",text="price")
    tree.column("#0", width=0)
    tree.pack(pady=10)
    view_info(tree)



    def close_tree():
        tree.pack_forget()
        close_button.destroy()
    close_button = tk.Button(view_window, text="Close Table", command=close_tree,width=20, height=2)
    close_button.pack(pady=10)
    def destroy():
        view_window.destroy()
    close_button = tk.Button(view_window, text="Close Window", command=destroy,width=20, height=2)
    close_button.pack(pady=10)





# Main GUI
root = tk.Tk()
root.title("Course and Student Management")
root.geometry('1366x768')
root.configure(background="#add8e6")


tk.Button(root, text="Add Course", command=create_course_gui,background='#a881af',width=20, height=2).pack(side=tk.TOP, padx=0,pady=30)
tk.Button(root, text="Add Student", command=create_student_gui, background='#a881af',width=20, height=2).pack(side=tk.TOP, padx=50,pady=30)
tk.Button(root, text="View Info", command=view_info_gui, bg='#a881af',width=20, height=2).pack(side=tk.TOP, padx=100,pady=30)

root.mainloop()
