def opening():
    print("********************")
    print("\n")

print("Hello Nikki")
slices = input("Pick a number\n")                                 # Creating variable
print("Great! You'll get " + str(slices) + " slices of pizza.")

opening()
def multiply(x, y):                                               # Creating function
    return x * y

x = multiply(5, 2)
print("The output if int x is " + str(x) + ".")

# Python has no command for declaring a variable.
# A variable is created when some value is assigned to it.
# The value assigned to a variable determines the data type of that variable.

# In python, void functions are not exactly the same as functions in C/C++
# If the function body does not have any return statement then a special value None returns when the function terminates

opening()
# Creating pow function 
def power(base, exponent):
    result = 1
    for x in range(exponent):
        result = result * base
    return result

def print_pow(base, exponent):
    my_power = power(base, exponent)
    print(f"{base} raised to {exponent}, the power is {my_power}.")
    # f-strings (formatted string literals) is a concise and readable way to embed variables directly into strings
    # The f before the string indicates that it is an f-string, and within the curly braces {}, can insert variables or expressions that will be evaluated and formatted into the string
    # Why Use f-strings?
        # Readability: F-strings make the code more readable compared to other methods of string formatting (like using + concatenation or .format()), especially when there are many variables to include in a string.
        # Performance: F-strings are faster than alternatives like % formatting or .format(), because they are evaluated at runtime and directly inserted into the string.

    #Comparison:

    # print("{} raised to {}, the power is {}.".format(base, exponent, my_power))

    # Or using string concatenation (less efficient and harder to read):

    # print(str(base) + " raised to " + str(exponent) + ", the power is " + str(my_power) + ".")

base = int(input("What is the base?\n"))
exponent = int(input("What is the exponent?\n"))
print_pow(base, exponent)