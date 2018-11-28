#!/usr/bin/env python3

from functools import reduce

t = int(input())
for i in range(t):
        n = int(input())
        c = [int(a) for a in input().split()]
        res = 'NO'
        if not reduce(lambda x, y: x^y, c):
                res = sum(sorted(c)[1:])
                                
        print("Case #{0}: {1}".format(i+1, res))
