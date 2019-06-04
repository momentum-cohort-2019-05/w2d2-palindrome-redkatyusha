# gonna try a couple different strategies here and see if any of them work

# function to reverse a string
def reverse_string(str):
    return str[::-1]

# For testing use only
#print(reverse_string("yavanna"))

# Import regular expressions module
import re

# Input statement
text_input = input("Input some text: ")
text_input = re.sub(r'[^A-Za-z]', '', text_input)
text_reverse = reverse_string(text_input)

# If statements

if text_input == text_reverse:
    print("This is a palindrome!")

else:
    print("This is not a palindrome.")