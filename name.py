from tkinter import *
from tkinter import messagebox
from main import CARD

root = Tk()
root.title("CARD")

# FUNCTIONS
def Exit():
    root.destroy()

def Create_Card():
    occ = Occation.get()
    nam = Name.get()

    if occ == "" or nam == "":
        messagebox.showinfo("ERROR", "ALL FIELDS ARE REQUIRED")

    elif occ != "" and nam != "":
        root.destroy()
        Card_root = Tk()
        CARD(Card_root, occ, nam)

# OCCATION
Occation_Label = Label(root, text = "OCCATION: ", fg = "black", font = (60))
Occation_Label.grid(row = 0)

Occation = Entry(root, font = (60))
Occation.grid(row = 0, column = 1)

# NAME
Name_Label = Label(root, text = "NAME: ", fg = "black", font = (60))
Name_Label.grid(row = 1)

Name = Entry(root, font = (60))
Name.grid(row = 1, column = 1)

# EXIT
Exit_Button = Button(root, text = "EXIT", width = 6, height = 1, command = lambda:Exit(), font = (30))
Exit_Button.grid(row = 2, column = 0)

# CREATE
Create_Button = Button(root, text = "CREATE", width = 6, height = 1, command = lambda:Create_Card(), font = (30))
Create_Button.grid(row = 2, column = 1)

# MAINLOOP
root.mainloop()