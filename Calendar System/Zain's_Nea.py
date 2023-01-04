from tkinter import *
from tkcalendar import *
import plotly.express as px
from sqlalchemy import create_engine
import pandas as pd
import sqlite3
from tkinter import ttk
import datetime
from datetime import time, timedelta

Yellow ="#F7F7F7"
White = "#EDD170"
root = Tk()
root.withdraw()
class Images():
    def __init__(self,Window):
        Window.geometry("1150x700")
        Window.iconbitmap("Logo.ico")
        Window.title("BeTheCase")
        Window.resizable(0,0)
    def Templates(self):
        self.SignIn =  PhotoImage(file = "SignIn.png")
        self.Picture1W = PhotoImage(file = "Picture1W.png")
        self.SignUpB = PhotoImage(file = "SignUp.png")
        self.MainImage = PhotoImage(file = "MainPage.png")
        self.LogOutB = PhotoImage(file = "LogOutB.png")
        self.MyCalendarB = PhotoImage(file = "MyCalendarB.png") #templates
        self.CompareB = PhotoImage(file = "CompareB.png")
        self.ContactsB = PhotoImage(file = "ContactsB.png")
        self.SettingsB = PhotoImage(file = "SettingsB.png")
        self.MyCalendar_P = PhotoImage(file = "MyCalendar.png")
        self.UpdateB = PhotoImage(file = "Update.png")
        self.ViewB = PhotoImage(file = "View.png")
        self.VMWDB = PhotoImage(file = "VMWD.png")
        self.SearchB = PhotoImage(file = "Search.png")
        self.BackB = PhotoImage(file = "Back.png")
        self.RemoveB = PhotoImage(file = "Remove.png")
        self.Compare_P = PhotoImage(file = "Compare.png")
        self.ThisOneB = PhotoImage(file = "ThisOne.png")
        self.AddB = PhotoImage(file = "Add.png")
        self.AddContactB = PhotoImage(file = "AddContact.png")
        self.Contacts_P = PhotoImage(file = "Contacts.png")
        self.AddContact_W = PhotoImage(file = "Contacts-Add.png")
    def DataBase(self):
        disk_engine = create_engine('sqlite:///NEA_Z.db')
        conn = sqlite3.connect('NEA_Z.db')
        c = conn.cursor()
        conn.execute('''CREATE TABLE IF NOT EXISTS User_Details (   
                    "UserID" INTEGER,                           
                    "First_Name" TEXT,
                    "Last_Name" TEXT,
                    "Password" TEXT,
                    "Phone Number" TEXT,
                    "Email" TEXT,
                    PRIMARY KEY("UserID" AUTOINCREMENT)
                    )''')
        conn.execute('''CREATE TABLE IF NOT EXISTS Dates_Details (
                    "UserID" INTEGER,
                    "start_event" TEXT,
                    "end_event" TEXT,
                    "name" TEXT,
                    "event_date" TEXT,
                    FOREIGN KEY("UserID") REFERENCES "User_Details"("UserID")
                    )''')                                                           
        conn.execute('''CREATE TABLE IF NOT EXISTS Notes ( 
                    "UserID" INTEGER,              
                    "Notes" TEXT,
                    FOREIGN KEY("UserID") REFERENCES "User_Details"("UserID")
                    )''')
        conn.execute('''CREATE TABLE IF NOT EXISTS Contacts ( 
                    "UserID" INTEGER,              
                    "Email" TEXT,
                    FOREIGN KEY("UserID") REFERENCES "User_Details"("UserID")
                    )''')                                        
                    
        conn.commit()
        conn.close()
