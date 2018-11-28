# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 19:17:33 2017

@author: pellowes
"""

import numpy as np
import sys

fileIn = '/Users/pellowes/Downloads/B-large(2).in'
#fileIn = '/Users/pellowes/Downloads/A-large-practice(2).in'
fileOut = fileIn.split('.')[0]+'out'

f = open(fileIn,'r')
fo = open(fileOut,'w')

#sets to the highest number such that the number at index is value
def rollBack(digits,index,value):
    digits[index-1]=digits[index-1]-1
    for i in range(index,len(digits)):
        digits[i] = 9
    return digits
    
def solve(untidy):
    #untidy is a string
    #treat as a list of ints
    digits = []
    for number in untidy: 
        digits.append(int(number))
    #increment over series
    reset = True
    while reset:
        last_digit = 0
        reset = False
        for i in range(0,len(digits)):
            digit = digits[i]
            if digit < last_digit:
                digits = rollBack(digits,i,last_digit)
                reset = True
                print(i)
                break
            last_digit = digit
    digitsString = ''
    leadingZeros = True
    for digit in digits:
        if(digit==0 and leadingZeros):
            continue
        else:
            leadingZeros = False
        digitsString+=str(digit)
    return digitsString
            

numcases = int(f.readline())
for casenum in range(1,numcases+1):
    problem = f.readline().strip()
    
    fo.write('Case #' + repr(casenum) + ': ' + solve(problem)+'\n')
    
f.close()
fo.close()