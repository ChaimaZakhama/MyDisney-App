from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#on importe le module messagebox pour les alertes
t = Tk()

t.geometry("800x700")

t.title('My Project Disneyland 🤍')
t.resizable(height=False,width=False)

def afficher_home():
    canvas1.delete("all")

    canvas1.create_image(0, 0, image=bg, anchor="nw")
    canvas1.create_image(10, 5, image=icon, anchor="nw")

    canvas1.create_text(400, 100, text="Welcome to Disneyland", font=("Verdana", 30,"bold"), fill="white")
    canvas1.create_text(400, 150, text="The magic world!", font=("Verdana", 15,"bold","italic"), fill="white")

    button1 = Button(t, text="Explore", font=("Verdana", 14), bg="plum", fg="white",command=afficher_explore )
    button2 = Button(t, text="Sign up", font=("Verdana", 14), bg="plum", fg="white", command=signUp)
    button3 = Button(t, text=" Log in ", font=("Verdana", 14), bg="plum", fg="white", command=logIn)
    def callback():
        if messagebox.askyesno('exit?', 'Are you sure you want to exit?'):
            messagebox.showinfo('', 'Bye!') 
            t.destroy()
        else:
            messagebox.showinfo('', 'okay!')
            
    btn_exit= Button(t, text="  Exit   ",font=("Verdana", 14) , bg="plum", fg="white", command=callback)
    button1_canvas = canvas1.create_window(120, 225, anchor="nw", window=button1)
    button2_canvas = canvas1.create_window(120, 275, anchor="nw", window=button2)
    button3_canvas = canvas1.create_window(120, 325, anchor="nw", window=button3)
    btn_exit_canvas= canvas1.create_window(120, 375, anchor="nw", window=btn_exit)

def afficher_explore():
    canvas1.delete("all")

    canvas1.configure(bg='mistyrose')
    canvas1.create_image(10, 5, image=icon, anchor="nw")

    canvas1.create_text(400, 50, text="Your best guide to make magical memories", font=("Helvetica", 14,"bold","italic"), fill="steelblue")
    
    #image it's a small world
    def my_command1():
       canvas1.create_text(200, 300, text="It's a Small World", font=("Verdana", 12), fill="black")

    #Let us create a label for button event
    img_label1= Label(image=click_btn1)

    button_cl1= Button(t, image=click_btn1,command= my_command1,borderwidth=0)
    button_cl1_canvas= canvas1.create_window(30, 85, anchor="nw", window=button_cl1)


    #image fantasy garden
    def my_command2():
       canvas1.create_text(575, 300, text="Fantasy garden", font=("Verdana", 12), fill="black")

    #Let us create a label for button event
    img_label2= Label(image=click_btn2)

    button_cl2= Button(t, image=click_btn2,command= my_command2,borderwidth=0)
    button_cl2_canvas= canvas1.create_window(425, 85, anchor="nw", window=button_cl2)

    #image night show
    def my_command3():
       canvas1.create_text(200, 600, text="Night show", font=("Verdana", 12), fill="black")

    #Let us create a label for button event
    img_label3= Label(image=click_btn3)

    button_cl3= Button(t, image=click_btn3,command= my_command3,borderwidth=0)
    button_cl3_canvas= canvas1.create_window(30, 350, anchor="nw", window=button_cl3)

    #image Hyperspace mountain
    def my_command4():
       canvas1.create_text(575, 600, text="Hyperspace mountain", font=("Verdana", 12), fill="black")

    #Let us create a label for button event
    img_label4= Label(image=click_btn4)

    button_cl4= Button(t, image=click_btn4,command= my_command4,borderwidth=0)
    button_cl4_canvas= canvas1.create_window(425, 350, anchor="nw", window=button_cl4)



    # Ajouter un bouton "back" en bas de la page
    button2 = Button(t, text="Back", font=("Verdana", 14), bg="plum", fg="white", command=afficher_home)
    button4_canvas = canvas1.create_window(360, 650, anchor="nw", window=button2)
    
