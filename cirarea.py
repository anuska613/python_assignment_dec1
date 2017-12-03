#!/usr/bin/python3
def circle_area(radius):
    appx_pi=22/7
    return appx_pi*radius**2


radius=input("Enter the radius of the circle: ")

area=circle_area(float(radius))

print("\nRadius of circle : {0} cm\nArea of circle : {1:.3f} cm sq".format(radius,area))

