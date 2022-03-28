#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on March 2022
# This program calculates the circumference of a circle using constants


def main():
    # this function can tell the user what the charge of the integer is

    # input
    number = int(input("Enter any integer: "))
    print("")

    # process & output
    if number > 0:
        print("The number {} is positive (+)".format(number))
    elif number < 0:
        print("The Number {} is Negative (-)".format(number))
    elif number == 0:
        print("Number is 0")
    else:
        print("Uh Oh")

    print("\nDone.")


if __name__ == "__main__":
    main()
