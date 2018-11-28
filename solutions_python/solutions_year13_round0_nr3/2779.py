#!/usr/bin/python3

import sys
from time import sleep

def read_input(numbers, file):
    cases = 0

    with open(file, "r") as fp:
        cases = fp.readline().strip('\n')

        for line in fp:
            if line == '\n':
                continue
            low, high = line.strip('\n').split()
            numbers.append([int(low), int(high)])

    return cases, numbers

def checkPalindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    return False

def checkSquare(number):
    if (number**0.5).is_integer():
        return int(number**0.5)
    return -1

def parseNumbers(cases, numbers):
    case = 1
    count = 1

    for low, high in numbers:
        count = 0
        for number in range(low, high+1):
            if not checkPalindrome(number):
                continue
            square = checkSquare(number)
            if square == -1:
                continue
            if not checkPalindrome(square):
                continue
            count += 1
        #sleep(5)

        print("Case #%d: %d" % (case, count))
        case += 1

cases, numbers = read_input([], sys.argv[1])
parseNumbers(cases, numbers)
