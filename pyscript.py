#!/usr/bin/python3
print("This program gives you the average of three numbers.")

name=input("Enter your name: ")
num1=int (input("Enter the first number: "))
num2=int (input("Enter the second number: "))
num3=int (input("Enter the third number: "))

print("Hi,"+name+".The numbers you entered are: \nnum1={0}\nnum2={1}\nnum3={2}".format(num1,num2,num3))
print("\nAverage = {}".format((num1+num2+num3)/3))

print("\nThank you for using my program.")
