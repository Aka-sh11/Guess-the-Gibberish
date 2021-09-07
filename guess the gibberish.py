import random
import time
from tkinter import *
from PIL import Image, ImageTk

# data for game
from question import *
from answer import *


root = Tk()
root.geometry('380x500')
root.title('Guess the Gibberish')
root.config(bg='#ffff63')
root.resizable(False, False)
root.iconbitmap('game-console.ico')
# image for gibberish background
image1 = Image.open('Gibberish_back.png')
test = ImageTk.PhotoImage(image1)
Label(image=test, bg='#ffff63').place(x=0, y=70)

timer = 15
score = 0


# start game function
def StartGame():
    start_button.config(state=DISABLED, bg='grey')
    next_btn.config(state=DISABLED)
    show_ans_l.config(text='')
    RW.config(text='')
    global random_num, timer
    timer = 15
    random_num = random.randint(1, 61)
    Question_label.config(text=Question[random_num])
    hint_label.config(text='Hint -> Number of words is : '+str(len(answer[random_num].split())))
    startcountdown()
    Ans_entry.bind('<Return>', Checkans)


def startcountdown():
    global timer
    if timer >= 0:
        time_label.config(text=str(timer))
        timer -= 1
        time_label.after(1000, startcountdown)
        if timer == -1:
            next_btn.config(state=NORMAL)
            show_ans_l.config(text='Right answer is : ' + answer[random_num].lower())
            Ans_entry.delete(0, END)


def Checkans(event):
    global score
    user = str(Ans_entry.get())
    if user.lower() == answer[random_num].lower():
        score += 1
        score_label.config(text='Your Score : ' + str(score))
        Ans_entry.delete(0, END)
        RW.config(text='RIGHT', fg='green')

    else:
        Ans_entry.delete(0, END)
        RW.config(text='WRONG', fg='red')
        show_ans_l.config(text='Right answer is : ' + answer[random_num].lower())


def Reset():
    global timer, score
    timer = 15
    score = 0
    score_label.config(text='Your Score : ' + str(score))
    time_label.config(text='15')
    Question_label.config(text='Guess The Gibberish')
    start_button.config(state=NORMAL)
    next_btn.config(state=DISABLED)
    hint_label.config(text='Hint -> Number of words is : ')
    Ans_entry.delete(0, END)


game_desp = 'Game Description: Guess The Gibberish Game is a free word \n puzzle game that will exercise your brain.' \
            'it has words that \n are  made up but when spoken/write sound similar to a real word. \n \n After Click ' \
            'start button, Enter the answer in the displyed below \n and press enter.  ' \
            'for next round click on Next button '
Label(root, text=game_desp, fg='grey', bg='#ffff63', font='Helvetica 8').place(x=15, y=0)

Label(root, text='Designed by AKASH', fg='white', bg='#0597fe', font='Helvetica 12 bold').place(x=130, y=100)
Question_label = Label(root, text='Guess The Gibberish', fg='white', bg='#0597fe', font='Helvetica 15 bold')
Question_label.place(x=50, y=140)

time_label = Label(root, text='15', font='Helvetica 18 bold', fg='white', bg='black')
time_label.place(x=178, y=216)

score_label = Label(root, text='Your Score : '+str(score), font='Helvetica 12 bold', fg='black', bg='#ffff63')
score_label.place(x=130, y=280)

Ans_entry = Entry(root, width=25, font='Helvetica 12 bold')
Ans_entry.place(x=35, y=320)

hint_label = Label(root, text='Hint -> Number of words is : ', fg='black', bg='#ffff63')
hint_label.place(x=35, y=350)

next_btn = Button(root, text='Next', width=7, height=1, bd=0, bg='grey', command=StartGame)
next_btn.place(x=270, y=320)

RW = Label(root, text='', fg='white', bg='#ffff63', font='Helvetica 13 bold')
RW.place(x=150, y=370)

show_ans_l = Label(root, text=' ', font='Helvetica 12 bold', fg='black', bg='#ffff63')
show_ans_l.place(x=40, y=410)

btn_frame = Frame(root, width=40, height=40)
btn_frame.pack(side=BOTTOM)
start_button = Button(btn_frame, text='Start', width=20, bd=0, padx=10, pady=10, bg='#a3ffc8', command=StartGame)
start_button.grid(row=0, column=0)
Button(btn_frame, text='Reset', width=20, bd=0, padx=10, pady=10, bg='light blue', command=Reset).grid(row=0, column=1)

root.mainloop()
