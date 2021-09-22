

from tkinter import *
import tkinter
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
import tkinter.font as font


def exit3():
    cms.destroy()


def register():
    def click1():
        db = pymysql.connect("localhost", "root", "1234", "cms")
        cursor = db.cursor()

        user_name = e1.get()
        user_email = e2.get()
        user_id = e3.get()
        user_password = e4.get()
        user_cof_password = e5.get()

        try:
            q1 = "INSERT INTO cms.user(`user_name`,`user_email`,`user_id`,`user_password`,`user_cof_password`) VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(q1, (user_name, user_email, user_id, user_password, user_cof_password))

            if e4.get() != e5.get():
                messagebox.showwarning('Registration error', 'Password did not match: Please try again...                                           ')
                db.close()
            elif len(e1.get()) == 0:
                messagebox.showwarning('Registration error', "You haven't  filled out name fields: Please try again...                             ")
                db.close()
            elif len(e2.get()) == 0:
                messagebox.showwarning('Registration error', "You haven't  filled out email fields: Please try again...                            ")
                db.close()
            elif len(e3.get()) == 0:
                messagebox.showwarning('Registration error',"You haven't  filled out username fields: Please try again...                          ")
                db.close()
            elif len(e4.get()) and len(e5.get()) == 0:
                messagebox.showwarning('Registration error', "You haven't  filled out password  fields: Please try again...")
                db.close()
            else:
                messagebox.showinfo('Congratulation {}'.format(user_name), 'You have been successfully registered                                  ')
                db.commit()
        except:
            messagebox.showerror('Error', 'The username and email value must be unique. please try again..                                 ')
        finally:
            register.destroy()

    register = tkinter.Tk()
    register.title("Register")
    register.geometry("470x450")
    register.configure(bg="salmon")
    Label(register, text="Register", font=('Time', '20'), fg='gray32', bg='salmon').grid(row=0, column=1, pady=15,
                                                                                       sticky=W)
    Label(register, text="Name:", font=('Time', '15'), bg='salmon').grid(row=2, column=0)
    e1 = Entry(register)
    e1.grid(row=2, column=1)
    Label(register, text="Email:", font=('Time', '15'), bg='salmon').grid(row=3, column=0)
    e2 = Entry(register)
    e2.grid(row=3, column=1)
    Label(register, text="(Email must be unique)", font=('Time', '10'), bg='salmon').grid(row=3, column=2)
    Label(register, text="Username:", font=('Time', '15'), bg='salmon').grid(row=4, column=0)
    e3 = Entry(register)
    e3.grid(row=4, column=1)
    Label(register, text="(Username must be unique)", font=('Time', '10'), bg='salmon').grid(row=4, column=2)
    Label(register, text="Password:", font=('Time', '15'), bg='salmon').grid(row=5, column=0)
    e4 = Entry(register, show="*")
    e4.grid(row=5, column=1)
    Label(register, text="Confirm Password:", font=('Time', '15'), bg='salmon').grid(row=6, column=0)
    e5 = Entry(register, show="*")
    e5.grid(row=6, column=1)
    Button(register, text="Submit", bg='steel blue', activebackground='spring green', command=click1).grid(row=7,
                                                                                                           column=1)
    register.mainloop()


def login():
    def click2():
        db = pymysql.connect("localhost", "root", "1234", "cms")
        cursor = db.cursor()

        user_id = e1.get()
        user_password = e2.get()

        try:
            q1 = "SELECT * FROM cms.user WHERE (`user_id`)=%s AND (`user_password`)=%s"
            cursor.execute(q1, (user_id, user_password))
            results = cursor.fetchall()
            if len(e1.get()) == 0:
                messagebox.showerror('Login error', "You haven't  filled out username fields: Please try again...")
                login.destroy()
            elif len(e2.get()) == 0:
                messagebox.showerror('Login error', "You haven't  filled out password fields: Please try again...")
                login.destroy()

            for j in results:
                if j[3] != e1.get() and j[4] == e2.get():
                    messagebox.showwarning('Login error','You have entered incorrect username. Please try again...')
                    login.destroy()

            for i in results:
                if i[3] == e1.get() and i[4] == e2.get():
                    messagebox.showinfo("Login successfully", "Welcome {} You have been successfully login".format(user_id))
                    cms.destroy()
                    login.destroy()
                    from project import main

        except:
            pass
    login = tkinter.Tk()
    login.geometry("450x450")
    login.title("Login")
    login.configure(bg="salmon")
    Label(login, text="Login", font=('Time', '20'), fg='gray32', bg='salmon').grid(row=0, column=1, pady=10)
    Label(login, text="Enter Username:", font=('Time', '15'), bg='salmon').grid(row=1, column=0)
    e1 = Entry(login)
    e1.grid(row=1, column=1)
    Label(login, text="Enter Password:", font=('Time', '15'), bg='salmon').grid(row=2, column=0)
    e2 = Entry(login, show="*")
    e2.grid(row=2, column=1)
    Button(login, text="Submit", bg='steel blue',  activebackground='spring green', command=click2).grid(row=3, column=1)
    login.mainloop()


cms = tkinter.Tk()
cms.geometry("1920x1080")
cms.title("Collage Management System")
cms.configure(bg="light cyan")
l1 = Label(cms, text="COLLEGE MANAGEMENT SYSTEM", font=('Time', '30'), fg='gray32', bg='light cyan').pack()
img = ImageTk.PhotoImage(Image.open("static/iec.png"))
panel = tkinter.Label(cms, image=img, bg='light cyan')
panel.pack(side="top", pady=4)
Label(cms, text="IEC College of Engineering and Technology", font=('Time', '15'), bg='light cyan').pack()
Label(cms, text="Plot No. 4, Knowledge Park I, G. Noida \nDistt. Gautam Budh Nagar, U.P. \nIndia - 2013010",
      font=('Time', '10'), bg='light cyan').pack()
myFont = font.Font(family='Helvetica', size=12, weight='bold')
b1 = Button(cms, text="Register", width="35", height="5",font=myFont, bg='steel blue', activebackground='spring green',
            command=register).pack(padx=30, pady=15)
b2 = Button(cms, text="Login", width="35", height="5",font=myFont, bg='steel blue', activebackground='spring green',
            command=login).pack(padx=30, pady=15)
b3 = Button(cms, text="Exit", width="35", height="2",font=myFont, bg='steel blue', activebackground='spring green',
            command=exit3).pack(padx=30, pady=15)
cms.mainloop()