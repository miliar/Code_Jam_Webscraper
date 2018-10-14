#!/usr/bin/python

import sys
import math

def isPalindrome (X):
    x = str(X)
    l = len(x)
    for i in range(l/2):
        if x[i] != x[l-i-1]:
            return False
    return True

T = int(sys.stdin.readline().strip())
for case in xrange(1,T+1):
    (A,B) = map (int, sys.stdin.readline().strip().split())
    a = int(math.ceil(math.sqrt(A)))
    b = int(math.floor(math.sqrt(B)))
    count = 0
    for i in xrange(a,b+1):
        if isPalindrome(i):
            if isPalindrome(i*i):
                count = count + 1
                #print "SquarePalindrome found:", i*i , "(", i, ")"
    print "Case #" + str(case) + ": " + str(count)
