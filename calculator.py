

from tkinter import *

root=Tk()
root.title("Calculator")

root.geometry("320x595")
root.configure(bg="lavender")
root.iconbitmap("asd.ico")


e=Entry(root,width=24,borderwidth=10,bg='light green',font=5)
e.grid(row=0,column=0,columnspan=4,padx=20,pady=20)
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def button_clear():
    e.delete(0,END)
def button_add():
    first_number=e.get()
    global f_num,a
    f_num=int(first_number)
    e.delete(0,END)
    a=1
def button_minus():
    first_number=e.get()
    global f_num,a
    f_num=int(first_number)
    e.delete(0,END)
    a=2
def button_mul():
    first_number=e.get()
    global f_num,a
    f_num=int(first_number)
    e.delete(0,END)
    a=3

def button_div():
    first_number=e.get()
    global f_num,a
    f_num=int(first_number)
    e.delete(0,END)
    a=4

def button_rem():
    first_number=e.get()
    global f_num,a
    f_num=int(first_number)
    e.delete(0,END)
    a=5


def button_equal():
    second_number=e.get()
    e.delete(0,END)



    if a==1:
        e.insert(0,f_num+int(second_number))
    elif a==2:
        e.insert(0,f_num-int(second_number))
    elif a==3:
        e.insert(0,f_num*int(second_number))  
    elif a/4:
            e.insert(0,f_num/int(second_number))
    elif a%5:
            e.insert(0,f_num%int(second_number))              
    else:
        e.insert(0,f_num+int(second_number))



button_1=Button(root,text="1",padx=10,pady=10,command=lambda:button_click(1),borderwidth=15,height=1, width=3,bg='gray',font=("Courier New",16,'bold'))
button_2=Button(root,text="2",padx=10,pady=10,command=lambda:button_click(2),borderwidth=15,height=1, width=3,bg='gray',font=("Courier New",16,'bold'))    
button_3=Button(root,text="3",padx=10,pady=10,command=lambda:button_click(3),borderwidth=15,height=1, width=3,bg='gray',font=("Courier New",16,'bold'))
button_4=Button(root,text="4",padx=10,pady=10,command=lambda:button_click(4),borderwidth=15,height=1, width=3,bg='gray',font=("Courier New",16,'bold'))
button_5=Button(root,text="5",padx=10,pady=10,command=lambda:button_click(5),borderwidth=15,height=1, width=3,bg='gray',font=("Courier New",16,'bold')) 
button_6=Button(root,text="6",padx=10,pady=10,command=lambda:button_click(6),borderwidth=15,height=1, width=3,bg='gray',font=("Courier New",16,'bold')) 
button_7=Button(root,text="7",padx=10,pady=10,command=lambda:button_click(7),borderwidth=15,height=1, width=3,bg='gray',font=("Courier New",16,'bold')) 
button_8=Button(root,text="8",padx=10,pady=10,command=lambda:button_click(8),borderwidth=15,height=1, width=3,bg='gray',font=("Courier New",16,'bold')) 
button_9=Button(root,text="9",padx=10,pady=10,command=lambda:button_click(9),borderwidth=15,height=1, width=3,bg='gray',font=("Courier New",16,'bold'))
button_0=Button(root,text="0",padx=10,pady=10,command=lambda:button_click(0),borderwidth=15,height=1, width=3,bg='gray',font=("Courier New",16,'bold'))
button_add=Button(root,text="+",padx=10,pady=10,command=button_add,borderwidth=15,height=1, width=3,bg='light blue',font=("Courier New",16,'bold'))
button_minus=Button(root,text="-",padx=10,pady=10,command=button_minus,borderwidth=15,height=1, width=3,bg='light blue',font=("Courier New",16,'bold'))
button_mul=Button(root,text="*",padx=10,pady=10,command=button_mul,borderwidth=15,height=1, width=3,bg='light blue',font=("Courier New",16,'bold'))
button_div=Button(root,text="/",padx=10,pady=10,command=button_div,borderwidth=15,height=1, width=3,bg='light blue',font=("Courier New",16,'bold'))
button_rem=Button(root,text="%",padx=10,pady=10,command=button_rem,borderwidth=15,height=1, width=3,bg='light blue',font=("Courier New",16,'bold'))
button_equal=Button(root,text="=",padx=10,pady=10,command=button_equal,borderwidth=15,height=1, width=3,bg='light blue',font=("Courier New",16,'bold'))
button_clear=Button(root,text="clear",bg='red',padx=60,pady=10,command=button_clear,borderwidth=15,height=1, width=3,font=("Courier New",16,'bold'))  

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
 
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_minus.grid(row=5,column=1)
button_mul.grid(row=5,column=2)
button_div.grid(row=6,column=0)
button_rem.grid(row=6,column=1)
button_equal.grid(row=6,column=2)
root.mainloop()



