from tkinter import *

root = Tk()
Label(text="Выберете цвет").pack()
e1 = Entry(width=30)
color_list = [['c1', "#ff0000"], ['c2', "#ff7d00"], ['c3', "#ffff00"], ["c4", "#00ff00"], ["c5", "#007dff"],
              ["c6", "#0000ff"], ["c7", "#7d00ff"]]
color = dict(color_list)
print(color)
print(color['c1'], color["c5"])


def c1_f():
    e1.insert(0, color['c1'].center(50))


def c2_f():
    e1.insert(0, color['c2'].center(50))


def c3_f():
    e1.insert(0, color['c3'].center(50))


def c4_f():
    e1.insert(0, color['c4'].center(50))


def c5_f():
    e1.insert(0, color['c5'].center(50))


def c6_f():
    e1.insert(0, color['c6'].center(50))


def c7_f():
    e1.insert(0, color['c7'].center(50))


e1.pack()
Button(bg="#ff0000", width=20, command=c1_f).pack()
Button(bg=color["c2"], width=20, command=c2_f).pack()
Button(bg=color["c3"], width=20, command=c3_f).pack()
Button(bg=color["c4"], width=20, command=c4_f).pack()
Button(bg=color["c5"], width=20, command=c5_f).pack()
Button(bg=color["c6"], width=20, command=c6_f).pack()
Button(bg=color["c7"], width=20, command=c7_f).pack()
b1 = Button(text='Exit', command=root.quit)
b1.pack()
root.mainloop()
