from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")

def time():
    string = strftime('%H:%m:%S %p')
    label.config(text=string)
    label.after(1000, time)
    
label = Label(root, font=("Digital-7", 80), background = "black", foreground = "cyan")
label.pack(anchor='center')
time()

mainloop()
