import calendar
# TO print the week header
print(calendar.weekheader(1))
print()
# Print calendar first week of the day
print(calendar.firstweekday())
print()
# This will print the calendar
print (calendar.calendar(2019))
# For example if we wanted to print the single month eg:- March
print (calendar.month(2019, 3))
# Python's default first day of the calendar is monday, so it starts with monday.
# If we wanted to start the day with Sunday then, we have to  use setfirstweekday
calendar.setfirstweekday(calendar.SUNDAY)
# Check whether first day of the week is changed to sunday, if it is right it should print as "6"
print(calendar.firstweekday())
# Now the calendar will be printed with sunday as the first day
print(calendar.calendar(2019))
# find whether a year is a leap year or non leap year
leap=calendar.isleap(2019)
print(leap)