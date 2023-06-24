import datetime


date = input("Enter a date (YYYY-MM-DD): ")

boom = datetime.datetime.strptime(date, '%Y-%m-%d').date()

day = boom.strftime('%A')

print("The day on", date, "is", day)
