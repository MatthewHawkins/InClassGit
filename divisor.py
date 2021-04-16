def get_input():
    number = input("Enter in a number: ")
    return number

def find_divisors(num):
    print("Your divisors are: ")
    for i in range(1, int(num)):
        if int(num) % i == 0:
            print(i)

number = get_input()
find_divisors(number)
