import random
import string

print("Welcome to Password Generator")
length = int(input("How long would you like your password to be?: "))
letters = string.ascii_letters+string.digits+string.punctuation
password = ""
for i in range(length):
    password += random.choice(letters)

print("Generated password:",password)

