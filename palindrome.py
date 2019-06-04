# Define function to reverse string
def reverse_string(str):
    return str[::-1]

# Import regular expressions module
import re

# Input text
text_input = input("Input some text: ")

# Remove non-alphabetic characters from string, then make it lowercase
text_input = re.sub(r'[^A-Za-z]', '', text_input)
text_input = text_input.lower()

# Reverse the string
text_reverse = reverse_string(text_input)

# Check to see if the text is a palindrome!
if text_input == text_reverse:
    print("This is a palindrome!")

else:
    print("This is not a palindrome.")