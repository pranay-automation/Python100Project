import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to the python password generator!")
nr_letter = int(input("How many letters would you like in your password\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_number = int(input("How many numbers would you like?\n"))


#Easy Password Generator
password = ""

for char in range(1, nr_letter + 1):
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(numbers)

for char in range(1, nr_number + 1):
    password += random.choice(symbols4)

print(password)

# Hard password generator
#Easy Password Generator
password_list = []

for char in range(1, nr_letter + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(numbers))

for char in range(1, nr_number + 1):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is : {password}")

