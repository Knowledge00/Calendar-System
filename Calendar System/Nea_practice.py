from tkinter import *
import plotly.express as px
from sqlalchemy import create_engine
import pandas as pd
import sqlite3
root = Tk()
root.withdraw()
def Page1W():
    Page1 = Toplevel()
    Page1.geometry(1150,700)
    Email = StringVar()
    Password1 = StringVar()
    Picture1W = PhotoImage("")
    Entry(Page1, textvariable=Email).place(x=10,y=100)
    Entry(Page1, textvariable=Password1).place(x=10, y=200)
    Button(Page1,command = calendarcollection).place(x=10, y=25)
def calendarcollection():
    title23 = "4/8/2020"
    hello = "frank"
    Password = "philip1"
    disk_engine = create_engine('sqlite:///NEA_Z.db')

    df = pd.read_sql_query('SELECT start_event, end_event, event_date, name '
                           'FROM CalendarEvents '
                           'WHERE (name  = "%s" OR name = "%s") AND (event_date = "%s"); '%(hello,Password, title23), disk_engine)
    df["start_event"] = pd.to_datetime(df["start_event"])
    df["start_event"] = df["start_event"].apply(lambda x: x.replace(year=1970, month=1, day=1))
    df["end_event"] = pd.to_datetime(df["end_event"])
    df["end_event"] = df["end_event"].apply(lambda x: x.replace(year=1970, month=1, day=1))



    fig = px.timeline(df, x_start="start_event", x_end="end_event", y="name",color="name",title= title23)
    fig.update_xaxes(
        tickformat="%H:%M",
        tickformatstops=[
            dict(dtickrange=[3600000, 86400000], value="%H:%M")]  # range is 1 hour to 24 hours
    )
    fig.show()
Page1W()
mainloop()
