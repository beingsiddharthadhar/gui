from tkinter import*
root=Tk()
root.title("Calculator")
e=Entry(root, width=50,borderwidth=50)
e.grid(row=0,column=0,columnspan=3,padx=30,pady=10)
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0, str(current)+ str(number))
    return
def button_clean():
    e.delete(0,END)

def button_add():
    first_number=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    e.delete(0,END)

    return
def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=="addition":
     e.insert(0,f_num+ int(second_number))
    if math == "subtraction":
         e.insert(0, f_num - int(second_number))
    if math == "multiplication":
         e.insert(0, f_num * int(second_number))
    if math== "division":
        e.insert(0,f_num/int(second_number))


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
    return
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0, END)
    return
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
    return

button1=Button(root,text="1",padx=50,pady=40,command=lambda: button_click(1))
button2=Button(root,text="2",padx=50,pady=40,command=lambda:button_click(2))
button3=Button(root,text="3",padx=50,pady=40,command=lambda:button_click(3))
button4=Button(root,text="4",padx=50,pady=40,command=lambda:button_click(4))
button5=Button(root,text="5",padx=50,pady=40,command=lambda:button_click(5))
button6=Button(root,text="6",padx=50,pady=40,command=lambda:button_click(6))
button7=Button(root,text="7",padx=50,pady=40,command=lambda:button_click(7))
button8=Button(root,text="8",padx=50,pady=40,command=lambda:button_click(8))
button9=Button(root,text="9",padx=50,pady=40,command=lambda:button_click(9))
button0=Button(root,text="0",padx=50,pady=40,command=lambda:button_click(0))
button_add=Button(root,text="+",padx=39,pady=40,command=button_add)
button_equal=Button(root,text="=",padx=91,pady=40,command=button_equal)
button_clear=Button(root,text="Clear",padx=50,pady=40,command=lambda:button_clean())
button_subtract=Button(root,text="-",padx=39,pady=40,command=button_subtract)
button_multiply=Button(root,text="*",padx=39,pady=40,command=button_multiply)
button_divide=Button(root,text="/",padx=39,pady=40,command=button_divide)

button1.grid(row=3,column=0)
button2.grid(row=3, column=1)
button3.grid(row=3,column=2)
button4.grid(row=2, column=0)
button5.grid(row=2,column=1)
button6.grid(row=2, column=2)
button7.grid(row=1,column=0)
button8.grid(row=1, column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)
button_add.grid(row=1,column=3,columnspan=1)
button_equal.grid(row=4,column=2)
button_clear.grid(row=4,column=1,columnspan=1)
button_subtract.grid(row=2,column=3)
button_multiply.grid(row=4,column=3)
button_divide.grid(row=3,column=3)
mybutton= Button(root,)




root.mainloop()

