#!/usr/bin/env python3
# Tidy Numbers

# from sys import argv
# import timeit # just use time in bash

# global variables and constants
TEST = False

def printOutput(number, result):
    outString = 'Case #' + str(number) + ': ' + result
    print(outString)
    return outString

# problem-specific defs

def isTidy(number):
    if number < 10:
        return True
    else: # double digits
        tidy = True
        digits = [int(x) for x in str(number)]
        for d in range(len(digits)-1):
            if digits[d] > digits[d+1]:
                tidy = False
                break
        return tidy

# (variant #3 -- take digits, sort, make new number, compare)

# returns number instead of T/F
def tidyUp(number):
    if isTidy(number):
        return number
    else: # note: 2+ digits
        digits = [int(x) for x in str(number)]
        # print("tidyup1", digits)
        for d in range(len(digits)-1):
            if digits[d] > digits[d+1]:
                digits[d] -= 1
                # print("tidyup2", d, digits)
                for dd in range(d+1, len(digits)):
                    digits[dd] = 9
                # print("tidyup3", digits)
                break
        return tidyUp(int(''.join(map(str, digits))))
        
    # j = ''.join(map(str, h))
    
# main

T = int(input())

for tt in range(1, T+1): # for each test case
    N = int(input())

    if TEST:
        print(N)
        d = tidyUp(66317)
        print(d)

    # print("N", str(N))

    result = '-1' # to indicate an issue

    # method 1 -- too slow for large dataset -- see ex. 4
    # otherwise correct
    # used for small dataset
    # 
    # for nn in range(N, 0, -1):
    #     # print("nn", nn)
    #     if isTidy(nn):
    #         result = str(nn)
    #         break

    # method 2 -- see tidyUp function
    
    # numDigits = len(str(N))
    # testof9s = int('9' * (numDigits - 1))
    # testof1s = int('1' * (numDigits))

    # # check first
    # if isTidy(N):
    #     result = N
    #     printOutput(tt, str(result))
    #     continue

    # not tidy, construct answer instead
    # j = ''.join(map(str, h))
    
    result = tidyUp(N)
    printOutput(tt, str(result))
    
