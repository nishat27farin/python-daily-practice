# Basic Print
print("Hello! World")
print(123)

#Printing Multiple Items
name = "Nishat"
gender = "Female"
country = "Bangladesh"
print("Name:", name, "Gender:", gender, "Country:", country )

#Using String Concatenation
name = "Nishat"
ID = 123
print("Name:" + name +", ID:" + str(ID)) # str() converts integer 'ID' to string for concatenation

#Using f-Strings ❤️
name = "Nishat"
ID = 123
print(f"My name is {name} and my ID is {ID}.")

#Using .format() Method
name = "Nishat"
ID = 123
print("My name is {} and my ID is {}." .format(name, ID))

#Printing Without Newline
print("Hello", end=" ") #By default, print() adds a newline at the end. Can change it using end.
print("World")
print("Nishat")

#Printing with Separator
print("Python", "Java", "C++", sep=", ")



""" 
✅ Assignment:
Print your name, age, and city in at least 3 different ways using the techniques above.
Use sep and end at least once.

"""

# 🚀 Try it yourself first before scrolling down to see the solution!


name = "Nishat"
age = 25
city = "Dhaka"
print(f"My name is {name}, I am {age} years old and lives in {city}")
print("My name is {}, I am {} years old and lives in {}".format(name,age,city))
print ("My name is," + name + "," , end=" ")
print ("I am", age, "years old and lives in", city, sep=" ")