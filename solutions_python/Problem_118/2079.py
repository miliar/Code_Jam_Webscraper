#!/usr/bin/env python

import sys
import math


def is_palindrome(n):
    s = str(n)
    length = len(s)
    for i in xrange(0, int(length/2.0)):
        if not s[i] == s[length-1-i]:
            return False
    return True

f = open(sys.argv[1])

cases = int(f.readline())

for case in xrange(0, cases):
    r = f.readline().split(' ')
    low = int(r[0])
    high = int(r[1])

    count = 0
    for i in xrange(low, high + 1):
        square = math.sqrt(i)
        if not square == int(square):
            #print "%s is NOT a perfect square" % i
            continue  # Number isn't a perfect square

        if not is_palindrome(i):
            #print "%s is not a palindrome" % i
            continue

        if not is_palindrome(int(square)):
            #print "%s's square: %s is not a palindrome" % (i, square)
            continue

        count += 1

    print "Case #%s: %s" % (case + 1, count)
