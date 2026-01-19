n = int(input("Enter a number between 1 and 10: "))

if n == 1:
    print(1)
elif n == 2:
    print(2)
elif n == 3:
    print(3)
elif n == 4:
    print(4)
elif n == 5:
    print(5)
elif n == 6:
    print(6)
elif n == 7:
    print(7)
elif n == 8:
    print(8)
elif n == 9:
    print(9)
elif n == 10:
    print(10)

# take two inputs from user and print their sum
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
print("sum:",a+b)

#Ask name and age and print formatted greeting.
name=input("Enter your name:")
age=int(input("Enter your age:"))
print("your name is ",name," and your age is ",age)

#Convert kilometers to miles.
km=int(input("Enter distance in km:"))
print("Distance in miles is:",km*0.6)

#Compute area of a triangle.
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("The area of the triangle is:", area)

#Print type of each variable entered by user.
var1 = input("Enter first variable: ")
var2 = input("Enter second variable: ")
var3 = input("Enter third variable: ")
print("Type of first variable:", type(var1))
print("Type of second variable:", type(var2))
print("Type of third variable:", type(var3))
