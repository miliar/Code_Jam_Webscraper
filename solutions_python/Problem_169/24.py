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
def rfloat():
    return map(float, raw_input().split())

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
        [N, V, X] = rstr()
        N = int(N)
        V = float(V)
        X = float(X)
        A = sorted([list(reversed(rfloat())) for _ in xrange(N)])
        B = list(reversed(A))
        def fl(T, U):
            [C, R] = zip(*U)
            i = 0
            W = 0
            Y = 0
            while i < N:
                dV = T * R[i]
                if W + dV <= V:
                    W += dV 
                else:
                    dV = V - W
                    W = V
                Y += C[i] * dV
                if W == V:
                    break
                i += 1
            assert W <= V
#            print 'W', W, V, V - W, V == W
            if W < V:
                return None
            return Y / V

        def ts(T):
            mi, ma = fl(T, A), fl(T, B)
            if mi == None or ma == None:
                assert mi == None and ma == None
                return False
            if mi * (1 - 1e-14) <= X <= ma * (1 + 1e-14):
                return True
            return False

        def bs(lo, hi):
#            print (lo, hi, mid)
            while hi - lo > 1e-10 and (hi - lo) / (hi + lo) > 1e-10:
                mid =  (hi + lo) / 2.0
#                print lo, hi
                if ts(mid):
                    hi = mid
                else:
                    lo = mid
            return (hi + lo) / 2.0
#        print A
#        print B
        if A[0][0] <= X <= B[0][0]:
            Tmax = max(V / A[0][1], V / B[0][1]) * 2.1
            F = bs(0, Tmax)
            print("Case #%i: %.8lf" % (caseNr + 1, F))
        else:
            print("Case #%i: IMPOSSIBLE" % (caseNr + 1))
#        print("Case #%i:" % (caseNr + 1))
