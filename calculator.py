from tkinter import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.bar = Entry(root, borderwidth=5, width=20, font=('Arial', 16))
        self.bar.grid(row=0, column=0, columnspan=4)
        self.first_num = None
        self.operation = None
        self.create_buttons()

    def create_buttons(self):
        buttons = [Button(self.root, text=str(i), padx=30, pady=20, font=('Arial', 16), command=lambda num=i: self.on_click(num)) for i in range(10)]
        
        button_add = Button(self.root, text="+", padx=30, pady=20, font=('Arial', 16), command=self.add)
        button_subtract = Button(self.root, text="-", padx=32, pady=20, font=('Arial', 16), command=self.subtract)
        button_multiply = Button(self.root, text="x", padx=31, pady=20, font=('Arial', 16), command=self.multiply)
        button_divide = Button(self.root, text="/", padx=33, pady=20, font=('Arial', 16), command=self.divide)

        button_equal = Button(self.root, text="=", padx=74, pady=20, highlightthickness=2, font=('Arial', 16), command=self.equal)
        button_clear = Button(self.root, text="Clear", padx=56, pady=20, font=('Arial', 16), command=self.clear)

        # Place buttons
        buttons[7].grid(row=1, column=0)
        buttons[8].grid(row=1, column=1)
        buttons[9].grid(row=1, column=2)
        button_add.grid(row=1, column=3)

        buttons[4].grid(row=2, column=0)
        buttons[5].grid(row=2, column=1)
        buttons[6].grid(row=2, column=2)
        button_subtract.grid(row=2, column=3)
        
        buttons[1].grid(row=3, column=0)
        buttons[2].grid(row=3, column=1)
        buttons[3].grid(row=3, column=2)
        button_multiply.grid(row=3, column=3)

        buttons[0].grid(row=4, column=0)
        button_clear.grid(row=4, column=1, columnspan=2)
        button_divide.grid(row=4, column=3)

        button_equal.grid(row=5, column=0, columnspan=4)

    def on_click(self, num):
        self.bar.insert(END, num)

    def add(self):
        self.first_num = float(self.bar.get())
        self.bar.delete(0, END)
        self.operation = 'add'

    def subtract(self):
        self.first_num = float(self.bar.get())
        self.bar.delete(0, END)
        self.operation = 'subtract'

    def multiply(self):
        self.first_num = float(self.bar.get())
        self.bar.delete(0, END)
        self.operation = 'multiply'

    def divide(self):
        self.first_num = float(self.bar.get())
        self.bar.delete(0, END)
        self.operation = 'divide'

    def equal(self):
        second_num = float(self.bar.get())
        self.bar.delete(0, END)
        if self.operation == 'add':
            result = self.first_num + second_num
        elif self.operation == 'subtract':
            result = self.first_num - second_num
        elif self.operation == 'multiply':
            result = self.first_num * second_num
        elif self.operation == 'divide':
            if second_num != 0:
                result = self.first_num / second_num
            else:
                self.bar.insert(0, 'Error')
                return
        self.bar.insert(0, f'{result:g}')

    def clear(self):
        self.bar.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    root.title("Calculator")
    calculator = Calculator(root)
    root.mainloop()