def submit_signUp(nom,em,pwd,cp):
    name = nom.get()
    email = em.get()
    password = pwd.get()
    confirm_password= cp.get()
    l=[]
    if not name or not email or not password or not confirm_password:
        messagebox.showwarning('Try again :(',"All fields are required")
      
    elif password != confirm_password:
        messagebox.showwarning('Try again :(',"Passwords do not match")
        
    elif email in users:
        messagebox.showwarning('Try again :(',"This email already exists")
        
    else:
        messagebox.showinfo('Welcome 🤍!',"Account created successfully")
        l.append(name)
        l.append(email)
        l.append(password)
        users[email] = l
        print(users)
        canvas1.delete("all")
        signUp()

def submit_book_ticket(nbr_tickets, email):
    nbr=nbr_tickets.get()
    if not nbr:
        messagebox.showwarning(':( Try again', "Enter the number of tickets you want to buy!")
    else:
        messagebox.showinfo(':) Congrats!', 'You have booked : '+nbr+' tickets ,Enjoy your day in Disneyland!')
        canvas1.delete("all")
        book_ticket(email)
def recommendations(email):
    canvas1.delete("all")
    canvas1.configure(bg='mistyrose')
    canvas1.create_image(10, 5, image=icon, anchor="nw")
    canvas1.create_image(140, 50, image=Disney fan 1, anchor="nw")
    label = Label(t,text="'My trip to Disneyland was pure magic! \n The atmosphere, the rides, and the \n characters  made me feel like a kid again.\n It's definitely a must-visit destination \n for anyone seeking some enchantment \n in their life.' \n\n -Disney fan 1-\n Rate: ★★★★★ 5/5 ", font=("verdana",12),bg="mistyrose",fg="dimgray")
    canvas1.create_window(620, 200, window=label)
    canvas1.create_image(140, 375, image=Disney fan 2, anchor="nw")
    label = Label(t,text="'Disneyland was a dream come true! \n The attractions were amazing, \n the atmosphere was magical, \n and the experience was unforgettable. \n Highly recommend it! ' \n\n -Disney fan 2-\n  Rate: ★★★★☆ 4/5 ", font=("verdana",12),bg="mistyrose",fg="dimgray")
    canvas1.create_window(620, 500, window=label)
    button2 = Button(t, text="Back", font=("Verdana", 14), bg="plum", fg="white", command= lambda: book_ticket(email))
    button4_canvas = canvas1.create_window(660, 20, anchor="nw", window=button2)
