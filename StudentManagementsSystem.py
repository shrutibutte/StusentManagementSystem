
def addstudent():
    def submitadd():
        id = idval .get()
        name = nameval .get()
        mobile = mobileval .get()
        email = emailval .get()
        address = addressval .get()
        gender = genderval .get()
        dob = dobval .get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (id, name, mobile, email, address, gender, dob, addeddate, addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notificatrions',
                                            'Id {} Name {} Added sucessfully.. and want to clean the form'.format(id,name),parent=addroot)
            if (res == True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')

        except:
            messagebox.showerror('Notifications', 'Id Already Exist try another id...', parent=addroot)
        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        # print(datas)
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)



    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('425x480+270+240')

    addroot.title('student management system')
    addroot.iconbitmap('man.ico')
    addroot.config(bg='cyan')
    addroot.resizable(False,False)

    #--------------------------------------------Add student  label
    idlabel = Label(addroot, text='Enter Id : ', bg='gold2', font=('times',17,'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    Namelabel = Label(addroot, text='Enter Name : ', bg='gold2', font=('times',17,'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    Namelabel.place(x=10, y=70)

    mobilelabel = Label(addroot, text='Enter Mobile : ', bg='gold2', font=('times',17,'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(addroot, text='Enter email : ', bg='gold2', font=('times',17,'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(addroot, text='Enter Address : ', bg='gold2', font=('times',17,'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(addroot, text='Enter Gender : ', bg='gold2', font=('times',17,'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(addroot, text='Enter D.O.B : ', bg='gold2', font=('times', 17, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)

    # ---------------------- add button--------------
    subbutton = Button(addroot, text='Add', font=("times", 18, 'bold'), width=14, bd=6, borderwidth=4, bg='green2',
                          activebackground='blue',activeforeground='white',command=submitadd)
    subbutton.place(x=122, y=420)
#--------------------------- ADD student entry
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    genderval = StringVar()
    dobval=StringVar()

    identry = Entry(addroot,font=('times',15,'bold'),bd=4,textvariable=idval)
    identry.place(x=200,y=10)

    nameentry = Entry(addroot, font=('times', 15, 'bold'), bd=4, textvariable=nameval)
    nameentry.place(x=200, y=70)

    mobileentry = Entry(addroot, font=('times', 15, 'bold'), bd=4, textvariable=mobileval)
    mobileentry.place(x=200, y=130)

    emailentry = Entry(addroot, font=('times', 15, 'bold'), bd=4, textvariable=emailval)
    emailentry.place(x=200, y=190)

    addressentry = Entry(addroot, font=('times', 15, 'bold'), bd=4, textvariable=addressval)
    addressentry.place(x=200, y=250)

    genderentry = Entry(addroot, font=('times', 15, 'bold'), bd=4, textvariable=genderval)
    genderentry.place(x=200, y=310)

    dobentry = Entry(addroot, font=('times', 15, 'bold'), bd=4, textvariable=dobval)
    dobentry.place(x=200, y=370)



    addroot.mainloop()
def updatestudent():
    def updateadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        emai = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update studentdata set name=%s,mobile=%s,emai=%s,address=%s,gender=%s,dob=%s,time=%s,date=%s where id=%s'
        mycursor.execute(strr, (name, mobile, emai, address, gender, dob,time,date, id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified sucessfully...'.format(id), parent=updateroot)
        strr = 'select *from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)



    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('425x580+270+165')

    updateroot.title('student management system')
    updateroot.iconbitmap('man.ico')
    updateroot.config(bg='cyan')
    updateroot.resizable(False, False)

    # --------------------------------------------Add student  label
    idlabel = Label(updateroot, text='Update Id : ', bg='gold2', font=('times', 17, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    Namelabel = Label(updateroot, text='Update Name : ', bg='gold2', font=('times', 17, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    Namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text='Update Mobile : ', bg='gold2', font=('times', 17, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text='Update email : ', bg='gold2', font=('times', 17, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text='Update Address : ', bg='gold2', font=('times', 17, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text='Update Gender : ', bg='gold2', font=('times', 17, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text='Update D.O.B : ', bg='gold2', font=('times', 17, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(updateroot, text='Update date : ', bg='gold2', font=('times', 17, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)

    timelabel = Label(updateroot, text='Update time : ', bg='gold2', font=('times', 17, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    timelabel.place(x=10, y=490)

    # ---------------------- add button--------------
    subbutton = Button(updateroot, text='update', font=("times", 15, 'bold'), width=15, bd=6, borderwidth=4, bg='green2',
                       activebackground='blue', activeforeground='white', command=updateadd)
    subbutton.place(x=120, y=530)
    # --------------------------- ADD student entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval=StringVar()
    timeval=StringVar()

    identry = Entry(updateroot, font=('times', 15, 'bold'), bd=4, textvariable=idval)
    identry.place(x=200, y=10)

    nameentry = Entry(updateroot, font=('times', 15, 'bold'), bd=4, textvariable=nameval)
    nameentry.place(x=200, y=70)

    mobileentry = Entry(updateroot, font=('times', 15, 'bold'), bd=4, textvariable=mobileval)
    mobileentry.place(x=200, y=130)

    emailentry = Entry(updateroot, font=('times', 15, 'bold'), bd=4, textvariable=emailval)
    emailentry.place(x=200, y=190)

    addressentry = Entry(updateroot, font=('times', 15, 'bold'), bd=4, textvariable=addressval)
    addressentry.place(x=200, y=250)

    genderentry = Entry(updateroot, font=('times', 15, 'bold'), bd=4, textvariable=genderval)
    genderentry.place(x=200, y=310)

    dobentry = Entry(updateroot, font=('times', 15, 'bold'), bd=4, textvariable=dobval)
    dobentry.place(x=200, y=370)

    dateentry = Entry(updateroot, font=('times', 15, 'bold'), bd=4, textvariable=dateval)
    dateentry.place(x=200, y=430)

    timeentry = Entry(updateroot, font=('times', 15, 'bold'), bd=4, textvariable=timeval)
    timeentry.place(x=200, y=490)

    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])


    updateroot.mainloop()
def searchstudent():
    def searchadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")

        if(id!=''):
            strr = 'select * from studentdata where id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif (name != ''):
            strr = 'select * from studentdata where name=%s'
            mycursor.execute(strr, (name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif (mobile != ''):
            strr = 'select * from studentdata where mobile=%s'
            mycursor.execute(strr, (mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif (email != ''):
            strr = 'select * from studentdata where email=%s'
            mycursor.execute(strr, (email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif ( address!= ''):
            strr = 'select * from studentdata where address=%s'
            mycursor.execute(strr, (address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif (gender != ''):
            strr = 'select * from studentdata where gender=%s'
            mycursor.execute(strr, (gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif (dob != ''):
            strr = 'select * from studentdata where dob=%s'
            mycursor.execute(strr, (dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif (addeddate != ''):
            strr = 'select * from studentdata where addeddate=%s'
            mycursor.execute(strr, (addeddate))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('425x520+270+220')

    searchroot.title('student management system')
    searchroot.iconbitmap('man.ico')
    searchroot.config(bg='cyan')
    searchroot.resizable(False, False)

    # --------------------------------------------Add student  label
    idlabel = Label(searchroot, text='Enter Id : ', bg='gold2', font=('times', 17, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    Namelabel = Label(searchroot, text='Enter Name : ', bg='gold2', font=('times', 17, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    Namelabel.place(x=10, y=70)

    mobilelabel = Label(searchroot, text='Enter Mobile : ', bg='gold2', font=('times', 17, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(searchroot, text='Enter email : ', bg='gold2', font=('times', 17, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(searchroot, text='Enter Address : ', bg='gold2', font=('times', 17, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(searchroot, text='Enter Gender : ', bg='gold2', font=('times', 17, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(searchroot, text='Enter Date : ', bg='gold2', font=('times', 17, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(searchroot, text='Enter D.O.B: ', bg='gold2', font=('times', 17, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)

    # ---------------------- add button--------------
    subbutton = Button(searchroot, text='search', font=("times", 15, 'bold'), width=15, bd=6, borderwidth=4, bg='green2',
                       activebackground='blue', activeforeground='white', command=searchadd)
    subbutton.place(x=122, y=470)
    # --------------------------- ADD student entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval=StringVar()

    identry = Entry(searchroot, font=('times', 15, 'bold'), bd=4, textvariable=idval)
    identry.place(x=200, y=10)

    nameentry = Entry(searchroot, font=('times', 15, 'bold'), bd=4, textvariable=nameval)
    nameentry.place(x=200, y=70)

    mobileentry = Entry(searchroot, font=('times', 15, 'bold'), bd=4, textvariable=mobileval)
    mobileentry.place(x=200, y=130)

    emailentry = Entry(searchroot, font=('times', 15, 'bold'), bd=4, textvariable=emailval)
    emailentry.place(x=200, y=190)

    addressentry = Entry(searchroot, font=('times', 15, 'bold'), bd=4, textvariable=addressval)
    addressentry.place(x=200, y=250)

    genderentry = Entry(searchroot, font=('times', 15, 'bold'), bd=4, textvariable=genderval)
    genderentry.place(x=200, y=310)

    dobentry = Entry(searchroot, font=('times', 15, 'bold'), bd=4, textvariable=dobval)
    dobentry.place(x=200, y=370)

    dateentry = Entry(searchroot, font=('times', 15, 'bold'), bd=4, textvariable=dateval)
    dateentry.place(x=200, y=430)

    searchroot.mainloop()



def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notification', 'Id {} deleted sucessfully....'.format(pp))
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)

def showstudent():
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)

def exportstudent(df=None):
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[];
    for  i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])

    dd = ['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added date','Added time']
    df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths, index=False)
    messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))
    print(paths)

def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do yoy want to exit?')
    # print(res)
    if(res==True):
        root.destroy()






#------------------------------------Connection of Database-----
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = usertval.get()
        password = passwordval.get()

        try:
            con = pymysql.connect(host=host,user = user,password=password,database="studentmanagementsystem1")
            mycursor = con.cursor()
            messagebox.showinfo(' Notification','Connected to database')
        except:
            messagebox.showerror('Notification','Data is incorrect please try again',parent=dbroot)

        try:
            mycursor = con.cursor()
            strr = 'create database studentmanagementsystem1'
            mycursor.execute(strr)
            # strr = '''create table studentdata(id int, name varchar(50), mobile varchar(50), email varchar(50),
            # adress varchar(100), gender varchar(50),dob varchar(50),time varchar(50),date varchar(50))'''
            mycursor = con.cursor()
            data="CREATE TABLE studentdata(id int, name varchar(50), mobile varchar(50) , emai varchar(50),address varchar(50),gender varchar(50),dob varchar(50), time varchar(50),date varchar(50))"
            mycursor.execute(data)
            strr = 'alter table studentdata modify column id int not null'
            mycursor.execute(strr)

            strr = 'alter table studentdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('notification','database created and now you are connected to the databases...',parent=dbroot)


        except:
            strr = 'Use studentmanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('notification','Now you are connected to the databases...',parent=dbroot)

        dbroot.destroy()



    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('man.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')

    #-------------------------------Connectdb Lables --------------------
    hostlabel = Label(dbroot,text = "Enter host : ",bg='gold2' , font=('times',17,'bold'),relief=GROOVE, borderwidth=4,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot, text="Enter user : ", bg='gold2', font=('times', 17, 'bold'), relief=GROOVE, borderwidth=4,
                    width=13, anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text="Enter password: ", bg='gold2', font=('times', 17, 'bold'), relief=GROOVE, borderwidth=4,width=13, anchor='w')
    passwordlabel.place(x=10, y=130)

    #---------------------------------- Connectdb Entry------------------------------
    hostval = StringVar()
    usertval = StringVar()
    passwordval = StringVar()


    hostentry = Entry(dbroot,font=('times',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot, font=('times', 15, 'bold'), bd=5, textvariable=usertval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('times', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)

    #--------------------- connectdb butttton
    submitbutton = Button(dbroot,text='submit',font=("times",15,'bold'),width=15, bd=6,borderwidth=4, bg='green2',activebackground='skyblue',
                          command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()


#####################################################################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%y")
    clock.config(text='Date :' + date_string + "\n" + "Time : " + time_string)
    clock.after(20, tick)


############################### intro slider   ##########################################
import random

colors = ["red", "pink", "blue", "gray", "red2", "gold2"];


def IntroLavelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2, IntroLavelColorTick)


def IntroLableTick():
    global count, text
    if (count >= len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text + ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(150, IntroLableTick)


#######################################################################################################################

from tkinter import *
from tkinter import Toplevel,messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import mysql.connector
import pandas
from tkinter import filedialog

import time
import time

root = Tk()
root.title('Student Management System')
root.config(bg='skyblue')  # this is for color
root.geometry('1174x700+200+50')  # width and height
root.iconbitmap('man.ico')
root.resizable(False, False)
####################################### Frame #########################################################################
DataEntryFrame = Frame(root, bg="blue", relief=GROOVE, borderwidth=4)
DataEntryFrame.place(x=10, y=80, width=500, height=600)

#------------------------------------------------ frame intro welcome section button
frontlable = Label(DataEntryFrame,text='------------------Welcome------------------',width=40,font=('Helvetica', 20, 'italic bold'),bg='blue')
frontlable.pack(side=TOP,expand=True)

#------------------------------------- 7 button ----------------
addbtn = Button(DataEntryFrame,text='1. Add Student',width=25,font=('Helvetica', 15, 'italic bold'),bd=6,bg='skyblue',activebackground='green2',activeforeground='white',relief=RIDGE,command=addstudent)
addbtn.pack(side=TOP ,expand=True)

searchbtn = Button(DataEntryFrame,text='2. Search Student',width=25,font=('Helvetica', 15, 'italic bold'),bd=6,bg='skyblue',activebackground='green2',activeforeground='white',relief=RIDGE,command=searchstudent)
searchbtn.pack(side=TOP ,expand=True)

deletebtn = Button(DataEntryFrame,text='3. Delete Student',width=25,font=('Helvetica', 15, 'italic bold'),bd=6,bg='skyblue',activebackground='green2',activeforeground='white',relief=RIDGE,command=deletestudent)
deletebtn.pack(side=TOP ,expand=True)

updatebtn = Button(DataEntryFrame,text='4. Update Student',width=25,font=('Helvetica', 15, 'italic bold'),bd=6,bg='skyblue',activebackground='green2',activeforeground='white',relief=RIDGE,command=updatestudent)
updatebtn.pack(side=TOP ,expand=True)

showbtn = Button(DataEntryFrame,text='5. Show All',width=25,font=('Helvetica', 15, 'italic bold'),bd=6,bg='skyblue',activebackground='green2',activeforeground='white',relief=RIDGE,command=showstudent)
showbtn.pack(side=TOP ,expand=True)

exportbtn = Button(DataEntryFrame,text='6. Expect Data',width=25,font=('Helvetica', 15, 'italic bold'),bd=6,bg='skyblue',activebackground='green2',activeforeground='white',relief=RIDGE,command=exportstudent)
exportbtn.pack(side=TOP ,expand=True)

exitbtn = Button(DataEntryFrame,text='7. Exit',width=25,font=('Helvetica', 15, 'italic bold'),bd=6,bg='skyblue',activebackground='green2',activeforeground='white',relief=RIDGE,command=exitstudent)
exitbtn.pack(side=TOP ,expand=True)

ShowDataFrame = Frame(root, bg='skyblue', relief=GROOVE, borderwidth=4)
ShowDataFrame.place(x=550, y=80, width=620, height=600)
#----------------------------------------Show dataframe---------------------------------------

style = ttk.Style()
style.configure('Treeview.Heading',font=('times',16,'bold'),foreground='blue')
style.configure('Treeview.Heading',font=('times',15,'bold'),foreground='blue2',bg='white')

scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)

studenttable = Treeview(ShowDataFrame,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time')
                        ,yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)           # for x view scroll
scroll_y.config(command=studenttable.yview)          # for y view scroll
studenttable.heading('Id', text='Id')
studenttable.heading('Name', text='Name')
studenttable.heading('Mobile No', text='Mobile No')
studenttable.heading('Email', text='Email')
studenttable.heading('Address', text='Address')
studenttable.heading('Gender', text='Gender')
studenttable.heading('D.O.B', text='D.O.B')
studenttable.heading('Added Date', text='Added Date')
studenttable.heading('Added Time', text='Added Time')
studenttable['show'] = 'headings'

studenttable.column('Id',width=170)
studenttable.column('Name',width=200)
studenttable.column('Mobile No',width=170)
studenttable.column('Email',width=170)
studenttable.column('Address',width=170)
studenttable.column('Gender',width=170)
studenttable.column('D.O.B',width=170)
studenttable.column('Added Date',width=170)
studenttable.column('Added Time',width=170)






studenttable.pack(fill=BOTH,expand=1 )

####################################### Slider ########################################################################
ss = 'Welcome to Student Management System'
count = 0;
text = ''
SliderLabel = Label(root, text=ss)
SliderLabel = Label(root, text=ss, font=('Helvetica', 26, 'italic bold'), relief=RIDGE, borderwidth=4, width=35,
                    bg='cyan')
SliderLabel.place(x=170, y=0)
IntroLavelColorTick()
IntroLableTick()
################################################ clock ################################################################
clock = Label(font=('times', 14, ' bold'), relief=RIDGE, borderwidth=4, bg='green2')
clock.place(x=0, y=0)
tick()
########################################################################## ConnectDatabaseButtton  ####################
connectButton = Button(root, text='connect to database', width=18, font=('Helvetica', 15, 'italic bold'), relief=RIDGE,
                        bd=6,borderwidth=4, bg='green2',activebackground='blue',activeforeground='white',command=Connectdb)
# connectButton = Button(root,text='connect to database',width=23,font=('Helvetica', 19, 'italic bold'), bg='green',
# relief=RIDGE, borderwidth=4,bd=6)


connectButton.place(x=930, y=0)

root.mainloop()

# reach till 20 min video 5

#


