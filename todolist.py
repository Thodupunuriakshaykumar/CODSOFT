from tkinter import *
from tkinter import messagebox

def newTask():
    task=my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0,"end")
    else:
        messagebox.showwarning("warning","please enter some task")

def deleteTask():
    lb.delete(ANCHOR)
ws=Tk()
ws.geometry('700x450+400+200')
ws.title('TO DO LIST')
ws.config(bg='#7ed4e6')
ws.resizable(width=False,height=False)

frame=Frame(ws)
frame.pack(pady=10)

lb=Listbox(
    frame,
    width=40,
    height=8,
    font=('time',18),
    bd=0,
    fg='#000000',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",

 )
lb.pack(side=LEFT,fill=BOTH)

task_list=[
    'prepare for exames',
    'nptel',
    'python revision',
    'cyber classes',
    'take a nap',
    'learn something',
]

for item in task_list:
    lb.insert(END,item)

sb=Scrollbar(frame)
sb.pack(side=RIGHT,fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry=Entry(
    ws,
    font=('good times',24)
    )

my_entry.pack(pady=20)

button_frame=Frame(ws)
button_frame.pack(pady=20)

addTask_btn=Button(
    button_frame,
    text='ADD TASK',
    font=('times 14'),
    bg='#FF6347',
    padx=20,
    pady=10,
    command=newTask

)
addTask_btn.pack(fill=BOTH,expand=True,side=LEFT)

delTask_btn=Button(
    button_frame,
    text='DELETE TASK',
    font=('times 14'),
    bg='#FF8C00',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH,expand=True,side=LEFT)

ws.mainloop()
