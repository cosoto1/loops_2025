# Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
# While loops  

# you can iterate a range sequce ect. 

credit_card =("1234-5678-9012-3456")

for x in credit_card:
    print(x)

for x in range (1,21):
    if x == 13:
        break
    else:
        print(x)




name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"Hello {name}")


age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")


food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("bye")


num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"Your number is {num}")