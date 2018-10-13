#! /usr/bin/env python

#usage: cat input | this_program > output

import sys

num_testcases = int(sys.stdin.readline())

for case in range(1, num_testcases + 1):
    n = int(sys.stdin.readline())
    candies = map(int, sys.stdin.readline().split())
    cry = reduce(lambda x, y: x ^ y,candies, 0)
    if cry:
        result = 'NO'
    else:
        candies.sort()
        result = str(sum(candies[1:]))
    print "Case #%i: %s" %(case, result)
