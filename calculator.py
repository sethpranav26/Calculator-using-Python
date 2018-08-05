from tkinter import *

top=Tk()
top.geometry("300x350")
top.title("Calculator")


t1=Entry(top,text="")
t1.place(x=50,y=40,width=200,height=50)
flag=0

def op_add(first,second):
    if(first==""):
        first=0
    if(second==""):
        second=0
    t1.insert("end",int(first)+int(second))
def op_sub(first,second):
    if(first==""):
        first=0
    if(second==""):
        second=0
    t1.insert("end",int(first)-int(second))
def op_mul(first,second):
    if(first==""):
        first=1
    if(second==""):
        second=1
    t1.insert("end",int(first)*int(second))
def op_div(first,second):
    global flag
    if(first==""):
        first=0
    if(second==""):
        second=1
    if second=='0':
        t1.insert(0,"Cannot divide by zero")
        flag=1
    else:
        t1.insert("end",int(first)/int(second))
    
    
def abc(a):
    global first,op,second,flag
    if (first=="#"):
        if a== "=":
            if(flag==1):
                t1.delete(0,"end")
            second=t1.get()
            t1.delete(0,"end")
            if op=="#":
                t1.insert(0,0)
            if op=="+":
                op_add(first,second)
            elif op=="-":
                op_sub(first,second)
            elif op=="/":
                    op_div(first,second)
            elif op=="*":
                op_mul(first,second)
            
                
        elif (a=="+" or a=="*" or a=="-" or a=="/"):
            first=t1.get()
            t1.delete(0,"end")
            t1.insert("end",a)
            op=t1.get()
            flag=1
        elif a=="<-":
            b=len(t1.get())
            t1.delete(b-1,b)
        else:
            if flag==1:
                t1.delete(0,"end")
                flag=0
            t1.insert("end",a)
    else:
        if (a=="+" or a=="*" or a=="-" or a=="/"):
            second=t1.get()
            t1.delete(0,"end")
            if op=="+":
                first=int(first)+int(second)
            elif op=="-":
                first=int(first)-int(second)
            elif op=="*":
                first=int(first)*int(second)
            elif op=="/":
                first=int(first)/int(second)
            t1.insert("end",a)
            op=t1.get()
            flag=1
        elif a=="=":
            if(flag==1):
                t1.delete(0,"end")
            second=t1.get()
            t1.delete(0,"end")
            if op=="+":
                op_add(first,second)
            elif op=="-":
                op_sub(first,second)
            elif op=="/":
                    op_div(first,second)
            elif op=="*":
                op_mul(first,second)
        elif a=="<-":
            b=len(t1.get())
            t1.delete(b-1,b)

        else:
            if flag==1:
                t1.delete(0,"end")
                flag=0
            t1.insert("end",a)
first="#"
op="#"
b1=Button(top,text=1,command=lambda : abc(1))
b2=Button(top,text=2,command=lambda : abc(2))
b3=Button(top,text=3,command=lambda : abc(3))
b4=Button(top,text=4,command=lambda : abc(4))
b5=Button(top,text=5,command=lambda : abc(5))
b6=Button(top,text=6,command=lambda : abc(6))
b7=Button(top,text=7,command=lambda : abc(7))
b8=Button(top,text=8,command=lambda : abc(8))
b9=Button(top,text=9,command=lambda : abc(9))
b10=Button(top,text=0,command=lambda : abc(0))
b11=Button(top,text="+",command=lambda : abc("+"))
b12=Button(top,text="<-",command=lambda : abc("<-"))
b13=Button(top,text="-",command=lambda : abc("-"))
b14=Button(top,text="/",command=lambda : abc("/"))
b15=Button(top,text="*",command=lambda : abc("*"))
b16=Button(top,text="=",command=lambda : abc("="))

b1.place(x=50,y=110,width=30,height=30)
b2.place(x=100,y=110,width=30,height=30)
b3.place(x=150,y=110,width=30,height=30)
b4.place(x=200,y=110,width=30,height=30)
b5.place(x=50,y=160,width=30,height=30)
b6.place(x=100,y=160,width=30,height=30)
b7.place(x=150,y=160,width=30,height=30)
b8.place(x=200,y=160,width=30,height=30)
b9.place(x=50,y=220,width=30,height=30)
b10.place(x=100,y=220,width=30,height=30)
b11.place(x=150,y=220,width=30,height=30)
b12.place(x=200,y=220,width=30,height=30)
b13.place(x=50,y=280,width=30,height=30)
b14.place(x=100,y=280,width=30,height=30)
b15.place(x=150,y=280,width=30,height=30)
b16.place(x=200,y=280,width=30,height=30)
top.mainloop()
