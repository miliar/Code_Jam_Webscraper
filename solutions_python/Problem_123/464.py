#!/usr/bin/env python

import itertools
import os.path as path
from collections import namedtuple, Counter
import pprint
import math
import numpy as np  # http://www.numpy.org/

def solve(A, N, motes):
    motes.sort()

    ca = A
    on = 0
    cand = [1e+100]
    for i, m in enumerate(motes):
        ##print cand, ca, m
        if ca <= m:
            cand += [on + len(motes[i:])]
            if ca - 1 < 1:
                on = 1e+100
                continue
            while ca <= m:
                ca += ca - 1
                on += 1
            ca += m
        else:
            ca += m
    cand += [on]
    return min(cand)

if __name__ == '__main__':
    ans = []
    T = int(raw_input())

    for i in xrange(T):
        A, N = map(int, raw_input().strip().split())
        motes = map(int, raw_input().strip().split())
        print 'Case #%d:'%(i+1), solve(A, N, motes)