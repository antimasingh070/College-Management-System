from tkinter import *
import tkinter
from tkinter import messagebox
import pymysql
import tkinter.font as font

def main_exit():
    main.destroy()


def addstu():
    def st_exit():
        student.destroy()

    def addst():
        db = pymysql.connect("localhost", "root", "1234", "cms")
        cursor = db.cursor()

        stu_id = e1.get()
        stu_first = e2.get()
        stu_last = e3.get()
        stu_dob = e4.get()
        stu_email = e6.get()
        stu_phone = e7.get()
        stu_address = e8.get()
        stu_prev_qual = e9.get()
        stu_doa = e10.get()
        stu_course = e11.get()
        stu_branch = e12.get()
        stu_section = e13.get()

        try:
            q1 = "INSERT INTO cms.student(`stu_id`,`stu_first`,`stu_last`,`stu_dob`,`stu_email`,`stu_phone`,`stu_address`,`stu_prev_qual`,`stu_doa`,`stu_course`,`stu_branch`,`stu_section`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(q1, (stu_id, stu_first, stu_last, stu_dob, stu_email, stu_phone, stu_address, stu_prev_qual, stu_doa, stu_course, stu_branch, stu_section))

            if len(e1.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out enrollment no fields.")
                db.rollback()
            elif len(e2.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out first name fields.")
                db.rollback()
            elif len(e3.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out last name fields.")
                db.rollback()
            elif len(e4.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out dob fields.")
                db.rollback()
            elif len(e6.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out email fields.")
                db.rollback()
            elif len(e7.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out phone fields.")
                db.rollback()
            elif len(e8.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out address fields.")
                db.rollback()
            elif len(e9.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out qualification fields.")
                db.rollback()
            elif len(e10.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out date of admission fields.")
                db.rollback()
            elif len(e11.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out class course fields.")
                db.rollback()
            elif len(e12.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out branch fields.")
                db.rollback()
            elif len(e13.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out section fields.")
                db.rollback()
            else:
                messagebox.showinfo('Congratulation {}'.format(stu_first), "Details added successfully")
                db.commit()
        except:
            messagebox.showerror('Error', 'The enrollment, email, phone no value must be unique. please try again..')
        finally:
            student.destroy()

    student = tkinter.Tk()
    student.title("Add student details")
    student.geometry("950x650")
    student.configure(bg="light goldenrod")
    Label(student, text="Add student details", font=("Arial", 20), bg="light goldenrod").grid(row=0, column=2, pady=10)
    Label(student, text="Enrollment No:", font=("Calibri", 15), bg="light goldenrod").grid(row=1, column=0, pady=10)
    e1 = Entry(student)
    e1.grid(row=1, column=1, pady=10)
    Label(student, text="(The enrollment value must be unique.)", font=("Calibri", 10), bg="light goldenrod").grid(row=2, column=1,
                                                                                                        pady=10)
    Label(student, text="First name:", font=("Calibri", 15), bg="light goldenrod").grid(row=1, column=2, pady=10)
    e2 = Entry(student)
    e2.grid(row=1, column=3, pady=10)
    Label(student, text="Last name:", font=("Calibri", 15), bg="light goldenrod").grid(row=3, column=0, pady=10)
    e3 = Entry(student)
    e3.grid(row=3, column=1, pady=10)
    Label(student, text="DOB:", font=("Calibri", 15), bg="light goldenrod").grid(row=3, column=2, pady=10)
    e4 = Entry(student)
    e4.grid(row=3, column=3, pady=10)
    Label(student, text="Email:", font=("Calibri", 15), bg="light goldenrod").grid(row=4, column=0, pady=10)
    e6 = Entry(student)
    e6.grid(row=4, column=1, pady=10)
    Label(student, text="(The email value must be unique.)", font=("Calibri", 10), bg="light goldenrod").grid(row=5, column=1,
                                                                                                   pady=10)
    Label(student, text="Phone no:", font=("Calibri", 15), bg="light goldenrod").grid(row=4, column=2, pady=10)
    e7 = Entry(student)
    e7.grid(row=4, column=3, pady=10)
    Label(student, text="(The phone no value must be unique.)", font=("Calibri", 10), bg="light goldenrod").grid(row=5, column=3,
                                                                                                      pady=10)
    Label(student, text="Address:", font=("Calibri", 15), bg="light goldenrod").grid(row=6, column=0, pady=10)
    e8 = Entry(student)
    e8.grid(row=6, column=1, pady=10)
    Label(student, text="Previous qualification:", font=("Calibri", 15), bg="light goldenrod").grid(row=6, column=2, pady=10)
    OPTIONS = [
        "12th",
        "Diploma",
        "B.tech",
        "BBA",
        "BCA"

    ]
    e9 = StringVar(student)
    e9.set(OPTIONS[0])

    j = OptionMenu(student, e9, *OPTIONS)
    j.grid(row=6, column=3, pady=10)
    Label(student, text="Date of admission:", font=("Calibri", 15), bg="light goldenrod").grid(row=7, column=0, pady=10)
    e10 = Entry(student)
    e10.grid(row=7, column=1, pady=10)
    Label(student, text="Course:", font=("Calibri", 15), bg="light goldenrod").grid(row=7, column=2, pady=10)
    OPTIONS = [
        "B.tech",
        "MBA",
        "MCA",
        "PGDM"
    ]
    e11 = StringVar(student)
    e11.set(OPTIONS[0])

    w = OptionMenu(student, e11, *OPTIONS)
    w.grid(row=7, column=3, pady=10)
    Label(student, text="Branch:", font=("Calibri", 15), bg="light goldenrod").grid(row=8, column=0, pady=10)
    OPTIONS = [
        "B.Tech Mechanical engineering",
        "B.Tech Computer Engineering",
        "B.Tech Civil Engineering",
        "B.Tech Electronics Engineering",
        "B.Tech Information Technology",
        "MBA in Marketing",
        "MBA in Human Recourse Management (HRM)",
        "MBA in International Business (IB)",
        "MBA in Information Technology (IT)",
        "MBA in Supply Chain Management",
        "PGDM in Marketing Management",
        "PGDM in Human Resource Management",
        "PGDM in Event Management",
        "PGDM in Operations Management",
        "PGDM in International Business",

    ]
    e12 = StringVar(student)
    e12.set(OPTIONS[0])

    g = OptionMenu(student, e12, *OPTIONS)
    g.grid(row=8, column=1, pady=10)
    Label(student, text="Section:", font=("Calibri", 15), bg="light goldenrod").grid(row=8, column=2, pady=10)
    OPTIONS = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L"
    ]
    e13 = StringVar(student)
    e13.set(OPTIONS[0])

    w = OptionMenu(student, e13, *OPTIONS)
    w.grid(row=8, column=3, pady=10)
    Button(student, text="Submit", bg='pale green', activebackground='spring green', command=addst).grid(row=9,
                                                                                                         column=1,
                                                                                                         pady=15)
    Button(student, text="Exit", bg='pale green', activebackground='spring green', command=st_exit).grid(row=9, column=2,
                                                                                                      pady=15)
    student.mainloop()


def addfac():
    def fa_exit():
        faculty.destroy()

    def addfa():
        db = pymysql.connect("localhost", "root", "1234", "cms")
        cursor = db.cursor()

        fac_id = e1.get()
        fac_first = e2.get()
        fac_last = e3.get()
        fac_dob = e4.get()
        fac_email = e5.get()
        fac_phone = e6.get()
        fac_address = e7.get()
        fac_qual = e8.get()
        fac_doj = e9.get()
        fac_class_co = e10.get()
        fac_branch = e11.get()
        fac_section = e12.get()

        try:
            q1 = "INSERT INTO cms.faculty(`fac_id`,`fac_first`,`fac_last`,`fac_dob`,`fac_email`,`fac_phone`,`fac_address`,`fac_qual`,`fac_doj`,`fac_class_co`,`fac_branch`,`fac_section`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(q1, (
                fac_id, fac_first, fac_last, fac_dob, fac_email, fac_phone, fac_address, fac_qual, fac_doj,
                fac_class_co, fac_branch, fac_section))
            if len(e1.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out faculty no fields.")
                db.rollback()
            elif len(e2.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out first name fields.")
                db.rollback()
            elif len(e3.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out last name fields.")
                db.rollback()
            elif len(e4.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out dob fields.")
                db.rollback()
            elif len(e5.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out email fields.")
                db.rollback()
            elif len(e6.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out phone fields.")
                db.rollback()
            elif len(e7.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out addresss fields.")
                db.rollback()
            elif len(e8.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out qualification fields.")
                db.rollback()
            elif len(e9.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out date od joining fields.")
                db.rollback()
            elif len(e10.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out class coordinator fields.")
                db.rollback()
            elif len(e11.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out branch fields.")
                db.rollback()
            elif len(e12.get()) == 0:
                messagebox.showinfo('Error', "You haven't  filled out section fields.")
                db.rollback()
            else:
                messagebox.showinfo('Congratulation {}'.format(fac_first), "Details added successfully")
                db.commit()
        except:
            messagebox.showerror('Error', 'The faculty no, email, phone no value must be unique. please try again..')
        finally:
            faculty.destroy()


    faculty = tkinter.Tk()
    faculty.title("Add faculty details")
    faculty.geometry("880x650")
    faculty.configure(bg="light goldenrod")
    Label(faculty, text="Add faculty details", font=("Calibri", 20), bg="light goldenrod").grid(row=0, column=2, pady=10)
    Label(faculty, text="Faculty No:", font=("Calibri", 15), bg="light goldenrod").grid(row=1, column=0, pady=10)
    e1 = Entry(faculty)
    e1.grid(row=1, column=1, pady=10)
    Label(faculty, text="(The faculty no value must be unique.)", font=("Calibri", 10), bg="light goldenrod").grid(row=2, column=1,
                                                                                                        pady=10)
    Label(faculty, text="First name:", font=("Calibri", 15), bg="light goldenrod").grid(row=1, column=2, pady=10)
    e2 = Entry(faculty)
    e2.grid(row=1, column=3, pady=10)
    Label(faculty, text="Last name:", font=("Calibri", 15), bg="light goldenrod").grid(row=3, column=0, pady=10)
    e3 = Entry(faculty)
    e3.grid(row=3, column=1, pady=10)
    Label(faculty, text="DOB:", font=("Calibri", 15), bg="light goldenrod").grid(row=3, column=2, pady=10)
    e4 = Entry(faculty)
    e4.grid(row=3, column=3, pady=10)
    Label(faculty, text="Email:", font=("Calibri", 15), bg="light goldenrod").grid(row=5, column=0, pady=10)
    e5 = Entry(faculty)
    e5.grid(row=5, column=1, pady=10)
    Label(faculty, text="(The email value must be unique.)", font=("Calibri", 10), bg="light goldenrod").grid(row=6, column=1,
                                                                                                   pady=10)
    Label(faculty, text="Phone no:", font=("Calibri", 15), bg="light goldenrod").grid(row=5, column=2, pady=10)
    e6 = Entry(faculty)
    e6.grid(row=5, column=3, pady=10)
    Label(faculty, text="(The phone no value must be unique.)", font=("Calibri", 10), bg="light goldenrod").grid(row=6, column=3,
                                                                                                      pady=10)
    Label(faculty, text="Address:", font=("Calibri", 15), bg="light goldenrod").grid(row=7, column=0, pady=10)
    e7 = Entry(faculty)
    e7.grid(row=7, column=1, pady=10)
    Label(faculty, text="Qualification:", font=("Calibri", 15), bg="light goldenrod").grid(row=7, column=2, pady=10)
    OPTIONS = [
        "P.hd",
        "M.tech",
        "MBA",
        "MCA"
    ]
    e8 = StringVar(faculty)
    e8.set(OPTIONS[0])

    j = OptionMenu(faculty, e8, *OPTIONS)
    j.grid(row=7, column=3, pady=10)
    Label(faculty, text="Date of joining:", font=("Calibri", 15), bg="light goldenrod").grid(row=8, column=0, pady=10)
    e9 = Entry(faculty)
    e9.grid(row=8, column=1, pady=10)
    Label(faculty, text="Class coordinator:", font=("Calibri", 15), bg="light goldenrod").grid(row=8, column=2, pady=10)
    OPTIONS = [
        "B.tech",
        "MBA",
        "MCA",
        "PGDM"
    ]
    e10 = StringVar(faculty)
    e10.set(OPTIONS[0])

    w = OptionMenu(faculty, e10, *OPTIONS)
    w.grid(row=8, column=3, pady=10)
    Label(faculty, text="Branch:", font=("Calibri", 15), bg="light goldenrod").grid(row=9, column=0, pady=10)
    OPTIONS = [
        "B.Tech Mechanical engineering",
        "B.Tech Computer Engineering",
        "B.Tech Civil Engineering",
        "B.Tech Electronics Engineering",
        "B.Tech Information Technology",
        "MBA in Marketing",
        "MBA in Human Recourse Management (HRM)",
        "MBA in International Business (IB)",
        "MBA in Information Technology (IT)",
        "MBA in Supply Chain Management",
        "PGDM in Marketing Management",
        "PGDM in Human Resource Management",
        "PGDM in Event Management",
        "PGDM in Operations Management",
        "PGDM in International Business",

    ]
    e11 = StringVar(faculty)
    e11.set(OPTIONS[0])
    j = OptionMenu(faculty, e11, *OPTIONS)
    j.grid(row=9, column=1, pady=10)
    Label(faculty, text="Section:", font=("Calibri", 15), bg="light goldenrod").grid(row=9, column=2, pady=10)
    OPTIONS = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L"
    ]
    e12 = StringVar(faculty)
    e12.set(OPTIONS[0])

    w = OptionMenu(faculty, e12, *OPTIONS)
    w.grid(row=9, column=3, pady=10)
    Button(faculty, text="Submit", bg='pale green', activebackground='spring green', command=addfa).grid(row=10,
                                                                                                         column=1,
                                                                                                         pady=15)
    Button(faculty, text="Exit", bg='pale green', activebackground='spring green', command=fa_exit).grid(row=10,
                                                                                                         column=2,
                                                                                                         pady=15)
    faculty.mainloop()


def searchstu():
    def exit():
        detailes.destroy()

    def View():
        root = tkinter.Tk()
        root.title("Details")
        root.configure(bg="azure")
        root.minsize(width=400, height=400)
        root.geometry("1600x1200")


        y = 0.25

        db = pymysql.connect("localhost", "root", "1234", "cms")
        cursor = db.cursor()

        stu_id = e1.get()
        stu_dob = e2.get()

        Label(root, text="%-30s%-20s%-30s%-20s%-40s%-30s%-40s%-20s%-30s%-20s%-30s%-10s" % (
        'Enrollment no', 'First name', 'Last name', 'DOB', 'Email', 'Phone no', 'Address', 'Qualification',
        'DOA', 'Course', 'Branch', 'Section'), bg='lavender', fg='black',font=("Helvetica", 9,'bold')).place(relx=0.07, rely=0.1)
        q1 = "SELECT * FROM cms.student WHERE (`stu_id`)=%s AND (`stu_dob`)=%s"
        try:
            cursor.execute(q1, (stu_id, stu_dob))
            results = cursor.fetchall()
            if len(e1.get()) == 0:
                messagebox.showerror('Error', "You haven't  filled out enrollment no fields.")
                root.destroy()
            elif len(e2.get()) == 0:
                messagebox.showerror('Error', "You haven't  filled out dob fields.")
                root.destroy()
            for i in results:
                Label(root, text="%-30s%-20s%-30s%-20s%-30s%-20s%-30s%-20s%-30s%-20s%-30s%-10s" % (
                i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12]),
                      bg='medium spring green', fg='black',font=("Helvetica", 9)).place(relx=0.07, rely=y)

                y += 0.1
        except:
            messagebox.showerror("Bad Format", "Can't fetch files from database")
        finally:
            detailes.destroy()
        root.mainloop()

    detailes = tkinter.Tk()
    detailes.title("Search Student detaile's")
    detailes.geometry("780x650")
    detailes.configure(bg="light goldenrod")
    Label(detailes, text="Search student detailes", font=("Calibri", 20), bg="light goldenrod").grid(row=0, column=2, pady=10)
    Label(detailes, text="Enrollment No:", font=("Calibri", 15), bg="light goldenrod").grid(row=1, column=0, pady=5)
    e1 = Entry(detailes)
    e1.grid(row=1, column=1, pady=5)
    Label(detailes, text="DOB:", font=("Calibri", 15), bg="light goldenrod").grid(row=1, column=2, pady=10, padx=10)
    e2 = Entry(detailes)
    e2.grid(row=1, column=3, pady=10)
    Button(detailes, text="Submit", bg='pale green', activebackground='spring green', command=View).grid(row=3,
                                                                                                         column=1)
    Button(detailes, text="Exit", bg='pale green', activebackground='spring green', command=exit).grid(row=3, column=2)
    detailes.mainloop()


def searchfac():
    def exit():
        detailes.destroy()

    def View():
        root = tkinter.Tk()
        root.title("Detaile's")
        root.configure(bg="azure")
        root.minsize(width=400, height=400)
        root.geometry("1600x1200")

        y = 0.25

        db = pymysql.connect("localhost", "root", "1234", "cms")
        cursor = db.cursor()

        fac_id = e1.get()
        fac_dob = e2.get()

        Label(root, text="%-30s%-20s%-30s%-20s%-40s%-30s%-40s%-20s%-30s%-30s%-30s%-10s" % (
        'Faculty no', 'First name', 'Last name', 'DOB', 'Email', 'Phone no', 'Address', 'Qualification',
        'DOJ', 'Class Coordinator', 'Branch', 'Section'), bg='lavender', fg='black',font=("Helvetica", 9,'bold')).place(relx=0.07, rely=0.1)
        q1 = "SELECT * FROM cms.faculty WHERE (`fac_id`)=%s AND (`fac_dob`)=%s"
        try:
            cursor.execute(q1, (fac_id, fac_dob))
            results = cursor.fetchall()
            if len(e1.get()) == 0:
                messagebox.showerror('Error', "You haven't  filled out faculty no fields.")
                root.destroy()
            elif len(e2.get()) == 0:
                messagebox.showerror('Error', "You haven't  filled out dob fields.")
                root.destroy()
            for i in results:
                Label(root, text="%-30s%-20s%-30s%-20s%-30s%-20s%-30s%-20s%-30s%-30s%-30s%-10s" % (
                i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12]),
                      bg='medium spring green', fg='black',font=("Helvetica", 9)).place(relx=0.07, rely=y)

                y += 0.1
        except:
            messagebox.showerror("Bad Format", "Can't fetch files from database")
        finally:
            detailes.destroy()

        root.mainloop()

    detailes = tkinter.Tk()
    detailes.title("Search Faculty detail's")
    detailes.geometry("780x650")
    detailes.configure(bg="light goldenrod")
    Label(detailes, text="Search faculty detailes", font=("Calibri", 20), bg="light goldenrod").grid(row=0, column=2, pady=10)
    Label(detailes, text="Faculty No:", font=("Calibri", 15), bg="light goldenrod").grid(row=1, column=0, pady=5)
    e1 = Entry(detailes)
    e1.grid(row=1, column=1, pady=5)
    Label(detailes, text="DOB:", font=("Calibri", 15), bg="light goldenrod").grid(row=1, column=2, pady=10, padx=10)
    e2 = Entry(detailes)
    e2.grid(row=1, column=3, pady=10)
    Button(detailes, text="Submit", bg='pale green', activebackground='spring green', command=View).grid(row=3,
                                                                                                         column=1)

    Button(detailes, text="Exit", bg='pale green', activebackground='spring green', command=exit).grid(row=3, column=2)
    detailes.mainloop()


main = tkinter.Tk()
main.geometry("1600x1200")
main.title("Collage Management System")
main.configure(bg="light cyan")
l1 = Label(main, text="COLLEGE MANAGEMENT SYSTEM", font=('Time', '30'), fg='gray32', bg='light cyan').pack(padx=30, pady=10)
Label(main, text="IEC College of Enginnering and Technology", font=('Time', '15'), bg='light cyan').pack()
Label(main,
      text="--------------------------------------------------------------------------------------------------------------",
      font=('Time', '10'), bg='light cyan').pack()
myFont = font.Font(family='Helvetica', size=12, weight='bold')
b1 = Button(main, text="Add Student", width="35", height="5",font=myFont, bg='steel blue', activebackground='spring green',
            command=addstu).pack(padx=30, pady=10)
b2 = Button(main, text="Add Faculty", width="35", height="5",font=myFont, bg='steel blue', activebackground='spring green',
            command=addfac).pack(padx=30, pady=10)
b3 = Button(main, text="Student details", width="35", height="5",font=myFont, bg='steel blue', activebackground='spring green',
            command=searchstu).pack(padx=30, pady=10)
b4 = Button(main, text="Faculty Details", width="35", height="5",font=myFont, bg='steel blue', activebackground='spring green',
            command=searchfac).pack(padx=30, pady=10)
b5 = Button(main, text="Exit", width="35", height="2",font=myFont, bg='steel blue', activebackground='spring green',
            command=main_exit).pack(padx=30, pady=10)
main.mainloop()