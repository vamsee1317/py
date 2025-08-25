# -------------------------------
# Introduction to Python
# -------------------------------

# 1. What is Python?
#    - Python is a high-level, interpreted programming language.
#    - It is known for its simplicity and readability.
#    - Python supports multiple programming paradigms:
#        * Procedural
#        * Object-Oriented
#        * Functional
#    - Created by Guido van Rossum in 1991.

# 2. Features of Python:
#    - Easy to learn and read (syntax similar to English).
#    - Open-source and free to use.
#    - Interpreted (code runs line by line).
#    - Dynamically typed (no need to declare variable types explicitly).
#    - Cross-platform (works on Windows, Mac, Linux).
#    - Huge standard library + third-party packages.
#    - Supports integration with other languages (C, C++, Java).

# 3. Applications of Python:
#    - Web Development (Django, Flask, FastAPI).
#    - Data Science & Machine Learning (Pandas, NumPy, scikit-learn).
#    - Artificial Intelligence (TensorFlow, PyTorch).
#    - Automation & Scripting.
#    - Game Development.
#    - Desktop GUI Applications.
#    - Embedded Systems & IoT.

# 4. Python Versions:
#    - Python 2.x (older, not recommended).
#    - Python 3.x (current and widely used).
#    - Latest stable version: Python 3.12 (2025).

# 5. Python Interpreter:
#    - Runs Python code line by line.
#    - You can use:
#        * Python Shell (interactive mode).
#        * Script Mode (writing .py files and running them).

# 6. Python as Interpreted Language:
#    - Unlike compiled languages (C, C++), Python does not need explicit compilation.
#    - The interpreter directly executes the instructions.

# 7. Python as Dynamically Typed:
#    - You don’t need to declare variable types.
#    - Example:
x = 10         # Integer
x = "Vamsi"    # Now it's a String
print(x)

# 8. Python Comments:
#    - Single line: starts with #
#    - Multi-line: use triple quotes (''' or """)
# Example:
# This is a single-line comment
"""
This is a
multi-line comment
"""

# 9. First Python Program:
print("Hello, World!")

# -------------------------------
# End of Introduction
# -------------------------------


# -------------------------------
# Python Syntax, Indentation, Variables, Identifiers & Keywords
# -------------------------------

# 1. Python Syntax Rules:
#    - Python uses indentation instead of braces {}.
#    - Code blocks are defined by spaces or tabs.
#    - Each statement is usually written on a new line.
#    - Python is case-sensitive.
# Example:
if True:
    print("This is inside an if block")   # Correct indentation
# print("This will cause error")         # Uncomment -> IndentationError


# 2. Python Indentation:
#    - Indentation is compulsory in Python.
#    - By default, 4 spaces are used as a standard indentation.
# Example:
for i in range(3):
    print("Loop:", i)
print("Outside loop")


# 3. Variables in Python:
#    - A variable is a name that refers to a value stored in memory.
#    - No need to declare type; Python assigns it dynamically.
#    - Variables are created when a value is assigned.
# Example:
name = "Vamsi"
age = 27
pi = 3.14159
print(name, age, pi)


# 4. Variable Naming Rules:
#    - Can contain letters, digits, and underscores.
#    - Must start with a letter or underscore (_).
#    - Cannot start with a digit.
#    - Cannot use Python keywords as variable names.
#    - Case-sensitive (Name and name are different).
# Valid Examples:
first_name = "Krishna"
_age = 30
rollNumber123 = 45
# Invalid Examples:
# 123age = 20    ❌ (starts with digit)
# first-name = "abc" ❌ (no hyphens allowed)
# class = "xyz" ❌ (class is a reserved keyword)


# 5. Identifiers:
#    - Identifiers are names given to variables, functions, classes, etc.
#    - Follow the same naming rules as variables.
# Example:
def my_function():
    return "Hello"
print(my_function())


# 6. Keywords in Python:
#    - Keywords are reserved words with special meaning.
#    - Cannot be used as identifiers.
#    - Examples: if, else, while, for, def, class, import, return, True, False
import keyword
print("Python Keywords:", keyword.kwlist)
print("Total Keywords:", len(keyword.kwlist))


# -------------------------------
# End of Syntax & Basics Notes
# -------------------------------