def book_ticket(email):
    l=users[email]
    canvas1.delete("all")
    canvas1.configure(bg='pink')
    #canvas1.create_image(0, 0, image=bg, anchor="nw")
    canvas1.create_image(20, 0, image=icon, anchor="nw")
    label = Label(t,text="Welcome, "+l[0]+" 🤍!", font=("verdana",18,"italic bold"),bg="pink",fg="darkmagenta")
    canvas1.create_window(370, 80, window=label)
    label = Label(t,text="Book your ticket and live your dream ", font=("verdana",13),bg="pink",fg="deeppink")
    canvas1.create_window(380, 110, window=label)
   
    show_label =  Label(t, text="You want to attend the night show?",bg='mistyrose', font=("Verdana", 12))
    value = StringVar()
    bouton1 = Radiobutton(t, text="Yes", variable=value, value=1,bg='mistyrose', font=("Verdana", 12))
    bouton2 = Radiobutton(t, text="No", variable=value, value=2,bg='mistyrose', font=("Verdana", 12))

    canvas1.create_window(140, 140, anchor=NW, window=show_label)
    canvas1.create_window(460, 140, anchor=NW, window=bouton1)
    canvas1.create_window(540, 140, anchor=NW, window=bouton2)

    valuee =  StringVar()
    visit_label =  Label(t, text="Choose the places you want to visit in Disneyland:",bg='mistyrose', font=("Verdana", 12))
    bout1 = Radiobutton(t, text="Fantasy garden",variable=valuee, value=1,bg='mistyrose', font=("Verdana", 12))
    bout2 = Radiobutton(t, text="It's a Small World",variable=valuee, value=2,bg='mistyrose', font=("Verdana", 12))
    bout3 = Radiobutton(t, text="Hyperspace mountain",variable=valuee, value=3,bg='mistyrose', font=("Verdana", 12))
    bout4 = Radiobutton(t, text="Castle of Magical Dreams",variable=valuee, value=4,bg='mistyrose', font=("Verdana", 12))

    canvas1.create_window(140, 180, anchor=NW, window=visit_label)
    canvas1.create_window(180, 210, anchor=NW, window=bout1)
    canvas1.create_window(180, 250, anchor=NW, window=bout2)
    canvas1.create_window(180, 290, anchor=NW, window=bout3)
    canvas1.create_window(180, 330, anchor=NW, window=bout4)

    '''

    numtickets_label =  Label(t, text= "Number of tickets you want to buy:",bg='mistyrose', font=("Verdana", 12))
    numtickets_spinbox =  Spinbox(t, from_=1, to='infinity')
    '''
    label = Label(t,text="Number of tickets you want to buy:", font=("verdana",12),bg="mistyrose")
    canvas1.create_window(140, 380, window=label, anchor="nw")
    numtickets= Entry(t)
    canvas1.create_window(450, 380, window=numtickets, anchor="nw")

    duration_label =  Label(t, text="Duration: ",bg='mistyrose', font=("Verdana", 12))
    my_value = StringVar()
    boutt1 = Radiobutton(t, text="Full day (7+ hours)", variable=my_value, value=1,bg='mistyrose', font=("Verdana", 12))
    boutt2 = Radiobutton(t, text="Multi-day", variable=my_value, value=2,bg='mistyrose', font=("Verdana", 12))

    canvas1.create_window(140, 420, window=duration_label, anchor="nw")
    canvas1.create_window(180, 460, window=boutt1, anchor="nw")
    canvas1.create_window(180, 500, window=boutt2, anchor="nw")
    
    canvas1.create_image(600, 370, image=mickey, anchor="nw")
    canvas1.lift(mickey)
    button_book_ticket = Button(t, text="Confirm", bg="plum", font=("verdana", 14),fg="white",command=lambda: submit_book_ticket(numtickets,email))
    button_book_ticket_canvas = canvas1.create_window(325, 550, anchor="nw", window=button_book_ticket)
    
    button2 = Button(t, text="Log out",  bg="plum", font=("verdana", 14),fg="white", command=logIn)
    button4_canvas = canvas1.create_window(500, 20, anchor="nw", window=button2)
    button2 = Button(t, text="Recommendations",  bg="plum", font=("verdana", 14),fg="white", command= lambda :recommendations(email))
    button4_canvas = canvas1.create_window(595, 20, anchor="nw", window=button2)
   
    canvas1.create_rectangle(120, 130, 600, 600, width=2,fill="mistyrose", outline="violet")


def submit_logIn(email,pwd):
    passwd = pwd.get()
    email1 = email.get()
    if not passwd or not email1 :
        messagebox.showwarning('Try again :( ',"All fields are required")
        
    elif email1 in users:
        e=users[email1]
        if e[2]==passwd : #e=[name,email,passwd]
            #print("hey")
            book_ticket(email1)
        else:
            canvas1.create_text(400, 210, text="Password is incorrect", fill="red", font=("Verdana", 11))
    else:
        messagebox.showwarning(':(',"Email doesn't exist")
        
