# Even or Odd

def run():
    even_or_odd()
    is_multiple_of_4()
    evenly_divided()



def even_or_odd():
    print("Let's find if your number is even or odd.")
    num = input('Enter a number: ')

    print(num, ' is an even number.') if int(num) % 2 == 0 else print(num, ' is an odd number')


def is_multiple_of_4():
    print("Let's find if your number is a multiple of 4.")
    num = input('Enter a number: ')
    print(num, ' is a multiple of 4.') if int(num) % 4 == 0 else print(num, ' is not a multiple of 4')


def evenly_divided():
    print("Let's find if your 1st number is divisible by your 2nd number")
    check = input("Enter your 1st number: ")
    num = input("Enter your 2nd number: ")
    print(check, " divides evenly into ", num, "s") \
        if (int(check) % int(num) == 0) else print(check, " doesn't divide evenly into ", num, "s")


if __name__ == '__main__':
    run()
