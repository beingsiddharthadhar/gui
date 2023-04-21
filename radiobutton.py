from tkinter import*
root=Tk()
root.title("Learn to code at sidhere.com")
MODES= [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Chilly","Chilly"),
    ("Chicken","Chicken")
]
pizza=StringVar()

for text,mode in MODES:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack()

    def clicked(value):
     myLabel=Label(root,text=value)
     myLabel.pack()
#Radiobutton(root,text="Option 1",value=1,command=lambda : clicked(r.get())).pack()
#Radiobutton(root,text="Option 2",value=2,command=lambda : clicked(r.get())).pack()
mylabel=Label(root,text=pizza.get())
mylabel.pack()
mybutton=Button(root,text="Click Me!",command=lambda :clicked(pizza.get()))
mybutton.pack()
root.mainloop()