def signUp():
    canvas1.delete("all")
    label = Label(t, text="Create your account", bg="mistyrose", font=("Verdana", 18, "bold"))
    canvas1.create_window(400, 135, window=label)
    canvas1.create_image(0, 0, image=bg1, anchor="nw")
    canvas1.create_image(20, 0, image=icon, anchor="nw")

    title_label =  Label(t, text="Title :",bg='mistyrose', font=("Verdana", 14))
    title_combobox = ttk.Combobox(t, values=["", "Mr.", "Ms.", "Dr."])
    canvas1.create_window(250, 180, window=title_label)
    canvas1.create_window(450, 180, window=title_combobox)
    
    label = Label(t, text="Name :", bg="mistyrose", font=("Verdana", 14))
    canvas1.create_window(250, 210, window=label)
    nom = Entry(t)
    canvas1.create_window(450, 210, window=nom)

    label = Label(t, text="Email :", bg="mistyrose", font=("Verdana", 14))
    canvas1.create_window(250, 240, window=label)
    email = Entry(t)
    canvas1.create_window(450, 240, window=email)

    label = Label(t, text="Password:", bg="mistyrose", font=("Verdana", 14))
    canvas1.create_window(250, 270, window=label)
    password = Entry(t, show="*")
    canvas1.create_window(450, 270, window=password)

    label = Label(t, text="Confirm password :", bg="mistyrose", font=("Verdana", 14))
    canvas1.create_window(260, 300, window=label)
    confirm_password = Entry(t, show="*")
    canvas1.create_window(450, 300, window=confirm_password)

    register_button = Button(t, text="Sign up", bg="plum", font=("Verdana", 14), fg="white", command=lambda: submit_signUp(nom, email, password, confirm_password))
    canvas1.create_window(410, 360, window=register_button)
    button2 = Button(t, text="Home", bg="plum", font=("Verdana", 14), fg="white", command=afficher_home)
    canvas1.create_window(660, 20, anchor="nw", window=button2)

    canvas1.create_rectangle(150, 100, 650, 325, width=2, fill="mistyrose", outline="violet")  #(x1,y1,x2,y2)

def logIn():
    canvas1.delete("all")
    canvas1.create_image(0, 0, image=bg2, anchor="nw")
    canvas1.create_image(0,0, image=icon, anchor="nw")
   
    label = Label(t, text="Log In",bg="mistyrose",font=("Verdana", 18, "bold"))
    canvas1.create_window(380, 100, window=label)


    label = Label(t, text="Email :",bg="mistyrose",font=("Verdana", 14))
    canvas1.create_window(250, 150, window=label)

    email = Entry(t, font=("Helvetica", 14))
    canvas1.create_window(450, 150, window=email)
     
    label = Label(t, text="password :",bg="mistyrose",font=("Verdana", 14))
    canvas1.create_window(250, 180, window=label)
    pas = Entry(t, font=("Helvetica", 14),show="*")
    canvas1.create_window(450, 180, window=pas)

    button_submit = Button(t, text="Log In", font=("Verdana", 14), bg="plum", fg="white", command=lambda: submit_logIn(email,pas))
    canvas1.create_window(400, 260, window=button_submit)
    
    button2 = Button(t, text="Home", bg="plum", font=("Verdana", 14), fg="white", command=afficher_home)
    canvas1.create_window(660, 20, anchor="nw", window=button2)
    
    canvas1.create_rectangle(170, 80, 600, 230, width=2, fill="mistyrose", outline="violet")



canvas1 = Canvas(t, width=800, height=700)
canvas1.pack()
bg = PhotoImage(file="disneyyy.png")
bg1= PhotoImage(file="welcomee.png")
bg2=PhotoImage(file="login (2).png")
icon=PhotoImage(file="logoo2.png")
click_btn1= PhotoImage(file='smallWorld1.png')
click_btn2= PhotoImage(file='Fantasy gardenn1.png')
click_btn3= PhotoImage(file='night show.png')
click_btn4= PhotoImage(file='Hyperspace mountain.png')
mickey = PhotoImage(file="mickey.png")
Disney fan 1 = PhotoImage(file="mickey.png")
Disney fan 2 = PhotoImage(file="mickey.png")

users = {"chayma@gmail.com": ["chayma", "chayma@gmail.com", "12345"],}
print(users)

afficher_home()
t.mainloop()

