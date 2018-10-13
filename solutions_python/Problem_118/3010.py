#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Luís Brandão on 2013-04-13.
"""

import sys
import os
import math

def qualificationC():
    inputFile = open("C-small-attempt0.in")
    outputFile = open("qualification-C-sample-luisbrandao.txt","w")
    counter = 0
    cases = 0
    res = 0
    min_val = 0
    min_val = 0
    for line in inputFile:
        line = line.replace('\n','')
        if counter is 0:
            cases = int(line)
        else:            
            line = line.split(' ')
            
            min_val = int(line[0])
            max_val = int(line[1])
            avg_val = int(max_val / 2) + 1

            lowest = int(math.ceil(math.sqrt(min_val)))
            heighest = int(math.sqrt(max_val))

            for n in range(lowest, heighest + 1):                
                n_sqrt = str(n**2)
                if isPalindrome(n_sqrt) and isPalindrome(str(n)):
                    res = res + 1

            print 'Case #{0}: {1}'.format(counter,res)
            outputFile.write("Case #{0}: {1}\n".format(counter,res))
        counter = counter + 1
        res = 0
    outputFile.close()

def isPalindrome(str):
    return str[::-1].lower() == str.lower()

def main():
    # qualificationA()
    qualificationC()

if __name__ == '__main__':
	main()