class Login_SignUp(Images):
    def __init__(self):
        self.Page1 = Toplevel()
        super().__init__(self.Page1)
        super().Templates()
        self.EmailE = StringVar()
        self.PasswordE = StringVar()
    def MainW(self):
        Label(self.Page1, image = self.Picture1W).place(x=0,y=0, relheight=1, relwidth=1)
        Entry(self.Page1, textvariable=self.EmailE, font = "Calibri 18 bold", bd = 0).place(x=360,y=228, width = 380)
        Entry(self.Page1, textvariable=self.PasswordE, font = "Calibri 18 bold", bd = 0).place(x=360,y=330, width = 380)
        Button(self.Page1,image = self.SignIn,bd= 0, bg = "#D9D6DD", activebackground="#D9D6DD" ,command = self.Login).place(x=649,y=416)
        Button(self.Page1,image = self.SignUpB, bd= 0, bg = "#D9D6DD", activebackground="#D9D6DD", command = self.Selection).place(x=468, y= 598)
    def Login(self):
        self.Email = self.EmailE.get()
        self.Password = self.PasswordE.get()
        conn = sqlite3.connect("NEA_Z.db")
        self.result = conn.execute('SELECT UserID FROM User_Details WHERE Email="%s" and Password="%s"'%(self.Email,self.Password))
        self.ID = self.result.fetchone()
        if self.ID:
            self.ID, = self.ID
            self.Page1.destroy()
            Main().InterfacePage(self.ID)
        else:
            Label(self.Page1, text = "Incorrect Email or Password",font = "Calibri 16 bold", bg="#FDF1BD").place(x=12, y = 12)
    def Selection(self):
        Window_S = Toplevel()
        Button(Window_S, text= "Commerical").pack()
        Button(Window_S, text= "Public").pack()
