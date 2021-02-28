from tkinter import *
from PIL import ImageTk
import mysql.connector as mycon


def home():

    root.destroy()
    global root5
    root5 = Tk()
    root5.title("Shoez")
    root5.geometry("1300x750")
    root5.resizable(False, False)

    bg = ImageTk.PhotoImage(file = r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/sbg7.jpg")       #BACKGROUND IMAGE
    Label(root5, image=bg).place(x=0, y=0, relwidth=1, relheight=1 )

    l1 = Label(root5, fg='white',bg="#c26e08", font=("Blade runner movie font", 30, "bold"), text="Welcome to Shoezz")     #TOP LABEL
    l1.place(x=0, y=0, height=67, width=1300)

    bgg = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Shoezz3.png")  # LOGO
    Label(root5, image=bgg,borderwidth=0).place(x=30)

    root5.iconphoto(False, bgg)

    bg1 = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/sneakers.jpg")      #TYPE 1 SNEAKERS
    Label(root5, image=bg1).place(x=120, y=82)

    b1 = Button(root5, text="Sneakers", font=('Roboto', 14),bd=0.1, command=sneakers, bg='white', fg='black')
    b1.place(x=250, y=342, height=40, width=262)
    def entered(event):
        b1.config( bg="grey",fg="black")
    def left(event):
        b1.config(bg="white",fg="black")
    b1.bind("<Enter>",entered)
    b1.bind("<Leave>",left)

    


    bg2 = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/sports.jpg")     #TYPE 2 SPORTS
    Label(root5, image=bg2).place(x=650, y=82)
    

    b2 = Button(root5, text="Sports",command=sports, font=('Roboto', 14),bd=0.1, bg='white', fg='black')
    b2.place(x=780, y=342, height=40, width=262)
    def entered1(event):
        b2.config( bg="grey",fg="black")
    def left1(event):
        b2.config(bg="white",fg="black")
    b2.bind("<Enter>",entered1)
    b2.bind("<Leave>",left1)



    bg3 = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/loafers.jpg")      #TYPE 3 LOAFERSS
    Label(root5, image=bg3).place(x=120, y=412)

    b3 = Button(root5, text="Loafers",command=loafers, font=('Roboto', 14),bd=0.1, bg='white', fg='black')
    b3.place(x=250, y=672, height=40, width=262)
    def entered2(event):
        b3.config( bg="grey",fg="black")
    def left2(event):
        b3.config(bg="white",fg="black")
    b3.bind("<Enter>",entered2)
    b3.bind("<Leave>",left2)



    bg4 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/formals.jpg")      #TYPE 4 FORMALS
    Label(root5, image=bg4).place(x=650, y=412)

    b4 = Button(root5, text="Formals",command=formals, font=('Roboto', 14),bd=0.1, bg='white', fg='black')
    b4.place(x=780, y=672, height=40, width=262)
    def entered3(event):
        b4.config( bg="grey",fg="black")
    def left3(event):
        b4.config(bg="white",fg="black")
    b4.bind("<Enter>",entered3)
    b4.bind("<Leave>",left3)



    Label(root5, text='Select Any\nof These\nCategories', font=('Lato',14)).place(x=560, y=342, height=100, width=150 )

    b6 = Button(root5, text="My Orders",command=OrderHist1, font=('Roboto', 14),bd=0.1, bg='white', fg='black')
    b6.place(x=1090, y=10, height=40, width=100)
    def entered3(event):
        b6.config( bg="grey",fg="black")
    def left3(event):
        b6.config(bg="white",fg="black")
    b6.bind("<Enter>",entered3)
    b6.bind("<Leave>",left3)

    b5=Button(root5, text='Exit', command=quit,font=('Roboto', 12),bd=0.1, bg='white', fg='black')    
    b5.place(x=1200, y=10, height=40, width=60)
    def entered4(event):
        b5.config( bg="#e32c22",fg="white")
    def left4(event):
        b5.config(bg="white",fg="black")
    b5.bind("<Enter>",entered4)
    b5.bind("<Leave>",left4)

    root5.mainloop()

def home2():


    global root5
    root5 = Tk()
    root5.title("Shoez")
    root5.geometry("1300x750")
    root5.resizable(False, False)


    bg = ImageTk.PhotoImage(file = r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/sbg7.jpg")       #BACKGROUND IMAGE
    Label(root5, image=bg).place(x=0, y=0, relwidth=1, relheight=1 )

    l1 = Label(root5, fg='white',bg="#c26e08", font=("Blade runner movie font", 30, "bold"), text="Welcome to Shoezz")     #TOP LABEL
    l1.place(x=0, y=0, height=67, width=1300)

    bgg = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Shoezz3.png")  # LOGO
    Label(root5, image=bgg,borderwidth=0).place(x=30)

    root5.iconphoto(False, bgg)

    bg1 = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/sneakers.jpg")      #TYPE 1 SNEAKERS
    Label(root5, image=bg1).place(x=120, y=82)

    b1 = Button(root5, text="Sneakers", font=('Roboto', 14),bd=0.1, command=sneakers, bg='white', fg='black')
    b1.place(x=250, y=342, height=40, width=262)
    def entered(event):
        b1.config( bg="grey",fg="black")
    def left(event):
        b1.config(bg="white",fg="black")
    b1.bind("<Enter>",entered)
    b1.bind("<Leave>",left)

    


    bg2 = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/sports.jpg")     #TYPE 2 SPORTS
    Label(root5, image=bg2).place(x=650, y=82)
    

    b2 = Button(root5, text="Sports", font=('Roboto', 14),bd=0.1,command=sports, bg='white', fg='black')
    b2.place(x=780, y=342, height=40, width=262)
    def entered1(event):
        b2.config( bg="grey",fg="black")
    def left1(event):
        b2.config(bg="white",fg="black")
    b2.bind("<Enter>",entered1)
    b2.bind("<Leave>",left1)



    bg3 = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/loafers.jpg")      #TYPE 3 LOAFERSS
    Label(root5, image=bg3).place(x=120, y=412)

    b3 = Button(root5, text="Loafers", font=('Roboto', 14),bd=0.1,command=loafers, bg='white', fg='black')
    b3.place(x=250, y=672, height=40, width=262)
    def entered2(event):
        b3.config( bg="grey",fg="black")
    def left2(event):
        b3.config(bg="white",fg="black")
    b3.bind("<Enter>",entered2)
    b3.bind("<Leave>",left2)



    bg4 = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/formals.jpg")      #TYPE 4 FORMALS
    Label(root5, image=bg4).place(x=650, y=412)

    b4 = Button(root5, text="Formals", font=('Roboto', 14),bd=0.1,command=formals, bg='white', fg='black')
    b4.place(x=780, y=672, height=40, width=262)
    def entered3(event):
        b4.config( bg="grey",fg="black")
    def left3(event):
        b4.config(bg="white",fg="black")
    b4.bind("<Enter>",entered3)
    b4.bind("<Leave>",left3)



    Label(root5, text='Select Any\nof These\nCategories', font=('Lato',14)).place(x=560, y=342, height=100, width=150 )

    b6 = Button(root5, text="My Orders",command=OrderHist1, font=('Roboto', 14),bd=0.1, bg='white', fg='black')
    b6.place(x=1090, y=10, height=40, width=100)
    def entered3(event):
        b6.config( bg="grey",fg="black")
    def left3(event):
        b6.config(bg="white",fg="black")
    b6.bind("<Enter>",entered3)
    b6.bind("<Leave>",left3)

    b5=Button(root5, text='Exit', command=quit,font=('Roboto', 12),bd=0.1, bg='white', fg='black')
    b5.place(x=1200, y=10, height=40, width=60)
 
    def entered4(event):
        b5.config( bg="#e32c22",fg="white")
    def left4(event):
        b5.config(bg="white",fg="black")
    b5.bind("<Enter>",entered4)
    b5.bind("<Leave>",left4)

    root5.mainloop()

def revert():
    root6.destroy()
    home2()

def revert2():
    root7.destroy()
    home2()

def revert3():
    root8.destroy()
    home2()

def revert4():
    root9.destroy()
    home2()

def revert5():
    root12.destroy()
    home2()
def revert6():
    root13.destroy()
    home2()
def revert9():
    root15.destroy()
    home2()
def revert8():
    root14.destroy()
    home2()
def revert10():
    root10.destroy()
    home2()
               
def sneakers():

    root5.destroy()

    global root6

    root6 = Tk()
    root6.title("Sneakers")
    root6.geometry("1300x750")
    root6.resizable(False, False)

    bg5 = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/sbg8.png")  # BACKGROUND IMAGE
    Label(root6, image=bg5).place(x=0, y=0, relwidth=1, relheight=1)

    # Label(root6, fg='Cyan', font=("Azonix", 30, "bold"), text="Exclusive Sneakers Collection").place(x=0, y=0, height=67, width=1300)

    # bgg = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Shoezz3.png")  # LOGO IMAGE
    # Label(root6, image=bgg).place(x=240)
    l1 = Label(root6, fg='white',bg="#c26e08", font=("Blade runner movie font", 30, "bold"), text="Sneakers Collection")     #TOP LABEL
    l1.place(x=0, y=0, height=67, width=1300)

    bgg = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Shoezz3.png")  # LOGO
    Label(root6, image=bgg,borderwidth=0).place(x=30)

    root6.iconphoto(False, bgg)

    bg1 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/vans_s.jpg")      #VANS
    Label(root6, image=bg1).place(x=120, y=80)
    Label(root6, text='Vans Sneakers: ₹3999', font=("Lato",14)).place(x=250, y=340, height=40, width=200)



    b1 = Button(root6, text='Add',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart(0))
    b1.place(x=450, y=340, height=40, width=60)
    def entered(event):
        b1.config( bg="grey",fg="white")
    def left(event):
        b1.config(bg="white",fg="black")
    b1.bind("<Enter>",entered)
    b1.bind("<Leave>",left)


    bg2 = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/puma_s.jfif")     #PUMA
    Label(root6, image=bg2).place(x=650, y=80)
    Label(root6, text='Puma Sneakers: ₹4999', font=("Lato",14)).place(x=780, y=340, height=40, width=200)

    b2 = Button(root6, text='Add',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart(1))
    b2.place(x=980, y=340, height=40, width=60)
    def entered1(event):
        b2.config( bg="grey",fg="white")
    def left1(event):
        b2.config(bg="white",fg="black")
    b2.bind("<Enter>",entered1)
    b2.bind("<Leave>",left1)


    bg3 = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/adi_s.jpg")      #ADIDAS
    Label(root6, image=bg3).place(x=120, y=410)
    Label(root6, text='Adidas Sneakers: ₹7999', font=("Lato",14)).place(x=230, y=670, height=40, width=230)

    b3 = Button(root6, text='Add',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart(2))
    b3.place(x=450, y=670, height=40, width=60)
    def entered2(event):
        b3.config( bg="grey",fg="white")
    def left2(event):
        b3.config(bg="white",fg="black")
    b3.bind("<Enter>",entered2)
    b3.bind("<Leave>",left2)


    bg4 = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/nike_s.jfif")      #NIKE
    Label(root6, image=bg4).place(x=650, y=410)
    Label(root6, text='Nike Sneakers: ₹8599', font=("Lato",14)).place(x=780, y=670, height=40, width=200)

    b4 = Button(root6, text='Add',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart(3))
    b4.place(x=980, y=670, height=40, width=60)
    def entered4(event):
        b4.config( bg="grey",fg="white")
    def left4(event):
        b4.config(bg="white",fg="black")
    b4.bind("<Enter>",entered4)
    b4.bind("<Leave>",left4)


    b5=Button(root6, text='Exit', command=quit,font=('Roboto', 12),bd=0.1, bg='white', fg='black')
    b5.place(x=1200, y=10, height=40, width=60)
    b6=Button(root6, text='MyCart', command=MyCart1,font=('Roboto', 12),bd=0.1, bg='white', fg='black')
    b6.place(x=1100, y=10, height=40, width=60)
    def entered4(event):
        b5.config( bg="#e32c22",fg="white")
    def left4(event):
        b5.config(bg="white",fg="black")
    b5.bind("<Enter>",entered4)
    b5.bind("<Leave>",left4)

    b6=Button(root6, text='Back', command=revert,font=('Roboto', 12),bd=0.1, bg='white', fg='black' )
    b6.place(height=40, width=50,x=10, y=90)
    def entered5(event):
        b6.config( bg="#38eb2f",fg="white")
    def left5(event):
        b6.config(bg="white",fg="black")
    b6.bind("<Enter>",entered5)
    b6.bind("<Leave>",left5)
    
    # root6.attributes("-alpha", 0.5)

    root6.mainloop()




def sports():
    
    root5.destroy()

    global root8

    root8 = Tk()
    root8.title("Sports Shoes")
    root8.geometry("1300x750")
    root8.resizable(False, False)

    bg5 = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/sbg8.png")  # BACKGROUND IMAGE
    Label(root8, image=bg5).place(x=0, y=0, relwidth=1, relheight=1)

    # Label(root6, fg='Cyan', font=("Azonix", 30, "bold"), text="Exclusive Sneakers Collection").place(x=0, y=0, height=67, width=1300)

    # bgg = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Shoezz3.png")  # LOGO IMAGE
    # Label(root6, image=bgg).place(x=240)
    l1 = Label(root8, fg='white',bg="#c26e08", font=("Blade runner movie font", 30, "bold"), text="Sports Shoes")     #TOP LABEL
    l1.place(x=0, y=0, height=67, width=1300)

    bgg = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Shoezz3.png")  # LOGO
    Label(root8, image=bgg,borderwidth=0).place(x=30)

    root8.iconphoto(False, bgg)

    bg1 = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/AdiLaceup.png")      #ADI SPORTS
    Label(root8, image=bg1).place(x=120, y=80)
    Label(root8, text='Adidas Stin: ₹3899', font=("Lato",14)).place(x=250, y=340, height=40, width=200)

    b1 = Button(root8, text='Add',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart2(0))
    b1.place(x=450, y=340, height=40, width=60)
    def entered(event):
        b1.config( bg="grey",fg="white")
    def left(event):
        b1.config(bg="white",fg="black")
    b1.bind("<Enter>",entered)
    b1.bind("<Leave>",left)


    bg2 = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/PumaHybrid.png")     #PUMA SPORTS
    Label(root8, image=bg2).place(x=650, y=80)
    Label(root8, text='Puma Hybrid: ₹5249', font=("Lato",14)).place(x=780, y=340, height=40, width=200)

    b2 = Button(root8, text='Add',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart2(1))
    b2.place(x=980, y=340, height=40, width=60)
    def entered1(event):
        b2.config( bg="grey",fg="white")
    def left1(event):
        b2.config(bg="white",fg="black")
    b2.bind("<Enter>",entered1)
    b2.bind("<Leave>",left1)


    bg3 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/NikeRevolution.png")      #NIKE SPORTS
    Label(root8, image=bg3).place(x=120, y=410)
    Label(root8, text='Nike Revolution: ₹3399', font=("Lato",14)).place(x=230, y=670, height=40, width=230)

    b3 = Button(root8, text='Add',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart2(2))
    b3.place(x=450, y=670, height=40, width=60)
    def entered2(event):
        b3.config( bg="grey",fg="white")
    def left2(event):
        b3.config(bg="white",fg="black")
    b3.bind("<Enter>",entered2)
    b3.bind("<Leave>",left2)


    bg4 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/Skechers.jpeg")      #SKECHERS SPORTS
    Label(root8, image=bg4).place(x=650, y=410)
    Label(root8, text='Skechers GoRun: ₹3444', font=("Lato",14)).place(x=760, y=670, height=40, width=220)

    b4 = Button(root8, text='Add',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart2(3))
    b4.place(x=980, y=670, height=40, width=60)
    def entered4(event):
        b4.config( bg="grey",fg="white")
    def left4(event):
        b4.config(bg="white",fg="black")
    b4.bind("<Enter>",entered4)
    b4.bind("<Leave>",left4)


    b5=Button(root8, text='Exit', command=quit,font=('Roboto', 12),bd=0.1, bg='white', fg='black')
    b5.place(x=1200, y=10, height=40, width=60)
    b6=Button(root8, text='MyCart', command=MyCart2,font=('Roboto', 12),bd=0.1, bg='white', fg='black')
    b6.place(x=1100, y=10, height=40, width=60)
    def entered4(event):
        b5.config( bg="#e32c22",fg="white")
    def left4(event):
        b5.config(bg="white",fg="black")
    b5.bind("<Enter>",entered4)
    b5.bind("<Leave>",left4)

    b6=Button(root8, text='Back', command=revert3,font=('Roboto', 12),bd=0.1 , bg='white', fg='black')
    b6.place(height=40, width=50,x=10, y=90)
    def entered5(event):
        b6.config( bg="#38eb2f",fg="white")
    def left5(event):
        b6.config(bg="white",fg="black")
    b6.bind("<Enter>",entered5)
    b6.bind("<Leave>",left5)
    
    # root6.attributes("-alpha", 0.5)

    root8.mainloop()   



def loafers():
    
    root5.destroy()

    global root7

    root7 = Tk()
    root7.title("Loafers")
    root7.geometry("1300x750")
    root7.resizable(False, False)

    bg5 = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/sbg8.png")  # BACKGROUND IMAGE
    Label(root7, image=bg5).place(x=0, y=0, relwidth=1, relheight=1)

    # Label(root6, fg='Cyan', font=("Azonix", 30, "bold"), text="Exclusive Sneakers Collection").place(x=0, y=0, height=67, width=1300)

    # bgg = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Shoezz3.png")  # LOGO IMAGE
    # Label(root6, image=bgg).place(x=240)
    l1 = Label(root7, fg='white',bg="#c26e08", font=("Blade runner movie font", 30, "bold"), text="Loafers Collection")     #TOP LABEL
    l1.place(x=0, y=0, height=67, width=1300)

    bgg = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Shoezz3.png")  # LOGO
    Label(root7, image=bgg,borderwidth=0).place(x=30)

    root7.iconphoto(False, bgg)

    bg1 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/RedChief.jpeg")      #REDCHIEF LOAFERS
    Label(root7, image=bg1).place(x=120, y=80)
    Label(root7, text='RedChief: ₹1899', font=("Lato",14)).place(x=250, y=340, height=40, width=200)

    b1 = Button(root7, text='Add',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart3(0))
    b1.place(x=450, y=340, height=40, width=60)
    def entered(event):
        b1.config( bg="grey",fg="white")
    def left(event):
        b1.config(bg="white",fg="black")
    b1.bind("<Enter>",entered)
    b1.bind("<Leave>",left)


    bg2 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/USPolo.jpeg")     #USPA LOAFERS
    Label(root7, image=bg2).place(x=650, y=80)
    Label(root7, text='US Polo Assn.: ₹2700', font=("Lato",14)).place(x=780, y=340, height=40, width=200)

    b2 = Button(root7, text='Add',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart3(1))
    b2.place(x=980, y=340, height=40, width=60)
    def entered1(event):
        b2.config( bg="grey",fg="white")
    def left1(event):
        b2.config(bg="white",fg="black")
    b2.bind("<Enter>",entered1)
    b2.bind("<Leave>",left1)


    bg3 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/Levis.jpeg")      #LEVI'S LOAFERS
    Label(root7, image=bg3).place(x=120, y=410)
    Label(root7, text="Levi's Justin: ₹2299", font=("Lato",14)).place(x=230, y=670, height=40, width=230)

    b3 = Button(root7, text='Add',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart3(2))
    b3.place(x=450, y=670, height=40, width=60)
    def entered2(event):
        b3.config( bg="grey",fg="white")
    def left2(event):
        b3.config(bg="white",fg="black")
    b3.bind("<Enter>",entered2)
    b3.bind("<Leave>",left2)


    bg4 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/Puma.jpeg")      #PUMA LOAFERS
    Label(root7, image=bg4).place(x=650, y=410)
    Label(root7, text='Puma Elara: ₹2099', font=("Lato",14)).place(x=780, y=670, height=40, width=200)

    b4 = Button(root7, text='Add',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart3(3))
    b4.place(x=980, y=670, height=40, width=60)
    def entered4(event):
        b4.config( bg="grey",fg="white")
    def left4(event):
        b4.config(bg="white",fg="black")
    b4.bind("<Enter>",entered4)
    b4.bind("<Leave>",left4)


    b5=Button(root7, text='Exit', command=quit,font=('Roboto', 12),bd=0.1, bg='white', fg='black')
    b5.place(x=1200, y=10, height=40, width=60)
    b6=Button(root7, text='MyCart', command=MyCart3,font=('Roboto', 12),bd=0.1, bg='white', fg='black')
    b6.place(x=1100, y=10, height=40, width=60)
    def entered4(event):
        b5.config( bg="#e32c22",fg="white")
    def left4(event):
        b5.config(bg="white",fg="black")
    b5.bind("<Enter>",entered4)
    b5.bind("<Leave>",left4)

    b6=Button(root7, text='Back', command=revert2,font=('Roboto', 12),bd=0.1 , bg='white', fg='black')
    b6.place(height=40, width=50,x=10, y=90)
    def entered5(event):
        b6.config( bg="#38eb2f",fg="white")
    def left5(event):
        b6.config(bg="white",fg="black")
    b6.bind("<Enter>",entered5)
    b6.bind("<Leave>",left5)
    
    # root6.attributes("-alpha", 0.5)

    root7.mainloop()    



def formals():
    
    root5.destroy()

    global root9

    root9 = Tk()
    root9.title("Formals")
    root9.geometry("1300x750")
    root9.resizable(False, False)

    bg5 = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/sbg8.png")  # BACKGROUND IMAGE
    Label(root9, image=bg5).place(x=0, y=0, relwidth=1, relheight=1)

    l1 = Label(root9, fg='white',bg="#c26e08", font=("Blade runner movie font", 30, "bold"), text="Formals Collection")     #TOP LABEL
    l1.place(x=0, y=0, height=67, width=1300)

    bgg = ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Shoezz3.png")  # LOGO
    Label(root9, image=bgg,borderwidth=0).place(x=30)

    root9.iconphoto(False, bgg)

    bg1 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/Arrow.jpeg")      #ARROW FORMALS
    Label(root9, image=bg1).place(x=120, y=80)
    Label(root9, text='Arrow Mill: ₹2899', font=("Lato",14)).place(x=250, y=340, height=40, width=200)

    b1 = Button(root9, text='Add',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart4(0))
    b1.place(x=450, y=340, height=40, width=60)
    def entered(event):
        b1.config( bg="grey",fg="white")
    def left(event):
        b1.config(bg="white",fg="black")
    b1.bind("<Enter>",entered)
    b1.bind("<Leave>",left)


    bg2 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/HushPuppies.jpeg")     #HUSHPUPPIES FORMALS
    Label(root9, image=bg2).place(x=650, y=80)
    Label(root9, text='HushPuppies: ₹2399', font=("Lato",14)).place(x=780, y=340, height=40, width=200)

    b2 = Button(root9, text='Add',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart4(1))
    b2.place(x=980, y=340, height=40, width=60)
    def entered1(event):
        b2.config( bg="grey",fg="white")
    def left1(event):
        b2.config(bg="white",fg="black")
    b2.bind("<Enter>",entered1)
    b2.bind("<Leave>",left1)


    bg3 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/LeeCooper.jpeg")      #LEECOOPER FORMALS
    Label(root9, image=bg3).place(x=120, y=410)
    Label(root9, text='LeeCooper: ₹2099', font=("Lato",14)).place(x=230, y=670, height=40, width=230)

    b3 = Button(root9, text='Add',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart4(2))
    b3.place(x=450, y=670, height=40, width=60)
    def entered2(event):
        b3.config( bg="grey",fg="white")
    def left2(event):
        b3.config(bg="white",fg="black")
    b3.bind("<Enter>",entered2)
    b3.bind("<Leave>",left2)


    bg4 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/RedTape.jpeg")      #REDTAPE
    Label(root9, image=bg4).place(x=650, y=410)
    Label(root9, text='RedTape: ₹2599', font=("Lato",14)).place(x=780, y=670, height=40, width=200)

    b4 = Button(root9, text='Add',font=("roboto",10), bg='white', fg='black', command=lambda *args: Cart4(3))
    b4.place(x=980, y=670, height=40, width=60)
    def entered4(event):
        b4.config( bg="grey",fg="white")
    def left4(event):
        b4.config(bg="white",fg="black")
    b4.bind("<Enter>",entered4)
    b4.bind("<Leave>",left4)


    b5=Button(root9, text='Exit', command=quit,font=('Roboto', 12),bd=0.1, bg='white', fg='black')
    b5.place(x=1200, y=10, height=40, width=60)
    b6=Button(root9, text='MyCart', command=MyCart4,font=('Roboto', 12),bd=0.1, bg='white', fg='black')
    b6.place(x=1100, y=10, height=40, width=60)
    def entered4(event):
        b5.config( bg="#e32c22",fg="white")
    def left4(event):
        b5.config(bg="white",fg="black")
    b5.bind("<Enter>",entered4)
    b5.bind("<Leave>",left4)

    b6=Button(root9, text='Back', command=revert4,font=('Roboto', 12),bd=0.1 , bg='white', fg='black')
    b6.place(height=40, width=50,x=10, y=90)
    def entered5(event):
        b6.config( bg="#38eb2f",fg="white")
    def left5(event):
        b6.config(bg="white",fg="black")
    b6.bind("<Enter>",entered5)
    b6.bind("<Leave>",left5)
    
    # root6.attributes("-alpha", 0.5)

    root9.mainloop()        

def main_window():   #this is the main login window where everything starts
    global pass_entry
    global user_entry
    global root
    global login_box
    global username11
   


    root=Tk()
    root.title("Login Lobby")
    root.geometry("1350x750")
    root.resizable(False,False)

    bg=ImageTk.PhotoImage(file=r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/sbg6.jpg")
    bg_image=Label(root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)

    bgg2 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Shoezz3.png")  # LOGO IMAGE

    root.iconphoto(False, bgg2)

    login_box=Frame(root,bg="white")
    login_box.place(x=110,y=165,height=480,width=600)   
    # #42f5bf

    #bgg2 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Shoezz.png")  # LOGO IMAGE
    #Label(root, image=bgg2).place(x=750, y=200)

    heading=Label(login_box,text="Login",font=("Azonix",38,"bold"),fg="#bf0d04",bg="white").place(x=210,y=30)
    heading=Label(login_box,text="Enter you username and password",font=("roboto",18,),fg="#bf0d04",bg="white").place(x=110,y=100)

    user_label=Label(login_box,text="Username :",font=("bebas",20),fg="black",bg="white").place(x=50,y=170)
    user_entry=Entry(login_box,font=("roboto,20"),fg="#3b3838",bg="#f7f7f7")
    user_entry.place(x=180,y=175,height=35,width=280)
    username11 = user_entry.get()



    pass_label= Label(login_box,text="Password :",font=("bebas",20),fg="black",bg="white").place(x=50,y=250)
    pass_entry=Entry(login_box,font=("roboto,20"),fg="#3b3838",bg="#f7f7f7",show="*")
    pass_entry.place(x=180,y=255,height=35,width=280)

    Forget_passwd=Button(login_box,text="Forgot Password?",font=("roboto",12),bg="white",fg="#bf0d04",bd=0).place(x=230,y=320)
    Login_passwd=Button(login_box,text="Login",command=mysql_login,font=("azonix",16),bg="#bf0d04",fg="white").place(x=240,y=370,width=120,height=60)

    signup_label=Label(login_box,text="Don't have an account ?",font=("roboto",12),bg="white",fg="black").place(x=169,y=442)
    sign_up_button=Button(login_box,text="Sign Up.",command=sign_up_here,font=("roboto",12),bg="white",fg="#bf0d04",bd=0).place(x=339,y=440)


    root.mainloop()

def sign_up_here(): #this is the sign_up window
    global user_entry1
    global pass_entry1
    global login_box1
    global root3
    root.destroy()
    root3=Tk()
    root3.title("SignUP Lobby")
    root3.geometry("1350x750")
    root3.resizable(False,False)

    bgg2 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Shoezz.png")  # LOGO IMAGE
    
    # root3.iconphoto(Fase,bgg2)

    bg1 = ImageTk.PhotoImage(file = r"D:/Coding/my stuff/Tkinter Course/CS_PROJECT/sbg3.jpg")
    bg_image1 = Label(root3, image = bg1)
    bg_image1.place(x=0, y=0, relwidth=1, relheight = 1)

    login_box1=Frame(root3,bg="white")
    login_box1.place(x=380,y=145,height=480,width=600)   
    # #42f5bf  

    heading1=Label(login_box1,text="SIGN UP",font=("Azonix",38,"bold"),fg="#bf0d04",bg="white").place(x=170,y=30)
    heading2=Label(login_box1,text="Enter you desired username and password",font=("roboto",18,),fg="#bf0d04",bg="white").place(x=65,y=100)

    user_label=Label(login_box1,text="Username :",font=("bebas",20),fg="black",bg="white").place(x=50,y=170)
    user_entry1=Entry(login_box1,font=("roboto,20"),fg="#3b3838",bg="#f7f7f7")
    user_entry1.place(x=180,y=175,height=35,width=280)



    pass_label=Label(login_box1,text="Password :",font=("bebas",20),fg="black",bg="white").place(x=50,y=250)
    pass_entry1=Entry(login_box1,font=("roboto,20"),fg="#3b3838",bg="#f7f7f7",show="*")
    pass_entry1.place(x=180,y=255,height=35,width=280)

    # Forget_passwd1=Button(login_box,text="Forgot Password?",font=("roboto",12),bg="white",fg="#bf0d04",bd=0).place(x=230,y=320)
    Login_passwd1=Button(login_box1,text="SIGN UP",command=mysql_sign_up,font=("azonix",16),bg="#bf0d04",fg="white").place(x=230,y=340,width=120,height=60)

    



   
def mysql_sign_up():
    global username1
    username1=user_entry1.get()
    password1=pass_entry1.get()
    mainlist1=[]
    user_list=[]
  

    
    con=mycon.connect(host="localhost",username="root",passwd="password123",database="project")

    cur=con.cursor()

    command="SELECT * FROM Login_Data"
    cur.execute(command)
    
    results=cur.fetchall()

    for a in results:
        d=list(a)
        mainlist1.append(a)
    for i in mainlist1:
        user=i[0]
        user_list.append(user)    

    if username1 in user_list :
        signup_label=Label(login_box1,text="Sorry this has already been taken",font=("roboto",12),bg="white",fg="black").place(x=169,y=442)
    elif username1=="" or password1=="":
        signup_label=Label(login_box1,text="Fill Out the Details completely",font=("roboto",12),bg="white",fg="black").place(x=169,y=442)
            
    else:
        signup_label=Label(login_box1,text="         Signed Up Successfully           ",font=("roboto",12),bg="white",fg="black").place(x=169,y=442)
        sql="INSERT INTO username VALUES (%s,%s)"
        val=(username1,password1)
        cur.execute(sql,val)
        con.commit()
        root3.destroy()
        main_window()






    
def login_fail(): #this is the login failed command
    
    # root2=Tk()
    # root2.title("Results")
    # root2.geometry("400x200")
    
    # output=Label(root2,text="Wrong Username/Password").pack()
  
    # root2.mainloop()
    #signup_label
    Label(login_box,text="Sorry,Try Again",font=("roboto",12),bg="white",fg="black").place(x=250,y=222)


def mysql_login(): #this is the Login Checker Command

    global username

    username = user_entry.get()
    password = pass_entry.get()
    mainlist = []

    
    con = mycon.connect(host="localhost",username="root",passwd="password123",database="project")

    cur = con.cursor()

    command = "SELECT * FROM Login_Data"
    cur.execute(command)
    mainmasala = (username, password)
    results = cur.fetchall()

    for a in results:
        mainlist.append(a)

    if mainmasala in mainlist:
        #print("Success")
        home()
    else:
        #print("Login Failed")
        login_fail()        




def OrderHist1():
    con = mycon.connect(host="localhost",username="root",passwd="password123",database="project")

    cur = con.cursor()

    command = "SELECT * FROM orders"
    cur.execute(command)
    orders = []
    results = cur.fetchall()

    for a in results:
        orders.append(a)
    #print(orders)

    myorders=[]

    for x in orders:
        if x[0]==username:
            myorders.append(x)


    root5.destroy()


    tx,ty=500,100
    px,py=700,100

    global root10
    root10 = Tk()
    root10.title("Cart")
    root10.geometry("1300x750")
    root10.resizable(False, False)
    #if:
    #else:
        #print("Login Failed")
    #    login_fail()        

    bg = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/sbg8.png")  # BACKGROUND IMAGE
    Label(root10, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

    ll = Label(root10, fg='white',bg="#c26e08", font=("Roboto", 30, "bold"), text="MY ORDER HISTORY")     #TOP LABEL
    ll.place(x=0, y=0, height=67, width=1300)

    bgg9 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Shoezz3.png")  # LOGO
    Label(root10, image=bgg9,borderwidth=0).place(x=30)

    root10.iconphoto(False, bgg9)
    
    if len(myorders)==0:
        Label(root10, text='Your do not have any recent orders', font=('Roboto',25)).place(x=350,y=300)
    i=0
    fakelist=[]
    for x in myorders:
        
        if x not in fakelist:
            i+=1
            Label(root10,text=str(i)+'.',font=('Roboto',11)).place(x=300,y=ty)
            Label(root10,text=x[1],font=('Roboto',11)).place(x=tx,y=ty)
            Label(root10, text='Qty: '+str(x[2]), font=('Roboto',11)).place(x=px,y=py)

            ty+=40
            py+=40
            fakelist.append(x)



    b5=Button(root10, text='Exit', command=quit,font=('Roboto', 12),bd=0.1, bg='white', fg='black')    
    b5.place(x=1200, y=10, height=40, width=60)
    def entered4(event):
        b5.config( bg="#e32c22",fg="white")
    def left4(event):
        b5.config(bg="white",fg="black")
    b5.bind("<Enter>",entered4)
    b5.bind("<Leave>",left4)


    b6=Button(root10, text='Back', command=revert10,font=('Roboto', 12),bd=0.1 , bg='white', fg='black')
    b6.place(height=40, width=50,x=10, y=90)
    def entered5(event):
        b6.config( bg="#38eb2f",fg="white")
    def left5(event):
        b6.config(bg="white",fg="black")
    b6.bind("<Enter>",entered5)
    b6.bind("<Leave>",left5)
    
            


    root10.mainloop()
    



#Cartt->
iCart=[]
def Cart(value):
    v=value
    iCart.append(items1[v])
def Cart2(value):
    v=value
    iCart.append(items2[v])
def Cart3(value):
    v=value
    iCart.append(items3[v])
def Cart4(value):
    v=value
    iCart.append(items4[v])            
def EndList():
    iCart=[]    
items1=['Vans','Puma','Adidas','Nike']
price1=[3999,4999,7999,8599]
items2=['AdidasStin','PumaHybrid','Nikerevolution','skechersGorun']
price2=[3899,5249,3399,3444]
items3=['RedChief','USPOLOASS','LeviJustin','PumaElara']
price3=[1899,2700,2299,2099]
items4=['ArrowMil','HushPuppies','LeeCooper','Redtape1']
price4=[2899,2399,2099,2599]
iCart=[]

def MyCart1():


    root6.destroy()
    global root12
    
    root12 = Tk()
    root12.title("Cart")
    root12.geometry("1300x750")
    root12.resizable(False, False)
    


    bg = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/sbg8.png")  # BACKGROUND IMAGE
    Label(root12, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

    ll = Label(root12, fg='white',bg="#c26e08", font=("Roboto", 30, "bold"), text="CONFIRM YOUR ORDER")     #TOP LABEL
    ll.place(x=0, y=0, height=67, width=1300)

    bgg2 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Shoezz3.png")  # LOGO
    Label(root12, image=bgg2,borderwidth=0).place(x=30)

    root12.iconphoto(False, bgg2)

    vansSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/vans_s(1).jpg")
    PumaSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/puma_s(1).jpg")
    AdiSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/adi_s(1).jpg")
    NikeSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/nike_s.jpg")

    images=[vansSn, PumaSn, AdiSn, NikeSn]

    ix,iy=190,100
    tx,ty=670,100
    px,py=670,140
    qx,qy=670,180

    if len(iCart)==0:
        Label(root12, text='Your Cart is Empty', font=('Roboto',25)).place(x=350,y=300)
    l=[]
    B1=Button(root12, text="Place Order",command=orderthisnow1, font=('Roboto',20)).place(x=950,y=370)
    b6=Button(root12, text='Back', command=revert5,font=('Roboto', 12),bd=0.1 , bg='white', fg='black')
    b6.place(height=40, width=50,x=10, y=90)
    for z in iCart:
        if z not in l:
            n=0
            for x in range(len(iCart)):
                if iCart[x]==z:
                    n+=1
            t1='Qty: '+str(n)
            Label(root12, image=images[items1.index(z)]).place(x=ix,y=iy)
            Label(root12, text=z, font=('Roboto',15)).place(x=tx,y=ty)
            Label(root12, text='Price: '+str(price1[items1.index(z)]), font=('Roboto',15)).place(x=px,y=py)
            Label(root12, text=t1, font=('Roboto',15)).place(x=qx,y=qy)
            l.append(z)
            iy+=150
            ty+=150
            py+=150
            qy+=150

        #B1=Button(root12, text="Place Order", font=('Roboto',25)).place(x=550,y=530)

    root12.mainloop()

def MyCart2():


    root8.destroy()
    global root13
    
    root13 = Tk()
    root13.title("Cart")
    root13.geometry("1300x750")
    root13.resizable(False, False)
    


    bg = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/sbg8.png")  # BACKGROUND IMAGE
    Label(root13, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

    ll = Label(root13, fg='white',bg="#c26e08", font=("Roboto", 30, "bold"), text="CONFIRM YOUR ORDER")     #TOP LABEL
    ll.place(x=0, y=0, height=67, width=1300)

    bgg2 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Shoezz3.png")  # LOGO
    Label(root13, image=bgg2,borderwidth=0).place(x=30)
    b6=Button(root13, text='Back', command=revert6,font=('Roboto', 12),bd=0.1 , bg='white', fg='black')
    b6.place(height=40, width=50,x=10, y=90)

    root13.iconphoto(False, bgg2)

    vansSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/AdiLaceup.jpg")
    PumaSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/PumaHybrid.jpg")
    AdiSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/NikeRevolution.jpg")
    NikeSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/Skechers.jpg")

    images=[vansSn, PumaSn, AdiSn, NikeSn]

    ix,iy=190,100
    tx,ty=670,100
    px,py=670,140
    qx,qy=670,180

    if len(iCart)==0:
        Label(root13, text='Your Cart is Empty', font=('Roboto',25)).place(x=350,y=300)
    l=[]
    B1=Button(root13, text="Place Order",command=orderthisnow2, font=('Roboto',20)).place(x=950,y=370)

    for z in iCart:
        if z not in l:
            n=0
            for x in range(len(iCart)):
                if iCart[x]==z:
                    n+=1
            t1='Qty: '+str(n)
            Label(root13, image=images[items2.index(z)]).place(x=ix,y=iy)
            Label(root13, text=z, font=('Roboto',15)).place(x=tx,y=ty)
            Label(root13, text='Price: '+str(price2[items2.index(z)]), font=('Roboto',15)).place(x=px,y=py)
            Label(root13, text=t1, font=('Roboto',15)).place(x=qx,y=qy)
            l.append(z)
            iy+=150
            ty+=150
            py+=150
            qy+=150

        #B1=Button(root13, text="Place Order", font=('Roboto',25)).place(x=550,y=530)

    root13.mainloop()

def MyCart3():


    root7.destroy()
    global root14
    
    root14 = Tk()
    root14.title("Cart")
    root14.geometry("1300x750")
    root14.resizable(False, False)
    


    bg = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/sbg8.png")  # BACKGROUND IMAGE
    Label(root14, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

    ll = Label(root14, fg='white',bg="#c26e08", font=("Roboto", 30, "bold"), text="CONFIRM YOUR ORDER")     #TOP LABEL
    ll.place(x=0, y=0, height=67, width=1300)

    bgg2 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Shoezz3.png")  # LOGO
    Label(root14, image=bgg2,borderwidth=0).place(x=30)

    root14.iconphoto(False, bgg2)
    b6=Button(root14, text='Back', command=revert8,font=('Roboto', 12),bd=0.1 , bg='white', fg='black')
    b6.place(height=40, width=50,x=10, y=90)

    vansSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/RedChief.jpg")
    PumaSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/USPolo.jpg")
    AdiSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/Levis.jpg")
    NikeSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/Puma.jpg")

    images=[vansSn, PumaSn, AdiSn, NikeSn]

    ix,iy=190,100
    tx,ty=670,100
    px,py=670,140
    qx,qy=670,180

    if len(iCart)==0:
        Label(root14, text='Your Cart is Empty', font=('Roboto',25)).place(x=350,y=300)
    l=[]
    B1=Button(root14, text="Place Order",command=orderthisnow3, font=('Roboto',20)).place(x=950,y=370)

    for z in iCart:
        if z not in l:
            n=0
            for x in range(len(iCart)):
                if iCart[x]==z:
                    n+=1
            t1='Qty: '+str(n)
            Label(root14, image=images[items3.index(z)]).place(x=ix,y=iy)
            Label(root14, text=z, font=('Roboto',15)).place(x=tx,y=ty)
            Label(root14, text='Price: '+str(price3[items3.index(z)]), font=('Roboto',15)).place(x=px,y=py)
            Label(root14, text=t1, font=('Roboto',15)).place(x=qx,y=qy)
            l.append(z)
            iy+=150
            ty+=150
            py+=150
            qy+=150

        #B1=Button(root14, text="Place Order", font=('Roboto',25)).place(x=550,y=530)

    root14.mainloop()    
def MyCart4():


    root9.destroy()
    global root15
    
    root15 = Tk()
    root15.title("Cart")
    root15.geometry("1300x750")
    root15.resizable(False, False)
    


    bg = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/sbg8.png")  # BACKGROUND IMAGE
    Label(root15, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

    ll = Label(root15, fg='white',bg="#c26e08", font=("Roboto", 30, "bold"), text="CONFIRM YOUR ORDER")     #TOP LABEL
    ll.place(x=0, y=0, height=67, width=1300)
    b6=Button(root15, text='Back', command=revert9,font=('Roboto', 12),bd=0.1 , bg='white', fg='black')
    b6.place(height=40, width=50,x=10, y=90)
    bgg2 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Shoezz3.png")  # LOGO
    Label(root15, image=bgg2,borderwidth=0).place(x=30)

    root15.iconphoto(False, bgg2)

    vansSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/Arrow.jpg")
    PumaSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/HushPuppies.jpg")
    AdiSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/LeeCooper.jpg")
    NikeSn = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/RedTape.jpg")

    images=[vansSn, PumaSn, AdiSn, NikeSn]

    ix,iy=190,100
    tx,ty=670,100
    px,py=670,140
    qx,qy=670,180

    if len(iCart)==0:
        Label(root15, text='Your Cart is Empty', font=('Roboto',25)).place(x=350,y=300)
    l=[]
    B1=Button(root15, text="Place Order",command=orderthisnow4, font=('Roboto',20)).place(x=950,y=370)

    for z in iCart:
        if z not in l:
            n=0
            for x in range(len(iCart)):
                if iCart[x]==z:
                    n+=1
            t1='Qty: '+str(n)
            Label(root15, image=images[items4.index(z)]).place(x=ix,y=iy)
            Label(root15, text=z, font=('Roboto',15)).place(x=tx,y=ty)
            Label(root15, text='Price: '+str(price4[items4.index(z)]), font=('Roboto',15)).place(x=px,y=py)
            Label(root15, text=t1, font=('Roboto',15)).place(x=qx,y=qy)
            l.append(z)
            iy+=150
            ty+=150
            py+=150
            qy+=150

        #B1=Button(root14, text="Place Order", font=('Roboto',25)).place(x=550,y=530)

    root15.mainloop()    


def orderthisnow1():

    Label(root12, text='Your order has been Placed Successfully', font=('Roboto',20)).place(x=400,y=630)
    order_mysql()
def orderthisnow2():
    Label(root13, text='Your order has been Placed Successfully', font=('Roboto',20)).place(x=400,y=630)
    order_mysql()
def orderthisnow3():
    Label(root14, text='Your order has been Placed Successfully', font=('Roboto',20)).place(x=400,y=630)
    order_mysql()
def orderthisnow4():
    Label(root15, text='Your order has been Placed Successfully', font=('Roboto',20)).place(x=400,y=630)
    order_mysql()


def order_mysql():
    con=mycon.connect(host="localhost",username="root",passwd="password123",database="project")
    #username = username1
    l=[]
    for z in iCart:
        if z not in l:
            n=0
            for x in range(len(iCart)):
                if iCart[x]==z:
                    n+=1
            qtyy=n
            orders=z
            cur=con.cursor()
            sql="INSERT INTO orders VALUES (%s,%s,%s)"
            val=(username,orders,qtyy)
            cur.execute(sql,val)
            con.commit()
            l.append(z)
    

    
main_window()

