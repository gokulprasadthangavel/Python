import calendar
# TO print the week header
print(calendar.weekheader(1))
print()
# This will print the calendar
print (calendar.calendar(2019))
# For example if we wanted to print the single month eg:- March
print (calendar.month(2019, 3))
# Python's default first day of the calendar is monday, so it starts with monday.
# If we wanted to start the day with Sunday then, we have to  use setfirstweekday
calendar.setfirstweekday(calendar.SUNDAY)
# Now the calendar will be printed with sunday as the first day
print(calendar.calendar(2019))