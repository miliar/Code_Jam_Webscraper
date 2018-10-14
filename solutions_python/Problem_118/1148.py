#!/usr/bin/env python2

import sys
import math

def intervals(filename):
    with open(filename) as f:
        cases = int(f.readline())
        intervals = [map(int, ival.split()) for ival in f.read().strip().split('\n')]
    return intervals

def is_palindrome(x):
    return str(x) == str(x)[::-1]

cache = {}
def is_fair_and_square(x):
    if x not in cache:
        cache[x] = is_palindrome(x) and is_palindrome(x * x)
    return cache[x]

def fair_and_square(a, b):
    num_fair_and_square = 0
    xmin, xmax = int(round(math.sqrt(a))), int(round(math.sqrt(b)))
    for x in xrange(xmin, xmax+1):
        if is_fair_and_square(x) and a <= x * x <= b:
            num_fair_and_square += 1
    return num_fair_and_square

filename = sys.argv[1]
for case, interval in enumerate(intervals(filename), 1):
    nums = fair_and_square(*interval)
    print 'Case #{0}: {1}'.format(case, nums)
