import tkinter
from tkinter import *
from functools import partial

win=Tk()
def sum(label,x1,x2):
    n1=x1.get()
    n2=x2.get()
    sum=int(n1)+int(n2)
    label.config(text='sum is : %d' %sum)
    return

def sub(label,x1,x2):
    n1=x1.get()
    n2=x2.get()
    sub=int(n1)-int(n2)
    label.config(text='difference is : %d' %sub)
    return

def pro(label,x1,x2):
    n1=x1.get()
    n2=x2.get()
    pro=int(n1)*int(n2)
    label.config(text='product is : %d' %pro)
    return

def div(label,x1,x2):
    n1=x1.get()
    n2=x2.get()
    div=float(n1)/float(n2)
    label.config(text='division is : %f' %div)
    return


l1=Label(win,text=" num 1")
l1.grid(row=1,column=0)
l2=Label(win,text=" num 2")
l2.grid(row=2,column=0)
label=Label(win)
label.grid(row=6,column=1)

x1=StringVar()
x2=StringVar()

e1=Entry(win,textvariable=x1)
e1.grid(row=1,column=2)
e2=Entry(win,textvariable=x2)
e2.grid(row=2,column=2)

sum=partial(sum,label,x1,x2)
sub=partial(sub,label,x1,x2)
pro=partial(pro,label,x1,x2)
div=partial(div,label,x1,x2)

b1=Button(win,text="sum" ,command=sum)
b1.grid(row=3,column=0)
b2=Button(win,text="sub" ,command=sub)
b2.grid(row=3,column=2)
b3=Button(win,text="pro" ,command=pro)
b3.grid(row=4,column=0)
b4=Button(win,text="div" ,command=div)
b4.grid(row=4,column=2)


win.mainloop()
