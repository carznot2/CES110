# print()
# length_square = input('What is the length of the side the square?    ')
# length_rectangle = input('What is the length of the rectangle?     ')
# width_rectangle = input('What is the width of the rectangle      ')
# area_square = (float(length_square) * float(length_square))
# area_rectangle = (float(length_rectangle) * float(width_rectangle))
# print(F'The area of the square is {area_square}     ')
# print(f'The area of the rectangle is {area_rectangle}     ')
# radius_circle = input('What is the radius of the circle?     ')
# area_circle = ((float(radius_circle) * float(radius_circle)) * float(3.14))
# print(f'The area of the circle is {area_circle}     ')
# print()
#Stretch Activity
# area_squarecm = float(area_squarecm/100) 
# print(f'The area of the square is {area_squarecm} cm^2')
# area_rectanglecm = float(area_rectangle/100)
# print(f'The area of the rectangle is: {area_rectanglecm} cm^2')
# area_circlecm = float(area_circle/100)
# print(f'The area of a circle is: {area_circlecm} cm^2')
# print()






print('Welcome to the velocity calculator. Please enter the following:   ')
mass = input('What is the mass in kg?   ')
gravity = input('State the gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter):    ')
time = input('State time (in seconds):    ')
density = input('State the density of the fluid (in kg/m^3, 1.3 for air, 1000 for water):    ')
cross_sectional = input('State the cross sectional area (in m^2):     ')
drag_constant = input('Drag constant (0.5 for sphere, 1.1 for cylinder):    ')


velocity_at_t = sqrt(m*g/c) * (1 - exp((-sqrt(mgc)/m)t))

Purpose: Calculate the speed of a falling object using the formula:

v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)*t))

"""

import math

m = float(input("Mass (in kg): "))
g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area (in m^2): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

