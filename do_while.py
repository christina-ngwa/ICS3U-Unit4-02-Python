#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: October 2019
# This program finds the factorial of a postive integer


def main():
    # this function finds the factorial of a postive integer
    loop_counter = 1
    product = 1

    print("Find the factorial of an integer.")

    # input
    user_input_string = input("Enter a positive integer: ")
    print("")

    # process & output
    try:
        user_input = int(user_input_string)
        while loop_counter <= user_input:
            print("{0}".format(loop_counter))
            product = loop_counter * product
            loop_counter += 1

        print("The factorial of", user_input, "! is {0}.".format(product))
    except Exception:
        print("Wrong input. Try again.")


if __name__ == "__main__":
    main()
