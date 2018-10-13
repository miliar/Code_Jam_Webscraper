#!/usr/bin/python

import sys
import math

# brute force method
with open(sys.argv[1]) as infile:
    cases = int(infile.readline().strip())
    for case in range(cases):
        values = infile.readline().split()
        count = 0
        for x in range(int(values[0]), int(values[1])+1):
            # if x is a palindrome
            if str(x) == str(x)[::-1]:
                root = math.sqrt(x)
                iroot = int(root)
                # if x is a square and our root is a palindrome, fair and square
                if root == iroot and str(iroot) == str(iroot)[::-1]:
                    count += 1
        print 'Case #%d: %d' % (case + 1, count)
