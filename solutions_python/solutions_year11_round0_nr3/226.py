#!/usr/bin/python
"""
The way Patrick is "adding" is using the XOR operator.

If Patrick is not crying, it means that for him both piles of candy have the
same value. Hence, if we add both piles using XOR, they will give 0 as a
result.

So if the sum of the numbers using XOR is 0, Sean simply gives the lowest
number to Patrick and keeps the rest for himself, because XOR has the
associative property. Otherwise, there is no solution.
"""

import sys

def xor_sum(a):
    s = 0
    for e in a:
        s = s^e
    return s

def solve(case):
    c = map(int, case.split())
    if xor_sum(c) != 0:
        return 'NO'
    else:
        return str(sum(c) - min(c))

def main(data = "C-example.in"):
    f = open(data, 'r')
    inp = map(lambda x: x[:-1], f.readlines())

    cases = inp[1:]
    i = 1
    j = 1
    while j < len(cases):
        print "Case #" + str(i) + ": " + solve(cases[j])
        j += 2
        i += 1

if len(sys.argv) == 2:
    main(sys.argv[1])
else:
    print sys.argv[0] + " <input file>"
