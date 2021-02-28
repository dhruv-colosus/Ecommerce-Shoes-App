from tkinter import *
from PIL import ImageTk

def home():

    #root.destroy()
    global root5
    root5 = Tk()
    root5.title("Shoez")
    root5.geometry("1300x750")
    root5.resizable(False, False)


    bg = ImageTk.PhotoImage(file = "D:/Coding/my stuff/Tkinter Course/CS_PROJECT/sbg4.jpg")       #BACKGROUND IMAGE
    Label(root5, image=bg).place(x=0, y=0, relwidth=1, relheight=1 )

    l1 = Label(root5, fg='Cyan', font=("Azonix", 30, "bold"), text="Welcome to Shoezz")     #TOP LABEL
    l1.place(x=0, y=0, height=65, width=1300)

    bgg = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Logoo.png")  # BACKGROUND IMAGE
    Label(root5, image=bgg).place(x=240, y=2)

    bg1 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/sneakers.jpg")      #TYPE 1 SNEAKERS
    Label(root5, image=bg1).place(x=120, y=80)

    b1 = Button(root5, text="Sneakers", font=('Roboto', 14), command=sneakers)
    b1.place(x=250, y=340, height=40, width=262)


    bg2 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/sports.jpg")     #TYPE 2 SPORTS
    Label(root5, image=bg2).place(x=650, y=80)

    b2 = Button(root5, text="Sports", font=('Roboto', 14))
    b2.place(x=780, y=340, height=40, width=262)


    bg3 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/loafers.jpg")      #TYPE 3 LOAFERSS
    Label(root5, image=bg3).place(x=120, y=410)

    b3 = Button(root5, text="Loafers", font=('Roboto', 14))
    b3.place(x=250, y=670, height=40, width=262)


    bg4 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/formals.jpg")      #TYPE 4 FORMALS
    Label(root5, image=bg4).place(x=650, y=410)

    b4 = Button(root5, text="Formals", font=('Roboto', 14))
    b4.place(x=780, y=670, height=40, width=262)


    Label(root5, text='Select Any\nof These\nCategories', font=(14)).place(x=560, y=340, height=100, width=150 )

    Button(root5, text='Exit', command=quit).place(x=1200, y=10, height=40, width=60)

    root5.mainloop()

def home2():

    global root5
    root5 = Tk()
    root5.title("Apni Dukaan")
    root5.geometry("1300x750")
    root5.resizable(False, False)


    bg = ImageTk.PhotoImage(file = "D:/Coding/my stuff/Tkinter Course/CS_PROJECT/sbg4.jpg")       #BACKGROUND IMAGE
    Label(root5, image=bg).place(x=0, y=0, relwidth=1, relheight=1 )

    l1 = Label(root5, fg='Cyan', font=("Azonix", 30, "bold"), text="Welcome to Shoezz")     #TOP LABEL
    l1.place(x=0, y=0, height=65, width=1300)

    bgg = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/Logoo.png")  # BACKGROUND IMAGE
    Label(root5, image=bgg).place(x=240, y=2)

    bg1 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/sneakers.jpg")      #TYPE 1 SNEAKERS
    Label(root5, image=bg1).place(x=120, y=80)

    b1 = Button(root5, text="Sneakers", font=('Roboto', 14), command=sneakers)
    b1.place(x=250, y=340, height=40, width=262)


    bg2 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/sports.jpg")     #TYPE 2 SPORTS
    Label(root5, image=bg2).place(x=650, y=80)

    b2 = Button(root5, text="Sports", font=('Roboto', 14))
    b2.place(x=780, y=340, height=40, width=262)


    bg3 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/loafers.jpg")      #TYPE 3 LOAFERSS
    Label(root5, image=bg3).place(x=120, y=410)

    b3 = Button(root5, text="Loafers", font=('Roboto', 14))
    b3.place(x=250, y=670, height=40, width=262)


    bg4 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/formals.jpg")      #TYPE 4 FORMALS
    Label(root5, image=bg4).place(x=650, y=410)

    b4 = Button(root5, text="Formals", font=('Roboto', 14))
    b4.place(x=780, y=670, height=40, width=262)


    Label(root5, text='Select Any\nof These\nCategories', font=(14)).place(x=560, y=340, height=100, width=150 )

    Button(root5, text='Exit', command=quit).place(x=1200, y=10, height=40, width=60)

    root5.mainloop()


def sneakers():

    root5.destroy()

    global root6

    root6 = Tk()
    root6.title("Sneakers")
    root6.geometry("1300x750")
    root6.resizable(False, False)

    bg5 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/sbg4.jpg")  # BACKGROUND IMAGE
    Label(root6, image=bg5).place(x=0, y=0, relwidth=1, relheight=1)

    Label(root6, fg='Cyan', font=("Azonix", 30, "bold"), text="Exclusive Sneakers Collection").place(x=0, y=0, height=55, width=1300)

    bg1 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/vans_s.jpg")      #VANS
    Label(root6, image=bg1).place(x=120, y=80)
    Label(root6, text='Vans Sneakers: ₹3999', font=(14)).place(x=250, y=340, height=40, width=200)

    b1 = Button(root6, text='Buy Now')
    b1.place(x=450, y=340, height=40, width=60)


    bg2 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/puma_s.jfif")     #PUMA
    Label(root6, image=bg2).place(x=650, y=80)
    Label(root6, text='Puma Sneakers: ₹4999', font=(14)).place(x=780, y=340, height=40, width=200)

    b2 = Button(root6, text='Buy Now')
    b2.place(x=980, y=340, height=40, width=60)


    bg3 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/adi_s.jpeg")      #ADIDAS
    Label(root6, image=bg3).place(x=120, y=410)
    Label(root6, text='Adidas Sneakers: ₹7999', font=(14)).place(x=250, y=670, height=40, width=200)

    b3 = Button(root6, text='Buy Now')
    b3.place(x=450, y=670, height=40, width=60)


    bg4 = ImageTk.PhotoImage(file="D:/Coding/my stuff/Tkinter Course/CS_PROJECT/ShoeCategory/nike_s.jfif")      #NIKE
    Label(root6, image=bg4).place(x=650, y=410)
    Label(root6, text='Nike Sneakers: ₹8599', font=(14)).place(x=780, y=670, height=40, width=200)

    b1 = Button(root6, text='Buy Now')
    b1.place(x=980, y=670, height=40, width=60)


    Button(root6, text='Exit', command=quit).place(x=1200, y=10, height=40, width=60)

    root6.mainloop()


home()