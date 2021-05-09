from tkinter import *
from tkinter import messagebox

class CARD:
    def __init__(self, root, occation, nam):
        self.root = root
        self.root.title("CARD")
        self.root.geometry("1500x900+0+0")
        self.root.config(bg = "sky blue")
        
        occ = occation.upper()
        name = nam.upper()

        # FUNCTIONS
        def Exit(): 
            self.root.destroy()

        # CARD
        self.pic_1 = PhotoImage(file = "/home/niksh/Downloads/party.png")
        pic1 = Label(self.root, image = self.pic_1)
        pic1.place(x = 150, y = 630)

        self.pic_2 = PhotoImage(file = "/home/niksh/Downloads/popper.png")
        pic2 = Label(self.root, image = self.pic_2)
        pic2.place(x = 500, y = 630)

        self.pic_3 = PhotoImage(file = "/home/niksh/Downloads/decor.png")
        pic3 = Label(self.root, image = self.pic_3)
        pic3.place(x = 50, y = 260)

        self.pic_4 = PhotoImage(file = "/home/niksh/Downloads/quote.png")
        pic4 = Label(self.root, image = self.pic_4)
        pic4.place(x = 1000, y = 270)

        occation_title = Label(self.root, text = occ, font = ("times new roman", 70, "bold"), bg = "yellow", fg = "black", bd = 10, relief = GROOVE)
        occation_title.place(x = 0, y = 0, relwidth = 1)

        name_title = Label(self.root, text = name, font = ("times new roman", 70, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        name_title.place(x = 0, y = 125, relwidth = 1)

        by_label = Label(self.root, text = "- NIKSH", font = ("times new roman", 50, "bold"), bg = "yellow", fg = "black")
        by_label.place(x = 1200, y = 150)

        # BUTTONS
        Exit_Button = Button(root, text = "CLOSE", width = 6, height = 1, command = lambda:Exit(), font = (30))
        Exit_Button.place(x = 30, y = 850)

        # MAINLOOP
        self.root.mainloop()