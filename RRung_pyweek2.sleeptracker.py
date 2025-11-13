# Sleep Tracker
days = int(input("How many days do you want to log? "))
total_sleep = 0
for i in range(days):
    hours = float(input(f"Hours slept on day {i+1}: "))
    total_sleep += hours
average = total_sleep / days
print("Total hours slept:", total_sleep)
print("Average hours per night:", round(average, 2))
if average < 7:
    print("You should try to get more rest!")
else:
    print("Nice! You're getting enough sleep.")
