import random

def get_input():
    number = input("Enter in a number: ")
    return int(number)


def generate_password(num):
    random.seed()
    password = ""
    for i in range(num):
        password += str(random.randrange(0,9))
    print(password)

num = get_input()
generate_password(num)