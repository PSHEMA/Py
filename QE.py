import math

# Prompt the user to input a, b, and c
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

def solve(a, b, c):
    # Compute the discriminant
    disc = b**2 - 4*a*c

    # Check if the discriminant is negative
    if disc < 0:
        # Return None to indicate no real solutions
        return None

    # Compute the solutions
    x1 = (-b + math.sqrt(disc)) / (2*a)
    x2 = (-b - math.sqrt(disc)) / (2*a)

    # Return the solutions as a tuple
    return (x1, x2)

# Call the solve() function and print the result
result = solve(a, b, c)
if result is None:
    print("No real solutions")
else:
    print("The solutions are:", result)
