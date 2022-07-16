
import string
import random

characters = string.ascii_letters + "123456789!@#£$%&/{([])}=?"

length = int(input("How long should the password be? (Just number required): "))
count = int(input("How many passwords do you want? (Just number required): "))

for p in range(count):
    password = " "
    for p in range(length):
        password_characters = random.choice(characters)
        password = password + password_characters
    print(f"Your password is: {password}")