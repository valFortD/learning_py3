def opening():
    print("********************")

print("Hello Nikki")
slices = input("Pick a number\n") # Creating variable
print("Great! You'll get " + str(slices) + " slices of pizza.")

opening() # Creating function
def multiply(x, y):
    return x * y

x = int(input("Pick a number for x\n"))
y = int(input("Pick a number for y\n"))
total = multiply(x, y)
print(f"The total of x * y with multiply() function is {total}.")

# Python has no command for declaring a variable.
# A variable is created when some value is assigned to it.
# The value assigned to a variable determines the data type of that variable.
# In Python, void functions are not exactly the same as functions in C/C++
# If the function body does not have any return statement then a special value None returns when the function terminates

opening()
def power(base, exponent):                                              # Creating pow function
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

# Python is an interpreted language
# Unlike C++, python does not need datatype when declaring variables
# Python data types are numeric(int, float), dictionary{}, bool, set{}, sequence types(string, list, tuple) 

opening() # Integral types in C++, numeric in Python
# int = integers, contains positive and negative whole numbers. No fractions or decimals
# float = floating numbers = decimal point numbers
# complex = complex numbers

a = 1
print(f"Type of a is {type(a)}.")

b = 1.0
print(f"The type of b is {type(b)}.")

c = 1 + 1j
print(f"The type of c is {type(c)}.")

# Compared to C/C++, Python DOES NOT have signed and unsigned integers as data types
# There is no need to specify the data types of variables as the interpreter itself predicts the variable data type based on the value assigned to it
# But can still convert signed integer to unsigned integer with the following example
signed_integer = -100

# Adding 2^32 to convert signed to unsigned integer
unsigned_integer = signed_integer + 2**32
print(unsigned_integer)
print(type(unsigned_integer))

opening()
print(f"Python3 use Unicode by default and it allows for the representation of a much wider range of characters. Thus Python does not have a character data type like C++ does.")

opening() # In Python it is known as Escape Characters(Escape sequences in C++)
text1 = "Hello"
text2 = "There"
print("Python and C++ are \"super\" awesome!")       # \" for strings
print("\\\' is used for single \'1\' character.")    # \' for chars and \\ for one backlash
print(f"{text1}\r {text2}.")                         # \r similar to \n? carriage return?
print(f"{text1}\t {text2}.")                         # \t tab between strings
print(f"{text1}\b {text2}.")                         # \b delete a char
print(f"{text1}\f{text2}.")                          # \f == \v(C++)

opening() # BOOL FUNCTION
not_found = 0
found = True
num = 5
print(bool(num))
print(bool(found))
print(bool(not_found))

# Any strings, list, tuple, set and dictionary are True, except empty ones
# Any number is True, except 0