'''
Created on 13.04.2013

@author: MrCube
'''

def isPalindrome(val):
    strVal = str(val)
    letters = [c for c in strVal]
    reversedLetters = letters[::-1]
    return letters == reversedLetters

## {{{ http://code.activestate.com/recipes/577821/ (r1)
def isqrt(x):
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y
## end of http://code.activestate.com/recipes/577821/ }}}

import math
def isSquare(val):
    intSquare =  isqrt(val)
    return intSquare*intSquare == val and isPalindrome(intSquare)

'''
input = """3
1 4
10 120
100 1000
"""
'''
import sys

input = open(sys.argv[1], "r").read()

input = input.splitlines()
numOfTests = int(input[0])
input = input[1:]

for test in range(1, numOfTests + 1):
    interval = input[0].split(' ')
    start = int(interval[0])
    end = int(interval[1]) + 1
    
    count = 0
    for i in range(start, end):
        if isPalindrome(i) and isSquare(i):
            count = count + 1
            
    print "Case #%s: %s" %(test, count)
    
    input = input[1:]