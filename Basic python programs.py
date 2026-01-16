#write a for loop program to print 4 in string format 4 times.
for i in range(4):
    print("4") # "4" is the string format of 4
#Use input function and give True as input and check if it is Boolean if no print its data type.
user_input = input("Enter a value: ")
if user_input == "True": # checking whether the input given by the user is True or not
    print(True)
else:
    print(type(user_input))
# Write a Python program to print "Welcome to Python Training!".
print("Welcome to Python Training!")
#Assign values to different variables and print their data types using type().
a=11
b=25.5
c='t'
d=False
print(type(a)) # int
print(type(b)) # float
print(type(c)) # str
print(type(d)) # bool
#Take user input for name and age, then display them.
name=input("Enter your name")
age=int(input("Enter you age"))
print("Name:",name)
print("Age:",age)