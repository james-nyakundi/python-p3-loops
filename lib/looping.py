#!/usr/bin/env python3
def happy_new_year():
 countdown = 10
 while countdown > 0:
        print(countdown)
        countdown += 1
print("Happy New Year!")

# Call the function to see the countdown
happy_new_year()
pass
def square_integers(int_list):

    squared_numbers = [num*num  for num in int_list]
    return squared_numbers
print(square_integers([1, 2, 3, 4, 5]))
pass

def fizzbuzz():
    
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Call the function to see the FizzBuzz sequence
fizzbuzz()
pass
