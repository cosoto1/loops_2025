# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]

print(len(fruits))

# Challenge:
# Use a for loop to print each fruit on a new line.
print(fruits[0])
print(fruits[1])
print(fruits[2])
for fruit in fruits:
    print(fruit)
# i just worked with loops

# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
for subject in subjects:
    print(subject)

for subject in subjects:
    if subject == "History":
        break
    print(subject)

for subject in subjects:
    if subject == "Science":
        continue
    print(subject)

list1000 = list(range[1,1000])
for number in list1000:
    if number > 599:
        break
    print (number)

list600 = list(range[1,601])
for number in list600:
    if 300 <= number <= 500:
        continue
    print(number)



# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"


# Given:
numbers = [5, 10, 15, 20]

# Challenge:
# Use a for loop to add all the numbers and print the total.