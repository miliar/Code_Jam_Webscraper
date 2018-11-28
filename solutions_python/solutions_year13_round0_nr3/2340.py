#!/usr/bin/env python

import sys
import math

def IsPalindrome(n):
    s = str(n)
    return(s == s[::-1])

def Solve(no):
    lo, hi = map(int, sys.stdin.readline().split())
    #print lo, hi
    count = 0
    # apenas numeros terminados em [0, 1, 5] tem quadrados palindromos
    low = int(math.sqrt(lo))
    high = int(math.sqrt(hi)) + 1
    for n in xrange(lo, hi + 1):
        if IsPalindrome(n):
            m = int(math.sqrt(n))
            if (n == (m * m)) and IsPalindrome(m):
                count += 1
                #print n
    print "Case #%d: %d" % (no, count)

#lo = 1
#hi = 1000000
#count = len(filter(IsPalindrome, xrange(1, 10000000)))
#print "[%d, %d]: %d" % (lo, hi, count)
#exit()

T = int(sys.stdin.readline())
for no in range(1, T+1):
    Solve(no)

