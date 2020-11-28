#!/usr/bin/env python3

# Created by Tong Gong
# Created time November 2020
# This is a program that asks the user for 2 numbers
# and then adds the 2 number together.

import math


def main():
    # This is the funciton to calculate 2 numbers and add them up.

    # Input
    number1 = int(input("Enter the first number you want calculate"))
    number2 = int(input("Enter the the second number you want calculate"))

    # Process
    answer = number1 + number2

    # Output
    print("")
    print("{0} + {1} = {2}".format(number1, number2, answer))


if __name__ == "__main__":
    main()
