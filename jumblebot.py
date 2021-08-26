import tkinter
from tkinter import *
from tkinter import messagebox
import random
from random import shuffle

answers = ["America", "Pakistan", "Australia"]

question = []

for i in answers:
    words = list(i)
    shuffle(words)
    question.append(words)

num = random.randint(0, len(question)-1)

def initial():
    global question, num
    lb1.configure(text=question[num])

def answercheck():
    global question, num, answers
    userinput = e1.get()

    if userinput == answers[num]:
        messagebox.showinfo('Success', 'Correct Answer')
    else:
        messagebox.showinfo('Oops', 'Wrong Answer')
        e1.delete(0, END) 

def resetmode():
    global question, num, answers
    num = random.randint(0, len(question)-1)
    lb1.configure(text=question[num])
    e1.delete(0, END)

window = Tk()
window.geometry("300x300")
window.configure(background='#0D0D0D')
window.title("Jumblebot")
window.iconbitmap("icon.ico")

lb1 = Label(window, font='times 20', bg='#207398' , fg='#03203C')
lb1.pack(pady=30, ipady=10, ipadx=10)

answer = StringVar()
e1 = Entry(window, textvariable=answer)
e1.pack(ipady=5, ipadx=5)

button1 = Button(window, text='check', bg='#242B2E', width=20, command=answercheck)
button1.pack(pady=40)

button2 = Button(window, text='Reset', bg='#A77B06', width=20, command=resetmode)
button2.pack()

initial()
window.mainloop()