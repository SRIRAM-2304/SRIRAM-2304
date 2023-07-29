import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import sqlite3

class DataBaseConnect:
    def __init__(self):
        self._db = sqlite3.connect('information.db')
        self._db.row_factory=sqlite3.Row
        self._db.execute('create table if not exists Compliant(ID integer primary key autoincrement, Name varchar(255), Gender varchar(255), Comment text)')
        self._db.commit()
    def Add(self, name, gender, comment):
        self._db.execute('insert into Compliant (Name, Gender, Comment) values (?,?,?)',(name,gender,comment))
        self._db.commit()
        return 'Your complaint has been submitted.'
    def ListRequest(self):
        cursor = self._db.execute('select * from Compliant')
        return cursor

class ListOfComp:
    def __init__(self):
        self._dbconnect = DataBaseConnect()
        self._dbconnect.row_factory = sqlite3.Row
        self._root = Tk()
        self._root.title('List of Complaints')
        tv = Treeview(self._root)
        tv.pack()
        tv.heading('#0', text='ID')
        tv.configure(column=('#Name', '#Gender', '#Comment'))
        tv.heading('#Name', text='Name')
        tv.heading('#Gender', text='Gender')
        tv.heading('#Comment', text='Comment')
        cursor = self._dbconnect.ListRequest()
        for row in cursor:
            tv.insert('', 'end', '#{}'.format(row['ID']),text=row['ID'])
            tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
            tv.set('#{}'.format(row['ID']),'#Gender',row['Gender'])
            tv.set('#{}'.format(row['ID']),'#Comment',row['Comment'])
#Config
connect = DataBaseConnect()
root = tk.Tk()
root.geometry('600x285')
root.title('Complaint Management')
root.configure(background='#06283D')
#style
style = Style()
style.theme_use('clam')
for elem in ['TLabel', 'TButton', 'TRadioutton']:
    style.configure(elem, background='#fff')
#lables
labels = ['Full Name:', 'Gender:', 'Comment:']
for i in range(3):
    tk.Label(root, text=labels[i],fg="#000000",font="Times 15 bold").grid(row=i, column=0, padx=10, pady=10)
BuList = Button(root, text='List Complaints.')
BuList.grid(row=4, column=1)
BuSubmit = Button(root, text='Submit Now')
BuSubmit.grid(row=4, column=2)

#Entries
fullname = Entry(root, width=40, font=('Times', 14))
fullname.grid(row=0, column=1, columnspan=2)
SpanGender = StringVar()
Radiobutton(root, text='Male', value='male', variable=SpanGender).grid(row=1, column=1)
Radiobutton(root, text='Female', value='female', variable=SpanGender).grid(row=1, column=2)
Radiobutton(root, text='Trans-Gender', value='transgender', variable=SpanGender).grid(row=1, column=3)
comment = Text(root, width=35, height=5, font=('Times', 14))
comment.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
#save enter data
def SaveData():
	msg = connect.Add(fullname.get(), SpanGender.get(), comment.get(1.0, 'end'))
	fullname.delete(0, 'end')
	comment.delete(1.0, 'end')
	showinfo(title='Add Info', message=msg)

def ShowList():
	listrequest = ListOfComp()

BuSubmit.config(command=SaveData)
BuList.config(command=ShowList)
root.mainloop()
