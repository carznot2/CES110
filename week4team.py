import math
print('Welcome to the Calculator. Please enter the following:')
print()
mass = float(input('Mass (in kg):   '))
gravity = float(input('Gravity(in m/s^2, 9.8 for Earth, 24 for Jupiter):     '))
time = float(input('Time (in seconds):     '))
density = float(input('Density in Fluid(in kg/m^3, 1.3 for air, 1000 for water):    '))
cross_sec = float(input('Cross Sectional Area (in m^2):    ')) 
drag = float(input('Drag Constant (0.5 for sphere, 1.1 for cylinder):    '))
inner_c = (1/2) * (density) * (drag)
velocity = math.sqrt(((mass) * (gravity)) / (inner_c)) * (1 - math.exp((-math.sqrt((mass) * (gravity) * (inner_c))) / (mass) * (time)))
print()
print(f'The inner value of c is: {inner_c:.3f}')
print(f'The velocity after {time:.1f} is {velocity:.3f} m/s')
print()