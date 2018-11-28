from audioop import reverse

__author__ = 'petrus'

#
# Problem: Old Magician
# Language: Python
# Author: Petrus T.
# Usage: python thisfile.py <input.in >output.out

#

import fileinput
from math import sqrt

def isPalindrome(n): # my naive impl.
    s = str(n)
    return s[::-1] == s

def is_palindrome_2(s): # via http://stackoverflow.com/a/11367380/198927
    return all(s[i] == s[-(i + 1)] for i in range(len(s)//2))

def compute(line):
    # find square root
    # is number?
    # test if number is a palindrome

    # test if square root is a palindrome

    a, b = map(int, line.split())

    n = 0
    for x in range(a,b+1):
        sq = sqrt(x)
        if sq.is_integer():
            #print("%d is an integer which is the root of %d" % (sq, x))
            if isPalindrome(x) and isPalindrome(int(sq)):
                n = n + 1

    return n

for i in range(int(input())):
    print("Case #%d: %s" % (i+1, compute(input())))