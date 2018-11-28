# -*- coding: utf-8 -*-
'''
'''

from collections import deque
#from decimal import Decimal
from sys import stdin, stderr
import copy
import fractions
import heapq
import itertools
import math
#import networkx as nx
import random
import re
import sys

sys.setrecursionlimit(100)

isa = isinstance
inf = 1 << 66

def next_one(i,j,A,B):
    if A[i] == B[j]:
        yield (i+1,j+1),0
        yield (i+1,j),1
        yield (i,j+1),1
    else:
        if i != 0 and j != 0:
            if A[i-1] == B[j]:
                yield (i,j+1),1
            if A[i] == B[j-1]:
                yield (i+1,j),1
        else:
            pass

def find(A,B):
    n = len(A); m = len(B)
    D = dict()
    D[0,0] = 0
    ans = inf
    while True:
        T = dict()
        for (i,j) in D:
            if i == n and j == m:
                ans = min(ans, D[i,j])
        if ans != inf:
            return ans
        for k in D:
            for (i,j),v in next_one(k[0],k[1],A,B):
                if i == n and j < m:
                    continue
                if i < n and j == m:
                    continue
                if (i,j) in T:
                    T[i,j] = min(T[i,j], D[k]+v)
                else:
                    T[i,j] = D[k]+v
        D = T
        if len(D) == 0:
            return inf
    assert(False)

def solve(A):
    n = len(A)
    ans = 0
    ans = max(ans, find(A[0],A[1]))
    return ans

def check_test(A, B, data='', case=[0]):
    print
    print "test %d:" % case[0]
    print A
#   if abs(A-B) > 1e-9:
    if A != B:
        if data:
            print data
        print '>>>', A
        print '<<<', B
        print "!!!!!!!! FAIL !!!!!!!!"
    else:
        print ":::::::) OK"
    case[0] += 1

def unit_test():
    print
    pass

def output(FH):
    for case in xrange(1, int(FH.next()) + 1):
        n = int(FH.next())
        A = list()
        for _ in range(n):
            a = FH.next().strip()
            A.append(a)
        # print >>stderr, '--', case
        # if case in [12]:
        #     print >>stderr, A
        #     break
        # print >>stderr, A
        ans = solve(A)
        print 'Case #%d:' % case, ans if ans < inf else "Fegla Won"
        # print >>stderr, 'Case #%d:' % case, ans

if __name__ == '__main__':
    # unit_test()
    # with open(foo) as stdin:
    output(stdin)
