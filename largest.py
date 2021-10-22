#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program finds the largest of 10 random numbers

import random


def greatest_number(number_list):
    # This function finds the largest of 10 random numbers

    biggest = number_list[1]

    for loop_counter in number_list:
        if loop_counter > biggest:
            biggest = loop_counter

    return biggest


def main():
    # This program finds the averae of 10 random numbers
    number_list = []

    print("Here is a list of random numbers : ")
    print("")

    for loop_counter in range(1, 11):
        random_number = random.randint(1, 100)
        number_list.append(random_number)
        print("The random number {0} is : {1}".format(loop_counter, random_number))

    biggest = greatest_number(number_list)

    print("")
    print("\nThe largest number is {0}".format(biggest))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
