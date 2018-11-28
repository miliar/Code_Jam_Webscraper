#!/usr/bin/python

from operator import xor

def solve(candy):
    if reduce(xor, candy, 0):
        return 'NO'
    return sum(candy) - min(candy)

T = int(raw_input())
for i in range(T):
    raw_input()
    print "Case #%i: %s" % (i+1, solve(map(int, raw_input().split(' '))))

