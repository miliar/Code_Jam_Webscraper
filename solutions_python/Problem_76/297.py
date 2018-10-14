#!/usr/bin/python

import sys

# Read in input
num_problems = int(sys.stdin.readline())

for problem_number in range(1, num_problems + 1):
    num_candies = int(sys.stdin.readline())
    candies = [int(candy) for candy in sys.stdin.readline().split(' ')]

    print "Case #" + str(problem_number) + ": ",
    if reduce(lambda a, b: a ^ b, candies):
        print "NO"
    else:
        candies.remove(min(candies))
        print sum(candies)
        
    # Output template

