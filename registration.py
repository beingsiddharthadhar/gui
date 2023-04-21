from tkinter import *
root =Tk()
root.geometry("500x300")
Label(root, text="Python Registration form", font="times 15 bold").grid(row=0,column=3)
name_user= Label(root,text="Student Name")
name_user.grid(row=1,column=2)
branch_user=Label(root,text="Branch")
branch_user.grid(row=2,column=2)
address_user=Label(root,text="Address")
address_user.grid(row=3,column=2)
phno_user=Label(root,text="Phone Number")
phno_user.grid(row=4,column=2)
dob_user=Label(root,text="Date of birth")
dob_user.grid(row=5,column=2)
gender_user=Label(root,text="Gender")
gender_user.grid(row=6,column=2)
gender1_user=Label(root,text="")
gender1_user.grid(row=7,column=2)
def submit_value():
    print("your information has been saved successfully")


name_value=StringVar
branch_value=StringVar
address_value=StringVar
phno_value=StringVar
dob_value=StringVar
gender_value=IntVar
gender1_value=IntVar

name_box=Entry(root,textvariable= name_value)
name_box.grid(row=1,column=3)
branch_box=Entry(root,textvariable= branch_value)
branch_box.grid(row=2,column=3)
address_box=Entry(root,textvariable= address_value)
address_box.grid(row=3,column=3)
phno_box=Entry(root,textvariable= phno_value)
phno_box.grid(row=4,column=3)
dob_box=Entry(root,textvariable= dob_value)
dob_box.grid(row=5,column=3)
gender_box=Checkbutton(text="Male",variable= gender_value,)
gender_box.grid(row=6,column=3)
gender1_box=Checkbutton(text="Female", variable= gender1_value)
gender1_box.grid(row=6,column=4)
Button(text="SUBMIT",command=submit_value).grid(row=7,column=3)
root.mainloop()


