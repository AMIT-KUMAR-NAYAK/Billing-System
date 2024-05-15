import tkinter as tk
from PIL import Image,ImageTk

root=tk.Tk()
root.config(background="#fcb6d7")
root.geometry("800x800")

#HEADING

frame_heading=tk.Frame(root,border=5,relief="groove",bg="#ff9cca")
frame_heading.pack(fill="x")

img_logo=ImageTk.PhotoImage(Image.open("logo.jpg"))
label_logo=tk.Label(frame_heading,image=img_logo,bg="#fcb6d7",width=100,height=100)
label_logo.image=img_logo
label_logo.pack(anchor="n")

label_name=tk.Label(frame_heading,text="SNACK MONKEY",font="sanserif 22 bold",bg="#ff9cca",fg="#fcebf3",width=14,height=1,highlightthickness=3,highlightbackground="#ff0080")
label_name.pack(anchor="n")

#MENU
list=[]
def add_list(n):
    global list
    list.append(n)

def process(list):
    s=0
    for i in list:
        s=s+i
    root.destroy()
    payment(s)

def paid():
    root.destroy()

def close():
    root.destroy()

def payment(n):
    global root
    root=tk.Tk()
    root.config(background="#fcb6d7")
    root.geometry("800x800")

    label_pay=tk.Label(root,text="Amount : $"+str(n),bg="pink",font="sanserif 18 bold underline",fg="black")
    label_pay.pack(anchor="center")

    frame_pay=tk.Frame(root,bg="#fcb6d7")
    frame_pay.pack(anchor="center",pady=20)

    button_pay=tk.Button(frame_pay,text="Pay",bg="pink",font="sanserif 18 bold",fg="black",command=paid)
    button_pay.grid(row=0,column=0,padx=10)

    button_close=tk.Button(frame_pay,text="Close",bg="pink",font="sanserif 18 bold",fg="black",command=close)
    button_close.grid(row=0,column=1)

    root.mainloop()

label_menu=tk.Label(root,text="MENU",font="sanserif 20 bold",fg="#ff0080",bg="#fcb6d7",highlightbackground="#ff0080",highlightthickness=3).pack(anchor="n")

frame_menu=tk.Frame(root,bg="pink")
frame_menu.pack(anchor="w")

label_regular=tk.Label(frame_menu,text="REGULARS",bg="pink",font="sanserif 18 bold underline",fg="black").pack()

check_food1=tk.Checkbutton(frame_menu,text="Coffee Latte - 10$",bg="pink",font="sanserif 18 bold",fg="black",command=lambda:add_list(10))
check_food1.pack(anchor="w")

check_food2=tk.Checkbutton(frame_menu,text="Pumpkin Pie - 15$",bg="pink",font="sanserif 18 bold",fg="black",command=lambda:add_list(15))
check_food2.pack(anchor="w")

check_food3=tk.Checkbutton(frame_menu,text="Espresso - 10$",bg="pink",font="sanserif 18 bold",fg="black",command=lambda:add_list(10))
check_food3.pack(anchor="w")

check_food4=tk.Checkbutton(frame_menu,text="Black Coffee - 5$",bg="pink",font="sanserif 18 bold",fg="black",command=lambda:add_list(5))
check_food4.pack(anchor="w")

check_food5=tk.Checkbutton(frame_menu,text="Capucchino - 10$",bg="pink",font="sanserif 18 bold",fg="black",command=lambda:add_list(10))
check_food5.pack()

label_special=tk.Label(frame_menu,text="SPECIAL",bg="pink",font="sanserif 18 bold underline",fg="black").pack()

check_food6=tk.Checkbutton(frame_menu,text="Yerba Matte - 12$",bg="pink",font="sanserif 18 bold",fg="black",command=lambda:add_list(12))
check_food6.pack()

button_order=tk.Button(root,text="ORDER",bg="pink",font="sanserif 18 bold",fg="black",command=lambda:process(list)).pack(anchor="center")

root.mainloop()
