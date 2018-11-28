#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import numpy as np
import sys
import copy
from heapq import *
import itertools as it
import re
import collections as co

def rint():
    return map(int, raw_input().split())

def rstr():
    return raw_input().split()

def rlist(*lfn):
    return  [f(a) for (f, a) in zip(lfn, raw_input().split())]

def fact(n):
    p = 1
    for i in xrange(1, n+1):
        p *= i
    return p

def rec_st(first, on_generate, on_execute):
    S = [(0, f) for f in first]
    while S:
        (k, cont) = S.pop()
        if k == 0:
            S.append((1, cont))
            for u in on_generate(cont):
                S.append((0, u))
        else:
            on_execute(cont)

def rec_q(first, on_generate):
    Q = co.deque(first)
    while Q:
        cont = Q.pop_left()
        for u in on_generate(cont):
            Q.append(u)

if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(testcases):
        [R, C] = rint()
        A = [raw_input() for _ in xrange(R)]
        D = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        K = {}
        K['.'] = (0,0)
        K['<'] = (0, -1)
        K['^'] = (-1, 0)
        K['v'] = (1, 0)
        K['>'] = (0, 1)

        def rin(r, c):
            return 0 <= r < R and 0 <= c < C
        cnt = 0
        imp = False
        for r in xrange(R):
            for c in xrange(C):
                if A[r][c] == '.':
                    continue
#                print (r, c)
                M = set([])
                for d in D:
#                    print 'd', d
                    rr, cc = r, c
                    m = False
                    while True:
                        rr += d[0]
                        cc += d[1]
#                        print ":", (rr, cc)
                        if not rin(rr, cc):
                            break
#                        print (rr, cc), A[rr][cc]
                        if A[rr][cc] != '.':
#                            print 'found'
                            m = True
                            break
                    if m: M.add(d)
#                print M
                if not (K[A[r][c]] in M):
                    if M:
                        cnt += 1
                    else:
                        imp = True

        T = 'IMPOSSIBLE' if imp else str(cnt)
        print("Case #%i: %s" % (caseNr + 1, T))
#        print("Case #%i:" % (caseNr + 1))
