#!/usr/bin/env python3

import math

def getDigits(number):
    digits = []
    while (number >= 1) :
        digits = [number % 10] + digits
        number = int(number // 10)
    return digits

def isTidyNumber(number):
    digits = getDigits(number)
    for i in range(len(digits) - 1):
        if(digits[i] > digits[i + 1]):
            return False      
    return True

def lastTidyNumber(number):

    index = 1
    while(not isTidyNumber(number)):
        nines = int(len(getDigits(index - 1))*"9") if (index > 1) else 0
        number = int(number // index - 1) * index + nines
        index = index * 10
    return number        

t = int(input()) 
for i in range(1, t + 1):
    n =  int(input()) 
    print("Case #{}: {}".format(i, lastTidyNumber(n)))