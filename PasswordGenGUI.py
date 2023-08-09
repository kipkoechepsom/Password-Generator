#--------------------------------------------#
#-------@author--Kelvin--Chepsom-------------#
#-------@portfolio---kipkoechepsom.rf.gd-----#
#--------------------------------------------#
#--------------------------------------------#
from tkinter import *
import sys
import os
import tkinter as tk
from tkinter.messagebox import showinfo


root = Tk()
root.title("Password Generator")
root.configure(bg="#D6AF22")
root.minsize(400,300)
root.maxsize(500,400)

def generate(x):
    import random
    
    upper    = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower    = "abcdefghijklmnopqrstuvwxyz"
    numbers  = "0123456789"
    symbols = "#$%@+|\[]{}()*:;/,._-"
    all = lower + upper + numbers + symbols
    length = x
    password = "".join(random.sample(all,length))
    
    display.delete(0, END)
    display.insert(10, password)
   

    return 

    

def displayScreen():
    
    return

def sixteen():
    length = 16
    generate(length)
    return

def fifteen():
    length = 15
    generate(length)
    return

def twelve():
    length = 12
    generate(length)
    return

def ten():
    length = 10
    generate(length)
    return

def nine():
    length = 9
    generate(length)
    return

def eight():
    length = 8
    generate(length)
    return

def seven():
    length = 7
    generate(length)
    return

def six():
    length = 6
    generate(length)
    return

#frame 000
topframe0 = Frame(root,bd=20)
topframe0.pack(side=TOP)
topframe0.configure(bg="#D6AF22")

label = Label(topframe0,text="Password Generator",foreground="black",font=("Segoe UI",20),bg="#D6AF22")
label.pack(side=LEFT)

topframelen = Frame(root,bd=20)
topframelen.pack(side=TOP)
topframelen.configure(bg="#D6AF22")

label = Label(topframelen,text="Click to Choose Password Length",foreground="black",font="Courier",bg="#D6AF22")
label.pack(side=LEFT)

#frame four
topframe3 = Frame(root,bd=20)
topframe3.pack(side=TOP)
topframe3.configure(bg="#D6AF22")


but = Button(topframe3,text="06",command=six,bd=6,foreground="white",font="Courier",bg="#D6AF22")
but.pack(side=LEFT)

but = Button(topframe3,text="07",command=seven,bd=6,foreground="white",font="Courier",bg="#D6AF22")
but.pack(side=LEFT)

but = Button(topframe3,text="08",command=eight,bd=6,foreground="white",font="Courier",bg="#D6AF22")
but.pack(side=LEFT)

but = Button(topframe3,text="09",command=nine,bd=6,foreground="white",font="Courier",bg="#D6AF22")
but.pack(side=LEFT)

but = Button(topframe3,text="10",command=ten,bd=6,foreground="white",font="Courier",bg="#D6AF22")
but.pack(side=LEFT)

but = Button(topframe3,text="12",command=twelve,bd=6,foreground="white",font="Courier",bg="#D6AF22")
but.pack(side=LEFT)

but = Button(topframe3,text="15",command=fifteen,bd=6,foreground="white",font="Courier",bg="#D6AF22")
but.pack(side=LEFT)

but = Button(topframe3,text="16",command=sixteen,bd=6,foreground="white",font="Courier",bg="#D6AF22")
but.pack(side=LEFT)



#frame five
topframe4 = Frame(root,bd=20)
topframe4.pack(side=TOP)
topframe4.configure(bg="#D6AF22")

label = Label(topframe4,text="Generated ",foreground="black",font="Courier",bg="#D6AF22")
label.pack(side=LEFT)

display = Entry(topframe4,justify = CENTER,font = ('courier', 14))
display.pack(side=LEFT)



topframe45 = Frame(root,bd=20)
topframe45.pack(side=TOP)
topframe45.configure(bg="#D6AF22")

label = Label(topframe45,text="@kipkoechepsom 2023",foreground="#FFD4FF",font="Courier",bg="#D6AF22")
label.pack(side=LEFT)
root.mainloop()
