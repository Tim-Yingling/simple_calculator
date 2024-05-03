from tkinter import *

if __name__ == "__main__":
    root = Tk()

    def on_click(num):
        bar.insert(END, num)
    
    def add():
        first_num = bar.get()
        bar.delete(0, END)
        global f_num
        f_num = int(first_num)
    
    def equal():
        second_num = bar.get()
        bar.delete(0, END)
        bar.insert(0, f_num + int(second_num))

    
    def clear():
        bar.delete(0, END)

    # Input field
    bar = Entry(root, borderwidth=5, width=20, font=(16))
    bar.grid(row=0, column=0, columnspan=4)

    # Define buttons
    button_1 = Button(root, text="1", padx=40, pady=30, font=(16), command=lambda:on_click(1))
    button_2 = Button(root, text="2", padx=40, pady=30, font=(16), command=lambda:on_click(2))
    button_3 = Button(root, text="3", padx=40, pady=30, font=(16), command=lambda:on_click(3))
    button_4 = Button(root, text="4", padx=40, pady=30, font=(16), command=lambda:on_click(4))
    button_5 = Button(root, text="5", padx=40, pady=30, font=(16), command=lambda:on_click(5))
    button_6 = Button(root, text="6", padx=40, pady=30, font=(16), command=lambda:on_click(6))
    button_7 = Button(root, text="7", padx=40, pady=30, font=(16), command=lambda:on_click(7))
    button_8 = Button(root, text="8", padx=40, pady=30, font=(16), command=lambda:on_click(8))
    button_9 = Button(root, text="9", padx=40, pady=30, font=(16), command=lambda:on_click(9))
    button_0 = Button(root, text="0", padx=40, pady=30, font=(16), command=lambda:on_click(0))
    button_add = Button(root, text="+", padx=40, pady=30, font=(16), command=add)
    button_equal = Button(root, text="=", padx=90, pady=30, font=(16), command=equal)
    button_clear = Button(root, text="Clear", padx=76, pady=30, font=(16), command=clear)

    # Place buttons
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)
    button_add.grid(row=1, column=3)

    button_0.grid(row=4, column=0)
    button_clear.grid(row=4, column=1, columnspan=2)

    button_equal.grid(row=5, column=1, columnspan=2)

    # Display the interface
    root.mainloop()