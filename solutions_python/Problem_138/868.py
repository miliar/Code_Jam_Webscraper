#! /usr/bin/env python

from sys import stdin
import numpy as np
from bisect import bisect

ntest = input()

for test in xrange(ntest):
    n = input()
    y = 0
    z = 0
    naomi = sorted([float(i) for i in stdin.readline().strip().split(' ')])
    ken = sorted([float(i) for i in stdin.readline().strip().split(' ')])
    ken2 = ken[:]
    for chosen_n in naomi:
        min_k = ken[0]
        if chosen_n > min_k:
            ken.pop(0)
            y += 1
        else:
            ken.pop()
    ken = ken2
    for chosen_n in naomi:
        k = bisect(ken, chosen_n) % len(ken)
        chosen_k = ken.pop(k)
        if chosen_n > chosen_k:
            z += 1

    print "Case #{}: {} {}".format(test+1, y, z)