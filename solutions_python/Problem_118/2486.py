#!/usr/bin/python

import math

def ispalindrome(n):
    rest = n
    rev = 0
    while rest:
        rev = (rev * 10) + (rest % 10)
        rest /= 10
    return n == rev

def find_fair_palindromes(a, b):
    for i in range(int(math.sqrt(a)), int(math.sqrt(b) + 1)):
        if ispalindrome(i):
            candidate = i ** 2
            if candidate >= a and candidate <= b and ispalindrome(candidate):
                yield i ** 2

if __name__ == '__main__':
    import re
    import sys

    count = int(sys.stdin.readline().strip())
    case = 1
    for case in range(1, count + 1):
        a, b = (int(i) for i in
            re.match("(\d*)\s*(\d*)", sys.stdin.readline()).groups())
        palindromes = list(find_fair_palindromes(a, b))
        print "Case #%s: %i" % (case, len(palindromes))
