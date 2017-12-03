#!/usr/bin/python3
def LHS(a,b):
    return (a+b)**2


def RHS(a,b):
    return a**2+2*a*b+b**2


a=input("Enter first number: ")
b=input("Enter second number: ")

l=LHS(int(a),int(b))
r=RHS(int(a),int(b))

print("LHS =(a+b)^2\n    =({0}+{1})^2\n    ={2}".format(a,b,l))
print("RHS =a^2 + 2 x a x b + b^2\n    ={0}^2 + 2 x {0} x {1} + {1}^2\n    ={2}\n".format(a,b,r))

print("\nHere, LHS = RHS\nTherefore, (a+b)^2 = a^2 + 2 x a x b + b^2.".format(l))
