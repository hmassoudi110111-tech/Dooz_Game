import tkinter
from tkinter import*
from tkinter import PhotoImage
from tkinter import messagebox
import random
import numpy as np
r=Tk()
r.title('Dooz')
r.geometry('600x600')
c=Canvas(r)
global p
global A
p=0
A=np.array([['-','-','-'],['-','-','-'],['-','-','-']])
def testwin(i,j,x,y,p1):
    global A,p
    if(p1==1):
        if(A[i][j]=='-'):
            A[i][j]='x'
            Bp=Button(r,text='x')
            Bp.place(relx=x,rely=y,relwidth=0.3,relheight=0.3)
            p=2
            lp=Label(r,text='player2',fg='red')
            lp.place(relx=0,rely=0,relwidth=0.3,relheight=0.05)
            if((A[0][0]=='x')and(A[1][1]=='x')and(A[2][2]=='x')):
                messagebox.showinfo("","player1 win")
                return
            if((A[0][2]=='x')and(A[1][1]=='x')and(A[2][0]=='x')):
                messagebox.showinfo("","player1 win")
                return
            t=0
            for i1 in range(3):
                c=0
                for j1 in range(3):
                    if(A[i1][j1]=='x'):
                        c+=1
                if(c==3):
                    t=1
                    break
            if(t==1):
                messagebox.showinfo("","player1 win")
                return
            t=0
            for i1 in range(3):
                c=0
                for j1 in range(3):
                    if(A[j1][i1]=='x'):
                        c+=1
                if(c==3):
                    t=1
                    break
            if(t==1):
                messagebox.showinfo("","player1 win")
                return
    if(p1==2):
        if(A[i][j]=='-'):
            A[i][j]='o'
            Bp=Button(r,text='o')
            Bp.place(relx=x,rely=y,relwidth=0.3,relheight=0.3)
            p=1
            lp=Label(r,text='player1',fg='green')
            lp.place(relx=0,rely=0,relwidth=0.3,relheight=0.05)
            if((A[0][0]=='o')and(A[1][1]=='o')and(A[2][2]=='o')):
                messagebox.showinfo("","player2 win")
                return
            if((A[0][2]=='o')and(A[1][1]=='o')and(A[2][0]=='o')):
                messagebox.showinfo("","player2 win")
                return
            t=0
            for i1 in range(3):
                c=0
                for j1 in range(3):
                    if(A[i1][j1]=='o'):
                        c+=1
                if(c==3):
                    t=1
                    break
            if(t==1):
                messagebox.showinfo("","player2 win")
                return
            t=0
            for i1 in range(3):
                c=0
                for j1 in range(3):
                    if(A[j1][i1]=='o'):
                        c+=1
                if(c==3):
                    t=1
                    break
            if(t==1):
                messagebox.showinfo("","player2 win")
                return
def startbtn():
    global p
    y=random.randint(1,2)
    if (y==1):
        p=1
        lp=Label(r,text='player1',fg='green')
        lp.place(relx=0,rely=0,relwidth=0.3,relheight=0.05)
    elif(y==2):
        p=2
        lp=Label(r,text='player2',fg='red')
        lp.place(relx=0,rely=0,relwidth=0.3,relheight=0.05)
img1=PhotoImage(file='1.png')
B1=Button(r,image=img1,command=lambda:testwin(0,0,0.05,0.05,p))
B1.place(relx=0.05,rely=0.05,relwidth=0.3,relheight=0.3)
img2=PhotoImage(file='1.png')
B2=Button(r,image=img2,command=lambda:testwin(0,1,0.35,0.05,p))
B2.place(relx=0.35,rely=0.05,relwidth=0.3,relheight=0.3)
img3=PhotoImage(file='1.png')
B3=Button(r,image=img3,command=lambda:testwin(0,2,0.65,0.05,p))
B3.place(relx=0.65,rely=0.05,relwidth=0.3,relheight=0.3)
img4=PhotoImage(file='1.png')
B4=Button(r,image=img4,command=lambda:testwin(1,0,0.05,0.35,p))
B4.place(relx=0.05,rely=0.35,relwidth=0.3,relheight=0.3)
img5=PhotoImage(file='1.png')
B5=Button(r,image=img5,command=lambda:testwin(1,1,0.35,0.35,p))
B5.place(relx=0.35,rely=0.35,relwidth=0.3,relheight=0.3)
img6=PhotoImage(file='1.png')
B6=Button(r,image=img6,command=lambda:testwin(1,2,0.65,0.35,p))
B6.place(relx=0.65,rely=0.35,relwidth=0.3,relheight=0.3)
img7=PhotoImage(file='1.png')
B7=Button(r,image=img7,command=lambda:testwin(2,0,0.05,0.65,p))
B7.place(relx=0.05,rely=0.65,relwidth=0.3,relheight=0.3)
img8=PhotoImage(file='1.png')
B8=Button(r,image=img8,command=lambda:testwin(2,1,0.35,0.65,p))
B8.place(relx=0.35,rely=0.65,relwidth=0.3,relheight=0.3)
img9=PhotoImage(file='1.png')
B9=Button(r,image=img9,command=lambda:testwin(2,2,0.65,0.65,p))
B9.place(relx=0.65,rely=0.65,relwidth=0.3,relheight=0.3)
B10=Button(r,text='start',command=lambda:startbtn())
B10.place(relx=0.6,rely=0,relwidth=0.3,relheight=0.05)
r.mainloop()
