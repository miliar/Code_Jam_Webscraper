#!/usr/bin/python2 
from __future__ import print_function
import math
import itertools

def xor(a,b):
    return a^b
def sum(a,b):
    return a+b

def rfl(l, c):
    x = list(l)
    for a in c:
        x.remove(a)

    return tuple(x)

with open("input.txt") as f:
    lines = f.readlines()
    lines.pop(0)
    lines = lines[1::2]
    n_line = 0

    for line in lines:
        n_line += 1

        candies = line.split()
        candies = [int(c) for c in candies]
        candies = tuple(candies)

        combinations = []
        for n in xrange(1,(len(candies) / 2) + 1):
            combinations.extend(list(itertools.combinations(candies, n)))

        n_combinations = [(x,rfl(candies, x)) for x in combinations]

        maxi = 0
        for combination in n_combinations:
            a = reduce(xor, combination[0])
            b = reduce(xor, combination[1])
            if (a == b):
                sum_a = reduce(sum, sorted(combination[0]))
                sum_b = reduce(sum, sorted(combination[1]))
                maxi = max(sum_a, sum_b, maxi)

        if maxi > 0:
            print("Case #%d: %d" % (n_line, maxi))
        else:
            print("Case #%d: NO" % (n_line))
