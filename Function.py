# 1. len() function in Python
# The len() function returns the number of elements in a sequence (e.g., list, string, tuple, dictionary, etc.).

# Example usage of len() with a list:
numbers = [10, 20, 30, 40, 50]
print("Length of the list:", len(numbers))  # Output: 5


# 2. Function to greet a person
def greet(name):
    print(f"Hello, {name}!")

greet("Agishma")


# 3. Function to find the maximum number in a list without using max()
def find_maximum(numbers):
    if not numbers:
        return None

    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


num_list = [15, 45, 78, 23, 89, 34]
print("Maximum value:", find_maximum(num_list))  # Output: 89

# 4. Local vs Global Variables
# Local variables are defined inside a function and can only be accessed within that function.
# Global variables are defined outside a function and can be accessed from anywhere in the script.

global_var = "I am a global variable"


def demo_function():
    global_var = "I am a local variable"  # This is a local variable
    print("Inside function:", global_var)


# Example usage:
demo_function()
print("Outside function:", global_var)  # The global variable remains unchanged


# 5. Function to calculate the area of a rectangle with a default width
def calculate_area(length, width=5):
    return length * width


print("Area with both arguments:", calculate_area(10, 4))
print("Area with only length:", calculate_area(10))
