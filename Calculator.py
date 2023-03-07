from tkinter import *
root = Tk()
root.geometry("500x500")
e1=Entry(root,width=20, font=("Arial",27))
e2=Entry(root,width=20, font=("Arial",27))
ce=Button(root,text="CE",font=("Arial",27),width=5)
add=Button(root,text="+",font=("Arial",27),width=5)
sub=Button(root,text="-",font=("Arial",27),width=5)
mul=Button(root,text="*",font=("Arial",27),width=5)
div=Button(root,text="/",font=("Arial",27),width=5)

def ce_f(event):
    e1.delete(0,END)
    e2.delete(0,END)
ce.bind("<Button-1>",ce_f)


def fadd(event):
    e3.delete(0,END)
    e3.insert(0,str(float(e1.get())+float(e2.get())))
    e1.delete(0,END)
    e2.delete(0,END)
add.bind("<Button-1>",fadd)


def sub_f(event):
    e3.insert(0,str(float(e1.get())-float(e2.get())))
sub.bind("<Button-1>",sub_f,ce_f)

def mul_f(event):
    e3.insert(0,str(float(e1.get())*float(e2.get())))
mul.bind("<Button-1>",mul_f,ce_f)

def div_f(event):
    e3.insert(0,str(float(e1.get())/float(e2.get())))
div.bind("<Button-1>",div_f)

e3=Entry(root,width=20, font=("Arial",27))
e1.pack()
e2.pack()
ce.pack()
add.pack()
sub.pack()
mul.pack()
div.pack()
e3.pack()

root.mainloop()