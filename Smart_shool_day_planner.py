print("=== SMART SCHOOL DAY PLANNER ===")
print("Answer 3 quick questions and I will plan your day! \n")
day = input("What day is  it? (Monday to Sunday):")
weather = input("What is the weather? (Sunny / Rainy / Cloudy):")
homework = input("Is your homework done? (yes / no )")
print("\n === Your Plan for {day} ===")
print("_"* 35)
if day in ("Saturday","Sunday"):
    print("Day type : Weekend - enjoy your free time!")
elif day == "Monday":
    print("Day type : First day of the week.Pack your weekly planner.")
elif day == "Friday":
    print("Day type : Last day of school.Return library books today.")
elif day == ("Tuesday","Wednesday","Thursday"):
    print("Day type : Regular school day.Stay focused!")
else:
    print("Day type : day not recognised.Please check the spelling")
if weather == "Sunny" and homework == "yes":
    print("After school head to the park, great weather and homework is done")
if weather == "Rainy" or weather == "Cloudy":
    print("Weather tip : Packer your umbrella - it may get wet outside.")
if not (homework == "yes"):
    print("Homework : Not done yet.Finish it before going out!")

