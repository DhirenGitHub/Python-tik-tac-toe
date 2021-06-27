from tkinter import *

window = Tk()
window.title("GUI")
turn = "X"


def click(button, r, c):
    global turn

    try:
        print(r, c, button)
        b = Button(window, text=turn, border=10, command=lambda: click(1, r, c), width=10, height=5)
        b.grid(row=r, column=c)
    except:
        print("Error")

    if turn == "X":
        turn = "0"
    else:
        turn = "X"


b1 = Button(window, text="", border=10, command=lambda: click(1, 0, 0), width=10, height=5)
b1.grid(row=0, column=0)

b2 = Button(window, text="", border=10, command=lambda: click(2, 1, 0), width=10, height=5)
b2.grid(row=1, column=0)

b3 = Button(window, text="", border=10, command=lambda: click(3, 2, 0), width=10, height=5)
b3.grid(row=2, column=0)

b4 = Button(window, text="", border=10, command=lambda: click(4, 0, 1), width=10, height=5)
b4.grid(row=0, column=1)

b5 = Button(window, text="", border=10, command=lambda: click(5, 1, 1), width=10, height=5)
b5.grid(row=1, column=1)

b6 = Button(window, text="", border=10, command=lambda: click(6, 2, 1), width=10, height=5)
b6.grid(row=2, column=1)

b7 = Button(window, text="", border=10, command=lambda: click(7, 0, 2), width=10, height=5)
b7.grid(row=0, column=2)

b8 = Button(window, text="", border=10, command=lambda: click(8, 1, 2), width=10, height=5)
b8.grid(row=1, column=2)

b9 = Button(window, text="", border=10, command=lambda: click(9, 2, 2), width=10, height=5)
b9.grid(row=2, column=2)

window.mainloop()
