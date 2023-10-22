# A very basic example of a function
def my_function():
    print("Hello, this is my function")


my_function()


# Task 1 - Create a function of any name , which when called, prints "Hello world!"

def hello_world():
    print("Hello world!")


hello_world()


# Another basic function, which takes in two arguments and prints them
def add_stuff(value1, value2):
    print(value1, value2)


add_stuff("Siddharth", 56)


# Task 2 - Create a function which takes 3 parameters and prints them in reverse order
def reverse_order(val1, val2, val3):
    print(val3, val2, val1)


reverse_order(59, 69, 79)


# Basic function for finding the length of two strings and printing their sum
def get_sum_string_lengths(string1, string2):
    len_string1 = len(string1)
    len_string2 = len(string2)
    print(len_string1 + len_string2)


get_sum_string_lengths("Siddharth", "Jaiswal")


# Basic function for taking a string as input and returning its first half characters
def half_string(string):
    len_string = len(string)
    half_len = len_string // 2
    print(string[0:half_len])


half_string("Siddharth")


# Task 3 - Create a function to input two strings, and print both of them in half
# For example: s1 = Siddharth, s2 = Jaiswal
# Output should be: SiddJai
def str_half_sum(string1, string2):
    len_string1 = len(string1)
    len_string2 = len(string2)
    half_len_str1 = len_string1 // 2
    half_len_str2 = len_string2 // 2
    print(string1[0: half_len_str1], string2[0: half_len_str2], sep='')


str_half_sum("Siddharth", "Jaiswal")


# A function which can have a variable nnumber of parameters. The output should be the sum of all these elements
def print_sum_of_inputs(*args):
    for arg in args:
        print(arg, end="")


print_sum_of_inputs("Siddharth", "Jaiswal", "Animesh", "Singh", 5, 81763, True, [18265, "Hishia"])


# Task 4 - Create a function to take any number of inputs and print them in reverse order
def sum_all_input_rev(*args):
    print()
    for value in args:
        print(value, end="")


sum_all_input_rev("Siddharth", "Jaiswal", "Animesh", "Singh", 5, 81763, True, [18265, "Hishia"])
