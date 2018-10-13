#!/usr/bin/env python

import sys

def readContent(fileName):
    with open(fileName, "r") as f_in:
        case = 1
        for line in f_in:
            line = line.strip()
            fieldArray = line.split()
            if len(fieldArray) == 2:
                try:
                    begin = int(fieldArray[0])
                    end = int(fieldArray[1])
                except ValueError:
                    print("Oops! The begin or end interval cannot be \
                            coverted to integer")
                    print(fieldArray)
                    sys.exit()
                calculate(begin,end, case)
                case += 1

def calculate(begin, end, case):
    num = 0
    for i in range(begin, end+1):
        root = float(i**(1/2))
        if checkPalindromes(float(i)) and checkPalindromes(root):
            num += 1
    print("Case","#"+str(case)+":",num)

def checkPalindromes(i):
    forwardStr = str(i)
    array = forwardStr.split('.')
    if array[1] == '0':
        forwardStr = array[0]
    reverseStr = forwardStr[::-1]
    return (forwardStr == reverseStr)


if __name__ == "__main__":
    assert len(sys.argv) < 3, "Too many arguments"
    readContent(sys.argv[1])
