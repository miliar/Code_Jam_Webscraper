#!/usr/bin/env python
NUM_OF_ELEMENTS_PER_PROBLEM = 1

import math

def isFair(n):
    n_str = str(n)
    reverse = n_str[::-1]
    return n_str == reverse

def isSquare(n):
    sq = math.sqrt(n)
    if(sq == int(sq)):
        return isFair(int(sq))
    else:
        return False

def solve(probleminput):
    """
    in: expects a list of inputs for the current testcase. see NUM_OF_ELEMENTS_PER_PROBLEM for the list size
    out: should return the solution for this testcase
    """
    (lower_bound,upper_bound) = probleminput[0].split(' ')

    result = 0
    for n in xrange(int(lower_bound),int(upper_bound)+1):
        if isFair(n) and isSquare(n):
            result += 1
        
    return str(result)

###### program skeleton #######
import sys
problem = [l.replace('\n', '') for l in sys.stdin.readlines()]
for testcase in xrange(1, int(problem[0]) + 1):
    begin = 1 + (testcase - 1) * NUM_OF_ELEMENTS_PER_PROBLEM
    result = solve(problem[begin:begin + NUM_OF_ELEMENTS_PER_PROBLEM])
    print "Case #%i: %s" % (testcase, result)
