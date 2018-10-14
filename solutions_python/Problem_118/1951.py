#!/usr/bin/env python3

import sys, math

def isPalindrome (n):
    s = str (n)
    l = len (s)
    print ("Checking if {0} is a palindrome".format (s), file=sys.stderr)
    for i in range (int (l / 2)):
        if s [i] != s [l - i - 1]:
            return False

    print ("yes", file=sys.stderr)
    return True

cases = int (input ())
def answer():
    numbers = input ().split (' ')
    A = int (numbers [0])
    B = int (numbers [1])

    print ("A is {0} and B is {1}".format (A, B), file=sys.stderr)

    start = max (int (math.sqrt (A)) - 2, 1)
    end = int (math.sqrt (B))
    count = 0

    for i in range (start, end + 2):
        n = i ** 2
        if n >= A and n <= B:
            if isPalindrome (n) and isPalindrome (i):
                count = count + 1

    return count

for i in range (cases):
    print ("Case #{0}: {1}".format (i + 1, answer ()))
