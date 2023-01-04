import tkinter as tk
from tkcalendar import Calendar
import datetime
class MyCalendar(Calendar):
    def __init__(self, master=None, **kw):
        self._disabled_dates = []
        Calendar.__init__(self, master, **kw)

    def disable_date(self, date):
        self._disabled_dates.append(date)
        mi, mj = self._get_day_coords(date)
        if mi is not None:  # date is displayed
            self._calendar[mi][mj].state(['disabled'])


root = tk.Tk()
cal = MyCalendar(root, selectmode='day',
                 year=2022, month=5, disableddaybackground="red",
                 day=22)
cal.disable_date(datetime.date(2022,5,1))
cal.disable_date(datetime.date(2022, 5, 25))
cal.disable_date(datetime.date(2022, 5, 31))
cal.pack(pady=20)
day = datetime.date(2022,7,5)
cal.calevent_create(day, "" ,tags="hi")
cal.tag_config("hi", background="blue")
def grad_date():
    date.config(text="Selected Date is: " + cal.get_date())

tk.Button(root, text="Get Date",
          command=grad_date).pack(pady=20)

date = tk.Label(root, text="")
date.pack(pady=20)

root.mainloop()