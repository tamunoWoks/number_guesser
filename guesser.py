import random

range_limit = input("Type a number: ").strip()

if range_limit.isdigit():
    range_limit = int(range_limit)

    if range_limit <= 0:
        print('You must enter a number larger than 0')
        quit()

else:
    print('You must enter a number')
    quit()