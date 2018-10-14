#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    d, n = input().strip().split()
    d = int(d)
    n = int(n)
    t = 0
    for i in range(n):
        k, v = input().strip().split()
        k = int(k)
        v = int(v)
        t_i = (d - k) / v
        if t_i > t:
            t = t_i
    v = d / t
    print("Case #" + str(a0+1) + ": " + "{0:.6f}".format(v))