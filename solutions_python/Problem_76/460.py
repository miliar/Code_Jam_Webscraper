#!/usr/bin/env python

from sys import stdin, stdout
from operator import add, xor

lines = stdin.readlines()
T = int(lines[0])
lines = lines[1:]
for t in range(0,T):
    N = int(lines[2*t])
    candy = [int(s) for s in lines[2*t+1].split()]
    result = "NO"
    if 0 == reduce(xor, candy[1:], candy[0]):
        result  = reduce(add, candy[1:], candy[0]) - min(candy)
    print "Case #{0}: {1}".format(t+1, result)
    
