# Create Variable named "string" with value "Hello"
string = "Hello"

# Printing indexing examples
print(string[0])
print(string[:4])
print(string[-1])

# Create Variable named "string_alphabet" with value "abcdefghijk"
string_alphabet = "abcdefghijk"

# Printing indexing examples
print(string_alphabet)
print(string_alphabet[2:])
print(string_alphabet[:3])
print(string_alphabet[3:6])
print(string_alphabet[1:3])

# Exercise try to get only "defghi" from variable string_alphabet
print(string_alphabet[3:9])

# Printing slicing examples
print(string_alphabet[::2])
print(string_alphabet[2:7:2])
print(string_alphabet[::-1])

# Exercise 1
# Write a string index that returns just the letter 'r'  from 'Hello World' .
# For example, 'Hello World'[0]  returns 'H'
# You should only write one line of code for this. Do not assign a variable name to the string.
print("Hello World"[8])

# Exercise 2
# String Slicing
# Use string slicing to grab the word 'ink'  from inside 'tinker'
# For example, 'education'[3:6]  returns 'cat'
# Remember that when slicing you only go up to but not including the end index.
# You should only write one line of code for this. Do not assign a variable name to the string.
print("tinker"[1:4])

# Learning about String Properties and Methods
# String Concatenation
# Change name from Sam to Pam
name = "Sam"
print(name[1:])
last_letters = name[1:]
print("P" + last_letters)

x = "Hello World"
x = x + " it's beautiful outside!"
print(x)

letter = "z"
print(10 * letter)

print(2 + 3)
print("2" + "3")

# Methods
x = "Hello World"
print(x.upper())
print(x.lower())

x = "Hello this is a string"
print(x.split())
print(x.split("i"))

# String formatting for printing
# .format() method
print("This is a string {}".format("INSERTED"))
print("The {2} {1} {0}".format("fox", "brown", "quick"))
print("The {0} {0} {0}".format("fox", "brown", "quick"))
print("The {q} {b} {f}".format(f = "fox", b = "brown", q = "quick"))

# Float formatting
result = 2984/777
print(result)
print("The result was {r:1.3f}".format(r = result))

name = "Jose"
age = 16
print(f"Hello his name is {name} he's {age}")

# Exercise
# Print Formatting
# Write an expression using any of the string formatting methods we have learned (except f-strings, see note below) to return the phrase 'Python rules!'
# For example, these phrases both return 'I like apples' :
# 'I like %s' %'apples'
# 'I like {}'.format('apples')
# Your solution should be entered on one line. You can not use variable names, only the strings themselves.
# NOTE: At this time, f-strings won't work! Udemy Coding Exercises use Python 3.5.2, and f-strings require Python 3.6 or higher.
print("{0} {1}".format("Python", "rules!"))

