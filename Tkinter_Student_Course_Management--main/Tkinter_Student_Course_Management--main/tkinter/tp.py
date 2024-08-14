# TKinter and database


from tkinter import *
from functools import partial
import tkinter.font as font

import mysql.connector as m

mydatabase = m.connect(host="localhost", user="root", password="Sahil@123", database="pythondb1")
query = "insert into person(name,address,age) values(%s,%s,%s)"  # must be "s"


def savePerson():
    myFont = font.Font(family='Helvetica', size=20)
    name_1 = nameEntry.get()
    address_1 = addressEntry.get()
    age_1 = ageEntry.get()
    # print(name_1,address_1,age_1)
    cursor = mydatabase.cursor()
    cursor.execute(query, [name_1, address_1, age_1])  # second argument has to be list or tuple or dictionary
    mydatabase.commit()


# window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Tkinter Login Form - pythonexamples.org')

# name label and text entry box
nameLabel = Label(tkWindow, text="Name")
nameLabel.grid(row=0, column=0)
nameEntry = Entry(tkWindow)
nameEntry.grid(row=0, column=1)

# Address label and password entry box
addressLabel = Label(tkWindow, text="Address")
addressLabel.grid(row=1, column=0)

addressEntry = Entry(tkWindow)
addressEntry.grid(row=1, column=1)

# Age label and password entry box
ageLabel = Label(tkWindow, text="Age")
ageLabel.grid(row=2, column=0)

ageEntry = Entry(tkWindow)
ageEntry.grid(row=2, column=1)

# login button
saveButton = Button(tkWindow, text="Save", command=savePerson)
saveButton.grid(row=4, column=0)

tkWindow.mainloop()


student_id,student_name,course_name,instructor_name,language,price,tree

None, None, None, None, None, None, tree

