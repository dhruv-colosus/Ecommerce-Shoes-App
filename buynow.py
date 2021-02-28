from tkinter import *
from PIL import ImageTk
from tkinter import ttk

items=['Vans','Puma','Adidas','Nike']
price=[3999,4999,7999,8599]
iCart=[]
#items me list ki jagah ek dict define karni hai with key as price


v=0

def Cart(value):
    v=value
    iCart.append(items[v])


def MyCart():


    root6.destroy()

    
    root = Tk()
    root.title("Cart")
    root.geometry("1300x750")
    root.resizable(False, False)

    # Scroll_Frame=Frame(root)
    # Scroll_Frame.pack(fill=BOTH,expand=1)

    # ScrollCanvas=Canvas(Scroll_Frame)
    # ScrollCanvas.pack(side=LEFT,fill=BOTH,expand=1)

    # FinalScrollbar=ttk.Scrollbar(Scroll_Frame,orient=VERTICAL,command=ScrollCanvas.yview)
    # FinalScrollbar.pack(side=RIGHT,fill=Y)

    # ScrollCanvas.configure(yscrollcommand=FinalScrollbar.set)
    # ScrollCanvas.bind('<Configure>',lambda e: ScrollCanvas.configure(scrollregion=ScrollCanvas.bbox("all")))
    
    
    bg = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/sbg8.png")  # BACKGROUND IMAGE
    Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

    ll = Label(root, fg='white',bg="#c26e08", font=("Roboto", 30, "bold"), text="CONFIRM YOUR ORDER")     #TOP LABEL
    ll.place(x=0, y=0, height=67, width=1300)

    bgg2 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Shoezz3.png")  # LOGO
    Label(root, image=bgg2,borderwidth=0).place(x=30)

    root.iconphoto(False, bgg2)

    vansSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/vans_s.jpg")
    PumaSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/puma_s.jfif")
    AdiSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/adi_s.jpg")
    NikeSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/nike_s.jfif")

    images=[vansSn, PumaSn, AdiSn, NikeSn]

    ix,iy=150,100
    tx,ty=670,100
    px,py=670,160
    qx,qy=670,220

    if len(iCart)==0:
        Label(root, text='Your Cart is Empty', font=('Roboto',25)).place(x=350,y=300)
    for z in iCart:
        Label(root, image=images[items.index(z)]).place(x=ix,y=iy)
        Label(root, text=z, font=('Roboto',25)).place(x=tx,y=ty)
        Label(root, text='Price: '+str(price[items.index(z)]), font=('Roboto',25)).place(x=px,y=py)
        Label(root, text='Qty: 1', font=('Roboto',25)).place(x=qx,y=qy)
        iy+=300
        ty+=300
        py+=300
        qy+=300




    

#root5.destroy()

global root6

root6 = Tk()
root6.title("Sneakers")
root6.geometry("1300x750")
root6.resizable(False, False)

bg5 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/sbg8.png")  # BACKGROUND IMAGE
Label(root6, image=bg5).place(x=0, y=0, relwidth=1, relheight=1)

# Label(root6, fg='Cyan', font=("Azonix", 30, "bold"), text="Exclusive Sneakers Collection").place(x=0, y=0, height=67, width=1300)

# bgg = ImageTk.PhotoImage(file="F:\Tkinter Course\Login System\CS_PROJECT\Shoezz3.png")  # LOGO IMAGE
# Label(root6, image=bgg).place(x=240)
l1 = Label(root6, fg='white',bg="#c26e08", font=("Blade runner movie font", 30, "bold"), text="Sneakers Collection")     #TOP LABEL
l1.place(x=0, y=0, height=67, width=1300)

bgg = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Shoezz3.png")  # LOGO
Label(root6, image=bgg,borderwidth=0).place(x=30)

root6.iconphoto(False, bgg)

bg1 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/vans_s.jpg")      #VANS
Label(root6, image=bg1).place(x=120, y=80)
Label(root6, text='Vans Sneakers: ₹3999', font=("Lato",14)).place(x=250, y=340, height=40, width=200)

b1 = Button(root6, text='Buy Now',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart(0))
b1.place(x=450, y=340, height=40, width=60)
def entered(event):
    b1.config( bg="grey",fg="white")
def left(event):
    b1.config(bg="white",fg="black")
b1.bind("<Enter>",entered)
b1.bind("<Leave>",left)


bg2 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory\puma_s.jfif")     #PUMA
Label(root6, image=bg2).place(x=650, y=80)
Label(root6, text='Puma Sneakers: ₹4999', font=("Lato",14)).place(x=780, y=340, height=40, width=200)

b2 = Button(root6, text='Buy Now',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart(1))
b2.place(x=980, y=340, height=40, width=60)
def entered1(event):
    b2.config( bg="grey",fg="white")
def left1(event):
    b2.config(bg="white",fg="black")
b2.bind("<Enter>",entered1)
b2.bind("<Leave>",left1)


bg3 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/adi_s.jpg")      #ADIDAS
Label(root6, image=bg3).place(x=120, y=410)
Label(root6, text='Adidas Sneakers: ₹7999', font=("Lato",14)).place(x=230, y=670, height=40, width=230)

b3 = Button(root6, text='Buy Now',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart(2))
b3.place(x=450, y=670, height=40, width=60)
def entered2(event):
    b3.config( bg="grey",fg="white")
def left2(event):
    b3.config(bg="white",fg="black")
b3.bind("<Enter>",entered2)
b3.bind("<Leave>",left2)


bg4 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/nike_s.jfif")      #NIKE
Label(root6, image=bg4).place(x=650, y=410)
Label(root6, text='Nike Sneakers: ₹8599', font=("Lato",14)).place(x=780, y=670, height=40, width=200)

b4 = Button(root6, text='Buy Now',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart(3))
b4.place(x=980, y=670, height=40, width=60)
def entered4(event):
    b4.config( bg="grey",fg="white")
def left4(event):
    b4.config(bg="white",fg="black")
b4.bind("<Enter>",entered4)
b4.bind("<Leave>",left4)


b5=Button(root6, text='MyCart', command=MyCart,font=('Roboto', 12),bd=0.1, bg='white', fg='black')
b5.place(x=1200, y=10, height=40, width=60)
def entered4(event):
    b5.config( bg="#e32c22",fg="white")
def left4(event):
    b5.config(bg="white",fg="black")
b5.bind("<Enter>",entered4)
b5.bind("<Leave>",left4)

#b6=Button(root6, text='Back', command=revert,font=('Roboto', 12),bd=0.1, bg='white', fg='black' )
#b6.place(height=40, width=50,x=10, y=90)
#def entered5(event):
#    b6.config( bg="#38eb2f",fg="white")
#def left5(event):
#    b6.config(bg="white",fg="black")
#b6.bind("<Enter>",entered5)
#b6.bind("<Leave>",left5)

# root6.attributes("-alpha", 0.5)

root6.mainloop()



