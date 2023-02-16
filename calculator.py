from tkinter import Tk, Entry, Button, StringVar
from tkinter import Label


class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("577x600+100+200")
        master.config(bg='#17161b')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        self.result_label = Label(
            master, textvariable=self.equation, width=25, height=2, font=('Arial Bold', 30)).pack()

        # row 1
        Button(width=5, height=1, text='C', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=self.clear).place(x=10, y=100)
        Button(width=5, height=1, text='(', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=lambda: self.show('(')).place(x=150, y=100)
        Button(width=5, height=1, text=')', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=lambda: self.show(')')).place(x=290, y=100)
        Button(width=5, height=1, text='/', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=lambda: self.show('/')).place(x=430, y=100)

        # row 2
        Button(width=5, height=1, text='7', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=lambda: self.show(7)).place(x=10, y=200)
        Button(width=5, height=1, text='8', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=lambda: self.show(8)).place(x=150, y=200)
        Button(width=5, height=1, text='9', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=lambda: self.show(9)).place(x=290, y=200)
        Button(width=5, height=1, text='x', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=lambda: self.show('*')).place(x=430, y=200)
        # row 3
        Button(width=5, height=1, text='4', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=lambda: self.show(4)).place(x=10, y=300)
        Button(width=5, height=1, text='5', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=lambda: self.show(5)).place(x=150, y=300)
        Button(width=5, height=1, text='6', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=lambda: self.show(6)).place(x=290, y=300)
        Button(width=5, height=1, text='-', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=lambda: self.show('-')).place(x=430, y=300)

        # row 4
        Button(width=5, height=1, text='1', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=lambda: self.show(1)).place(x=10, y=400)
        Button(width=5, height=1, text='2', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=lambda: self.show(2)).place(x=150, y=400)
        Button(width=5, height=1, text='3', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=lambda: self.show(3)).place(x=290, y=400)
        Button(width=5, height=1, text='+', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=lambda: self.show('+')).place(x=430, y=400)

        # row 5
        Button(width=5, height=1, text='.', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=lambda: self.show('.')).place(x=10, y=500)
        Button(width=5, height=1, text='0', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=lambda: self.show(0)).place(x=150, y=500)
        Button(width=5, height=1, text='%', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=lambda: self.show('%')).place(x=290, y=500)
        Button(width=5, height=1, text='=', relief='flat', bg='#3697f5', font=("arial", 30, "bold"), bd=1, fg="#fff",
               command=self.solve).place(x=430, y=500)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result = ''
        if self.entry_value != '':
            try:
                result = eval(self.entry_value)
                self.equation.set(result)
            except:
                result = "error"


root = Tk()
Calculator = Calculator(root)
root.mainloop()
