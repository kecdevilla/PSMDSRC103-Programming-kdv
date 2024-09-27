import math

def quadratic_formula(a, b, c):
    file = open('quadratic_log.txt', 'a') # using 'a' append instead of 'w' so that we won't overwrite 
        # it everytime we use the function

    file.write(f"Solving for a: {a}, b: {b}, c: {c} \n")
        
    # friendly reminder that discriminant is b^2 - 4ac and determined how many roots the function has
    if b**2 - (4*a*c) < 0: # checks if the discriminant is negative. Negative discriminant means equation has complex (imaginary) roots
        x1 = (complex(-b, math.floor(math.sqrt(abs(b**2 - (4*a*c)))))) / (2*a) # -b is real, other is imaginary.
        # math.sqrt(abs(b**2 - (4*a*c))) takes the square root of the absolute value of the discriminant
        # math.floor() rounds down the expression to the nearest integer
        # divide everything by 2a to get the first root of the equation
        x2 = (complex(-b, -1 * math.floor(math.sqrt(abs(b**2 - (4*a*c)))))) / (2*a) # same with x1 except negative discriminant

        file.write(f"Imaginary Roots: {x1}, {x2}\n")
        
    else: 
        x1 = (-b + math.sqrt(b**2 - (4*a*c))) / (2*a)
        x2 = (-b - math.sqrt(b**2 - (4*a*c))) / (2*a)

        file.write(f"Real Roots: {x1}, {x2}\n")

    print('--------------\n')

    file.close