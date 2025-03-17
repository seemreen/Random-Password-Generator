import random
password = "ABCDEFGHIJKLMNOPQRSTYXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-}{?:"
length_password = int(input("Enter the length of the password: "))
a = "".join(random.sample(password, length_password))
print(f"Your password is {a}")