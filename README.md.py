# Random-password-generator-

import random


uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
numbers = "0123456789"
symbols = "*#$_&-+/?!;:<>[]{}¢£¥^√÷π§∆"
#ask the user the kind of characters they want to input#

upper = input("Include uppercase letters? (yes/no): ").lower() == "yes"
lower = input("Include lowercase letters? (yes/no): ").lower() == "yes"
nums = input("Include numbers? (yes/no): ").lower() == "yes"
syms = input("Include symbols? (yes/no): ").lower() == "yes"


all = ""

# Add character sets to 'all' based on user input
if upper:
	all += uppercase_letters
if lower:
	all += lowercase_letters
if nums:
	all += numbers
if syms:
	all += symbols

# Ask the user for password length and amount
lenght = int(input("Enter password length: "))
amount = int(input("Enter number of passwords to generate: "))

# Generate and print the passwords
for x in range(amount):
	password = "".join(random.sample(all, lenght))
	print(password)

