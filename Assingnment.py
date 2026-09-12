name = str( input("Enter your name:"))
a_or_w = str(input("Are you Alone or With parents? :"))
age = int(input("Enter your age:"))
if age >= 10 and a_or_w == "Alone" or a_or_w == "With parents":
    SJS = "You can enter in the swimming pool."
elif age < 10 and a_or_w =="With parents":
    SJS = "You may enter the pool but take care."
elif age < 10 and a_or_w == "Alone":
    SJS = "You can't enter in the pool"
else:
    print("It mus t be a spelling error:")
    print("(It should be like this:) With parents")
    print("Alone")
    print("Age should be in numbers")
print("\n==== SWIMING POOL ENTERY CHECKER ====")
print("Hello",name)
print(SJS)
print("=====================================")
