from tkinter import *
window = Tk()
window.title("Calculator")
window.geometry("208x316")

math_string = StringVar()
display_text = ""

def numbr(numerica):
    global display_text
    display_text = display_text + str(numerica)
    math_string.set(display_text)

def symbol_sum():
    global display_text
    sum_all = str(eval(display_text))
    math_string.set(sum_all)
    display_text = sum_all

def clear():
    global display_text
    math_string.set("")
    display_text = ""

def close():
    window.destroy()

calc_1 = Button(window, text="1", height=3, width=6, command=lambda: numbr(1))
calc_2 = Button(window, text="2", height=3, width=6, command=lambda: numbr(2))
calc_3 = Button(window, text="3", height=3, width=6, command=lambda: numbr(3))
calc_4 = Button(window, text="4", height=3, width=6, command=lambda: numbr(4))
calc_5 = Button(window, text="5", height=3, width=6, command=lambda: numbr(5))
calc_6 = Button(window, text="6", height=3, width=6, command=lambda: numbr(6))
calc_7 = Button(window, text="7", height=3, width=6, command=lambda: numbr(7))
calc_8 = Button(window, text="8", height=3, width=6, command=lambda: numbr(8))
calc_9 = Button(window, text="9", height=3, width=6, command=lambda: numbr(9))
calc_0 = Button(window, text="0", height=3, width=6, command=lambda: numbr(0))
sym_plus = Button(window, text="+", height=3, width=6, command=lambda: numbr("+"))
sym_minus = Button(window, text="-", height=3, width=6, command=lambda: numbr("-"))
sym_divide = Button(window, text="/", height=3, width=6, command=lambda: numbr("/"))
sym_multi = Button(window, text="*", height=3, width=6, command=lambda: numbr("*"))
dot = Button(window, text=".", height=3, width=6, command=lambda: numbr("."))
num_sum = Button(window, text="=", height=3, width=6, command=symbol_sum)
clear = Button(window, text="C", height=3, width=6, command=clear)



calc_1.grid(row=4 , column=0)
calc_2.grid(row=4 , column=1)
calc_3.grid(row=4 , column=2)
calc_4.grid(row=3 , column=0)
calc_5.grid(row=3 , column=1)
calc_6.grid(row=3 , column=2)
calc_7.grid(row=2 , column=0)
calc_8.grid(row=2 , column=1)
calc_9.grid(row=2 , column=2)
calc_0.grid(row=5 , column=1)
sym_plus.grid(row=4, column=3)
sym_minus.grid(row=3, column=3)
sym_divide.grid(row=1, column=3)
sym_multi.grid(row=2, column=3)
num_sum.grid(row=5, column=3)
clear.grid(row=5, column=0)
dot.grid(row=5, column=2)

window.bind("<Escape>", lambda event: close())
window.bind("<Return>", lambda event: symbol_sum())

all_sum = Label(window, textvariable=math_string, bg="cyan", height=2, width=20)
all_sum.grid(row=0, columnspan=10)

window.mainloop()