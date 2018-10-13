#!/usr/bin/env python
# coding: utf8

import sys
from math import sqrt, ceil, floor
import itertools

DATASET_LENGTH_MAX  = 7

class Lines(object):
    def __init__(self, lines):
        self.lines = lines[:]
        self.counter = 0
    #enddef
    
    def __call__(self):
        retval = self.lines[self.counter].strip("\n")
        self.counter += 1
        return retval
    #enddef
#endclass


def isFair(number):
    for i in xrange(len(number) / 2):
        if (number[i] != number[-(i + 1)]):
            return False
        #endif
    #endfor
    return True
#enddef


def solve(fairAndSquareNumbers, low, high):
    count = 0
    for number in fairAndSquareNumbers:
        if number >= low and number <= high:
            count += 1
    #endfor
    return count
#enddef


def generatePalindromes(length):
    digits = range(10)
    if length == 1:
        return digits[1:]
    #endif
    
    retval = []
    for i in itertools.product("0123456789", repeat = length // 2):
        s = "".join(i)
        if not s.startswith("0"):
            if (length % 2 == 0):
                retval.append(int(s + s[::-1]))
            else:
                for digit in "0123456789":
                    retval.append(int(s + digit + s[::-1]))
                #endfor
            #endif
        #endif
    #endfor
    return retval
#enddef


def prepareData(maxLength):
    retval = []
    for i in xrange(1, maxLength + 1):
        palindromes = generatePalindromes(i)
        for one in palindromes:
            square = one * one
            if isFair(str(square)):
                retval.append(square)
            #endif
        #endfor
    #endfor
    return retval
#enddef


if __name__ == "__main__":
    fairAndSquareNumbers = tuple(prepareData(DATASET_LENGTH_MAX))

    lines = Lines(open(sys.argv[1], "r").readlines())
    caseCount = int(lines())
    for caseNumber in xrange(1, caseCount + 1):
        print "Case #%d:" % caseNumber,
        print solve(fairAndSquareNumbers, *(int(one) for one in lines().split(" ")))
    #endfor
#endif