class Main(Login_SignUp):
    def __init__(self):
        self.Main = Toplevel()
        super(Login_SignUp,self).__init__(self.Main)
        super(Login_SignUp,self).Templates()
        self.cal = StringVar()
        self.dropchoice = StringVar()
        self.name1 = StringVar()
        self.name2 = StringVar()
        self.name3 = StringVar()
        self.name4 = StringVar()
        self.name5 = StringVar()
        self.start = StringVar()
        self.end = StringVar()
        self.my_list = StringVar()
    def InterfacePage(self,ID):
        self.UniqueID = ID
        Label(self.Main, image = self.MainImage).place(x=0,y=0, relwidth = 1, relheight = 1) #placing the template on the window
        s=ttk.Style()
        s.theme_use("clam") # gives the calendar design a modern look
        cal = Calendar(self.Main,
                font="Arial 35", #Changes font size
                textvariable = self.cal, # attaches the variable "cal" to the outcome of the calendar(aka the date selected)
                selectmode="day", #calendar format is days
                showweeknumbers = False, #disables the side bar of the week number
                firstweekday="monday", # each calendar page starts with monday
                background=Yellow, #makes the background yellow
                foreground=White,  # makes the writing white
                bordercolor= Yellow, # makes the border yellow
                othermonthweforeground = White,
                othermonthwebackground = Yellow,
                selectbackground = White,
                selectforeground = Yellow,
                normalbackground=Yellow,
                weekendbackground=Yellow,
                weekendforeground = White,
                headersbackground =Yellow,
                headersforeground = White,
                normalforeground=White,
                othermonthforeground = White,
                othermonthbackground = Yellow,
                date_pattern="d/m/yyyy")
        self.Markers(cal)
        Button(self.Main, image = self.LogOutB, bd= 0, bg = "#F7F7F7", activebackground= "#F7F7F7", command = lambda:[self.Main.destroy(),self.Transfer()]).place(x=22 ,y=0)
        Button(self.Main, image = self.MyCalendarB, bd = 0,  bg = "#F7F7F7", activebackground= "#F7F7F7",command = lambda:[self.Main.destroy(),self.MyCalendar()] ).place(x=54 ,y=131)
        Button(self.Main, image = self.CompareB, bd = 0,  bg = "#F7F7F7", activebackground= "#F7F7F7", command = lambda:[self.Main.destroy(),self.Compare()]).place(x=54 ,y=274)
        Button(self.Main, image = self.ContactsB, bd = 0,  bg = "#F7F7F7", activebackground= "#F7F7F7", command  = lambda:[self.Main.destroy(),self.Contacts()]).place(x=54 ,y=417)
        Button(self.Main, image = self.SettingsB,bd = 0,  bg = "#F7F7F7", activebackground= "#F7F7F7").place(x=54 ,y=560)
    def Transfer(self):
        Login_SignUp.MainW()
    def Compare(self):
        self.COMP = Toplevel()
        super(Login_SignUp,self).__init__(self.COMP)
        Label(self.COMP, image = self.Compare_P).place(x=0,y=0, relheight=1, relwidth=1)
        Button(self.COMP, image =self.BackB, bd= 0, bg = "#F7F7F7", activebackground= "#F7F7F7", command = lambda:[self.COMP.destroy(),self.backToMain()]).place(x=22,y=21)
        self.conn = sqlite3.connect("NEA_Z.db")
        self.cur = self.conn.cursor()
        self.contacts =self.cur.execute('''SELECT User_Details.Email
                                           FROM User_Details,Contacts
                                           WHERE (User_Details.UserID = Contacts.FriendID) AND Contacts.UserID = "%s"'''%(self.UniqueID))
        self.contacts = self.contacts.fetchall()
        self.caldrop = DateEntry(self.COMP,
                font="Arial 15",
                textvariable = self.cal,
                selectmode="day",
                showweeknumbers = False,
                firstweekday="monday",
                background=Yellow, #doesnt mean anything,
                foreground=White, # heading writing,
                bordercolor= Yellow,
                othermonthweforeground = White,
                othermonthwebackground = Yellow,
                selectbackground = White,
                selectforeground = Yellow,
                normalbackground=Yellow,
                weekendbackground=Yellow,
                weekendforeground = White,
                headersbackground =Yellow,
                headersforeground = White,
                normalforeground=White,
                othermonthforeground = White,
                othermonthbackground = Yellow,
                date_pattern="d/m/yyyy")
        self.caldrop.place(x= 445,y=158)
        self.contacts = [r for r, in self.contacts]
        OptionMenu(self.COMP,self.name1,*self.contacts).place(x=39, y= 280)
        OptionMenu(self.COMP,self.name2,*self.contacts).place(x=263, y= 280)
        OptionMenu(self.COMP,self.name3,*self.contacts).place(x=498, y= 280)
        OptionMenu(self.COMP,self.name4,*self.contacts).place(x=726, y=280)
        OptionMenu(self.COMP,self.name5,*self.contacts).place(x=948, y= 280)
        Button(self.COMP,image = self.ThisOneB,bd = 0, bg = "#F7F7F7", activebackground= "#F7F7F7",command = lambda:[self.CompareDates(self.name1.get(),self.name2.get(),self.name3.get(),self.name4.get(),self.name5.get(),"name",self.cal.get())]).place(x=210,y=625)
        Button(self.COMP,image = self.ThisOneB,bd = 0, bg = "#F7F7F7", activebackground= "#F7F7F7",command = lambda:[self.CompareDates(self.name1.get(),self.name2.get(),self.name3.get(),self.name4.get(),self.name5.get(),"event_date",self.cal.get())]).place(x=743, y=625)  
    def CompareDates(self,name1,name2,name3,name4,name5,option,SelectedDate):
        self.contactIDs = self.cur.execute('''SELECT UserID
                                              FROM User_Details
                                              WHERE Email = "%s" OR Email = "%s" OR Email = "%s" OR Email = "%s" OR Email = "%s"'''%(name1,name2,name3,name4,name5))
        self.contactsIDs = self.contactIDs.fetchall()
        self.contactsIDs = [r for r, in self.contactsIDs]
        self.contactsIDs.append("")
        self.contactsIDs.append("")
        self.contactsIDs.append("")
        self.contactsIDs.append("")
        self.contactsIDs.append("")
        self.FreeSpaces(self.contactsIDs[0],self.contactsIDs[1],self.contactsIDs[2],self.contactsIDs[3],self.contactsIDs[4],SelectedDate)
        conn = sqlite3.connect('NEA_Z.db')
        self.df = pd.read_sql_query('SELECT * '
                            'FROM Dates_Details '                                # searching for the names and the selected date in the datebase and pulling the Start_event,end_event,event_date and name
                            'WHERE ((UserID  = "%s" OR UserID = "%s"OR UserID = "%s"OR UserID = "%s"OR UserID = "%s"OR UserID = "%s") AND (event_date = "%s") OR (Name = "Available Space")); '%(self.UniqueID,self.contactsIDs[0],self.contactsIDs[1],self.contactsIDs[2],self.contactsIDs[3],self.contactsIDs[4],SelectedDate), conn)
        self.df = pd.DataFrame(self.df)
        self.df["start_event"] = pd.to_datetime(self.df["start_event"])
        self.df["start_event"] = self.df["start_event"].apply(lambda x: x.replace(year=1970, month=1, day=1)) #setting the axis for start_event
        self.df["end_event"] = pd.to_datetime(self.df["end_event"])
        self.df["end_event"] = self.df["end_event"].apply(lambda x: x.replace(year=1970, month=1, day=1)) #setting the axis for end_event
        self.fig = px.timeline(self.df, x_start="start_event", x_end="end_event", y=option,color="name",title= SelectedDate) # setting the format of the graph
        self.fig.update_xaxes(
            tickformat="%H:%M",#converts the format from years to minutes and hours
            tickformatstops=[
                dict(dtickrange=[3600000, 86400000], value="%H:%M")]  # setting the range
        )
        self.df = pd.DataFrame(self.df)
        self.fig.show()
        self.DeleteFreeSpaces()
    def DeleteFreeSpaces(self):
        self.conn = sqlite3.connect('NEA_Z.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''DELETE FROM Dates_Details WHERE name = "Available Space"''')
        self.conn.commit()

    def FreeSpaces(self,name1,name2,name3,name4,name5,SelectedDate):
        conn = sqlite3.connect('NEA_Z.db')
        cur = conn.cursor()
        data = cur.execute('''SELECT start_event, end_event
                              FROM Dates_Details
                              WHERE (UserID  = "%s" OR UserID = "%s"OR UserID = "%s"OR UserID = "%s"OR UserID = "%s" OR UserID = "%s") AND (event_date = "%s")
                              ORDER BY start_event'''%(self.UniqueID, name1,name2,name3,name4,name5,SelectedDate))
        data =data.fetchall()
        data.insert(0,("00:00","00:00"))
        data.append(("23:59","23:59"))
        for i in range (0,len(data)-1):
            start = "00:00"
            end  = "23:59"
            distance = 5
            if i == 0:
                start_time = datetime.datetime.strptime(start,"%H:%M")
                end_time =  datetime.datetime.strptime(data[i+1][0], "%H:%M") - timedelta(minutes = distance)

            elif i == len(data)-2:
                start_time = datetime.datetime.strptime(data[i][1], "%H:%M") + timedelta(minutes = distance)
                end_time = datetime.datetime.strptime(end,"%H:%M")


            else:
                start_time = datetime.datetime.strptime(data[i][1], "%H:%M") + timedelta(minutes = distance)
                end_time = datetime.datetime.strptime(data[i+1][0], "%H:%M") - timedelta(minutes = distance)

            difference = str(end_time-start_time)
            start_time = str(start_time)
            end_time = str(end_time)
            start_time = start_time.replace('1900-01-01 ','')
            end_time = end_time.replace('1900-01-01 ','')
            start_time = start_time[:-3]
            end_time = end_time[:-3]
            if not("-" in difference):
                cur.execute('''INSERT INTO Dates_Details(start_event,end_event,name,event_date)
                               VALUES("%s","%s","Available Space","%s")'''%(start_time,end_time,SelectedDate))
                conn.commit()


    def Markers(self,cal):
        conn = sqlite3.connect('NEA_Z.db')
        cur  = conn.cursor()
        data= cur.execute('''SELECT event_date, Description
                       FROM Dates_Details
                       WHERE UserID = "%s"'''%(self.UniqueID))
        data = data.fetchall()
        for i in data:
            d = datetime.datetime.strptime(i[0], '%d/%m/%Y')
            cal.calevent_create(d,i[1],"event")
            cal.tag_config("event",background = Yellow, foreground = "black")
        cal.place(x=354,y=144)
        
                        
    def MyCalendar(self):
        self.MC = Toplevel()
        super(Login_SignUp,self).__init__(self.MC)
        Label(self.MC, image = self.MyCalendar_P).place(x=0,y=0, relheight=1, relwidth=1)
        Button(self.MC, image =self.BackB, bd= 0, bg = "#F7F7F7", activebackground= "#F7F7F7", command = lambda:[self.MC.destroy(),self.backToMain()]).place(x=22,y=21)
        Button(self.MC,  image = self.SearchB, bd= 0, bg = "#F7F7F7", activebackground= "#F7F7F7", command =lambda:[self.Times(self.cal.get(),self.dropchoice)]).place(x=321,y=21)
        Button(self.MC, image= self.VMWDB, bd= 0, bg = "#F7F7F7", activebackground= "#F7F7F7", command = lambda:[self.View_Day(self.cal.get())]).place(x=52,y=141)
        Button(self.MC, image= self.RemoveB, bd= 0, bg = "#F7F7F7", activebackground= "#F7F7F7", command = lambda:[self.confirm(self.cal.get(),self.dropchoice.get())]).place(x=52,y=258)
        self.caldrop = DateEntry(self.MC,
                font="Arial 15",
                textvariable = self.cal,
                selectmode="day",
                showweeknumbers = False,
                firstweekday="monday",
                background=Yellow, #doesnt mean anything,
                foreground=White, # heading writing,
                bordercolor= Yellow,
                othermonthweforeground = White,
                othermonthwebackground = Yellow,
                selectbackground = White,
                selectforeground = Yellow,
                normalbackground=Yellow,
                weekendbackground=Yellow,
                weekendforeground = White,
                headersbackground =Yellow,
                headersforeground = White,
                normalforeground=White,
                othermonthforeground = White,
                othermonthbackground = Yellow,
                date_pattern="d/m/yyyy")
        self.caldrop.place(x= 149,y=33)
        
    def backToMain(self):
        self.back = Main()
        self.back.InterfacePage(self.UniqueID)
    def Times(self, cal,choice):
        conn = sqlite3.connect("NEA_Z.db")
        self.cur = conn.cursor()
        self.list = self.cur.execute('''SELECT start_event
                            FROM Dates_Details
                            WHERE UserID = "%s" and event_date = "%s"
                            ORDER BY start_event'''%(self.UniqueID, cal))
        self.list = self.list.fetchall()
        self.list = [r for r, in self.list]
        self.list.insert(0, "Add New Date")
        self.list.insert(1, "Add New Date")
        self.choice = ttk.OptionMenu(self.MC,self.dropchoice,*self.list)
        self.choice.place(x=431,y=33)
        Button(self.MC, image = self.ViewB, bd= 0, bg = "#F7F7F7", activebackground= "#F7F7F7", command =lambda:[self.search(cal,self.dropchoice.get(),self.UniqueID)]).place(x=558, y=21)
    def confirm(self,cal,choice):
        self.CON = Toplevel()
        Label(self.CON, text ="Are you sure you want to remove all data from " + cal + "\n" + choice ).pack()
        Button(self.CON, text = "Yes", command = lambda:[self.CON.destroy(),self.RemoveData(self.UniqueID,cal,choice)]).pack()
        Button(self.CON, text = "No", command = self.CON.destroy).pack()
    def RemoveData(self,ID,cal,choice):
        self.conn = sqlite3.connect("NEA_Z.db")
        self.cur = self.conn.cursor()
        self.cur.execute('''DELETE FROM Dates_Details WHERE UserID = "%s" and event_date = "%s" and start_event = "%s"'''%(ID,cal,choice))
        self.conn.commit()
        self.CON.destroy()
        self.MC.destroy()
        self.MyCalendar()
    def search(self,cal,choice,ID):
        self.conn = sqlite3.connect("NEA_Z.db")
        self.cur = self.conn.cursor()
        self.data = self.cur.execute('''SELECT start_event, end_event,Description
                                        FROM Dates_Details 
                                        WHERE UserID = "%s" and event_date = "%s" and start_event = "%s"'''%(ID,cal,choice))
        self.data = self.data.fetchone()
        self.holder = ["","","",""]
        self.description = Text(self.MC, width = 105, font = "Arial 10", height = 20)
        start = Entry(self.MC, textvariable = self.start)
        start.delete(0, END)
        start.place(x=219,y=559)
        end=Entry(self.MC, textvariable = self.end)
        end.delete(0, END)
        end.place(x=783,y=559)
        if self.data != None:
            Button()
            self.description.insert(INSERT, self.data[2])
            Button(self.MC, image= self.UpdateB, bd= 0, bg = "#F7F7F7", activebackground= "#F7F7F7", command = lambda:[self.UpdateDB(self.start.get(),self.end.get(),self.description.get(1.0, END),cal,self.data[0],self.data[1])]).place(x=52,y=375)
            print(self.data[0])
            start.insert(0,self.data[0])
            end.insert(0,self.data[1])
        else:
            Button(self.MC, image= self.AddB, bd= 0, bg = "#F7F7F7", activebackground= "#F7F7F7", command = lambda:[self.AddToDB(self.start.get(),self.end.get(),self.description.get(1.0, END),cal)]).place(x=52,y=375)
            self.description = Text(self.MC, width = 105, font = "Arial 10", height = 20)
            self.description.place(x=367, y=130)
        Entry(self.MC, textvariable = self.start).place(x=219,y=559)
        Entry(self.MC, textvariable = self.end).place(x=783,y=559)
        self.description.place(x=367, y=135)
    def AddToDB(self,start,end,des,cal):
        print(start,end,des)
        self.conn = sqlite3.connect("NEA_Z.db")
        self.cur = self.conn.cursor()
        self.data = self.cur.execute('''SELECT start_event, end_event
                                        FROM Dates_Details 
                                        WHERE UserID = "%s" and event_date = "%s"
                                        ORDER BY start_event'''%(self.UniqueID,cal))
        self.data = self.data.fetchall()
        print(self.data)
        self.data.insert(0,("00:00","00:00"))
        self.data.append(("24:00","24:00"))
        if (self.date_verification(start) == True and self.date_verification(end) == True) and start < end:
            print("hello1")
            for i in range (0,len(self.data)):
                print("hello3")
                if (start > self.data[i][1] and end < self.data[i+1][0]): # this algorithm will be visualised in the report
                    print("hello4")
                    self.cur.execute('''INSERT INTO Dates_Details (UserID,start_event,end_event,event_date,Description)
                                        VALUES("%s","%s","%s","%s","%s")'''%(self.UniqueID,start,end,cal,des))
                    self.conn.commit()
                    self.MC.destroy()
                    self.MyCalendar()
                    break
                else:
                    if i ==(len(self.data)-1):
                        errormsg = Toplevel()
                        Label(errormsg, text= "The times you have entered arent available, review your schedule to see whats occupying that time slot").pack()
                        Button(errormsg, text= "confirm", command = errormsg.destroy).pack()
        else:
            errormsg = Toplevel()
            Label(errormsg, text= "invalid input(s)!").pack()
            Button(errormsg, text= "confirm", command = errormsg.destroy)
    def UpdateDB(self,start,end,des,cal,old_start,old_end):
        print(start,end,des)
        self.conn = sqlite3.connect("NEA_Z.db")
        self.cur = self.conn.cursor()
        self.data = self.cur.execute('''SELECT start_event, end_event
                                        FROM Dates_Details 
                                        WHERE UserID = "%s" and event_date = "%s"
                                        ORDER BY start_event'''%(self.UniqueID,cal))
        self.data = self.data.fetchall()
        self.data.remove((old_start,old_end))
        self.data.insert(0,("00:00","00:00"))
        self.data.append(("24:00","24:00"))
        print(self.data)
        if (self.date_verification(start) == True and self.date_verification(end) == True) and start < end:
            print("hello1")
            if len(self.data) != 2:
                print("hello2")
                for i in range (0,len(self.data)):
                    print("hello3")
                    if (start > self.data[i][1] and end < self.data[i+1][0]): # this algorithm will be visualised in the report
                        print("hello4")
                        self.cur.execute('''UPDATE Dates_Details 
                                            SET start_event = "%s", end_event = "%s", description = "%s"
                                            WHERE UserID = "%s" and event_date = "%s" and start_event = "%s" and end_event = "%s"'''%(start,end,des,self.UniqueID,cal,old_start,old_end))
                        self.conn.commit()
                        self.MC.destroy()
                        self.MyCalendar()
                        break
                    else:
                        if i ==(len(self.data)-1):
                            errormsg = Toplevel()
                            Label(errormsg, text= "The times you have entered arent available, review your schedule to see whats occupying that time slot").pack()
                            Button(errormsg, text= "confirm", command = errormsg.destroy).pack()
            else:
                print("hello5")
                self.cur.execute('''INSERT INTO Dates_Details (UserID,start_event,end_event,event_date,Description)
                                    VALUES("%s","%s","%s","%s","%s")'''%(self.UniqueID,start,end,cal,des))
                self.conn.commit()
                self.MC.destroy()
                self.MyCalendar()
        else:
            errormsg = Toplevel()
            Label(errormsg, text= "invalid input(s)!").pack()
            Button(errormsg, text= "confirm", command = errormsg.destroy)

                
    def date_verification(self,date):
        try:
            if len(date) == 5 :
                if int(date[0]+date[1]) > 23:
                    return False
                elif date[2] != ":":
                    return False
                elif int(date[3]+date[4]) > 59:
                    return False
                else:
                    return True
        except:
            return False


    def View_Day(self,SelectedDate):
        conn = sqlite3.connect('NEA_Z.db')
        self.df = pd.read_sql_query('SELECT * '
                            'FROM Dates_Details '                                # searching for the names and the selected date in the datebase and pulling the Start_event,end_event,event_date and name
                            'WHERE (UserID  = "%s" AND event_date = "%s"); '%(self.UniqueID,SelectedDate), conn)
        self.df = pd.DataFrame(self.df)
        self.df["start_event"] = pd.to_datetime(self.df["start_event"])
        self.df["start_event"] = self.df["start_event"].apply(lambda x: x.replace(year=1970, month=1, day=1)) #setting the axis for start_event
        self.df["end_event"] = pd.to_datetime(self.df["end_event"])
        self.df["end_event"] = self.df["end_event"].apply(lambda x: x.replace(year=1970, month=1, day=1)) #setting the axis for end_event
        self.fig = px.timeline(self.df, x_start="start_event", x_end="end_event", y="event_date",color="name",title= SelectedDate) # setting the format of the graph
        self.fig.update_xaxes(
            tickformat="%H:%M",#converts the format from years to minutes and hours
            tickformatstops=[
                dict(dtickrange=[3600000, 86400000], value="%H:%M")]  # setting the range
        )
        self.df = pd.DataFrame(self.df)
        self.fig.show()
    def Contacts(self):
        self.conn = sqlite3.connect("NEA_Z.db")
        self.cur = self.conn.cursor()
        self.contacts = self.cur.execute('''SELECT User_Details.Email
                                            FROM  User_Details,Contacts
                                            WHERE Contacts.UserID = "%s" and Contacts.FriendID = User_Details.UserID'''%(self.UniqueID))
        self.contacts = self.contacts.fetchall()
        self.contacts = [r for r, in self.contacts]
        self.CON = Toplevel()
        super(Login_SignUp,self).__init__(self.CON)
        Label(self.CON, image = self.Contacts_P).place(x=0,y=0, relheight=1, relwidth=1)
        Button(self.CON, image =self.BackB, bd= 0, bg = "#F7F7F7", activebackground= "#F7F7F7", command = lambda:[self.CON.destroy(),self.backToMain()]).place(x=22,y=21)
        Button(self.CON, image = self.AddContactB, bd= 0, bg = "#F7F7F7", activebackground= "#F7F7F7", command = lambda:[self.Addfriend()]).place(x=476,y=577)
        self.my_list = Listbox(self.CON,width=50,height= 15,font = ("Arial", 15), bd=0, bg= White,fg= Yellow ,highlightthickness=0 ,selectbackground=Yellow, selectforeground= White)
        self.my_list.place(x=305, y= 163)
        for item in self.contacts:
            self.my_list.insert(END, item)
        def profile(e):
            selectedname = (self.my_list.get(self.my_list.curselection()))
            result = self.cur.execute('''SELECT *
                                FROM User_Details,Contacts
                                WHERE Email = "%s" and Contacts.UserID = "%s" and Contacts.FriendID = User_Details.UserID'''%(selectedname,self.UniqueID))
            print(result.fetchall())
        self.my_list.bind("<Double-Button-1>",profile)
    def Addfriend(self):
        self.userentry = StringVar()
        self.ADW = Toplevel()
        self.ADW.geometry("675x700")
        self.ADW.iconbitmap("Logo.ico")
        self.ADW.title("BeTheCase")
        self.ADW.resizable(0,0)
        Label(self.ADW, image = self.AddContact_W).place(x=0,y=0, relheight=1, relwidth=1)
        Button(self.ADW, image =self.BackB, bd= 0, bg = "#F7F7F7", activebackground= "#F7F7F7", command = lambda:[self.ADW.destroy(),self.backToMain()]).place(x=22,y=21)
        Button(self.ADW, image = self.AddContactB,bd= 0, bg = "#F7F7F7", activebackground= "#F7F7F7", command = lambda:[self.check(self.userentry.get())]).place(x=239,y=514)
        Entry(self.ADW,textvariable=self.userentry,width=50).place(x=205,y=255)
    def check(self,useri):
        self.conn = sqlite3.connect("NEA_Z.db")
        self.cur = self.conn.cursor()
        self.found = self.cur.execute('''SELECT UserID
                         FROM User_Details
                         WHERE Email = "%s"'''%(useri))
        self.found = self.found.fetchone()
        self.presences = self.cur.execute('''SELECT *
                                             FROM Contacts
                                             WHERE FriendID = "%s" and UserID = "%s"'''%(self.found,self.UniqueID))
        self.presences = self.presences.fetchone()
        self.found = str(self.found)
        self.me  = "("+str(self.UniqueID)+",)"
        if self.found == "None":
            errormsg = Toplevel()
            Label(errormsg, text= "This user doesnt exist").pack()
            Button(errormsg, text= "confirm", command = errormsg.destroy).pack() 
        elif self.presences != None:
            errormsg = Toplevel()
            Label(errormsg, text= "Already in your contacts").pack()
            Button(errormsg, text= "confirm", command = errormsg.destroy).pack() 
        elif self.found == self.me:
            errormsg = Toplevel()
            Label(errormsg, text= "You cant add urself to a contact").pack()
            Button(errormsg, text= "confirm", command = errormsg.destroy).pack() 
        else:
            self.cur.execute('''INSERT INTO Contacts (UserID, FriendID) VALUES ("%s","%s")'''%(self.UniqueID,self.found[1]))
            self.conn.commit()
            self.ADW.destroy()
            self.CON.destroy()
            self.Contacts()




        

S = Login_SignUp()
S.MainW()
mainloop()
