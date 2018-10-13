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
INF = 1 << 66

def solve(A):
    n = len(A)
    m = len(A[0])
    D = dict()
    for i in range(n):          # gether the height info
        for j in range(m):
            k = A[i][j]
            D.setdefault(k,[]).append((i,j))
    R = set()                   # row fixed
    C = set()                   # col fixed
    # cut from the highest to lowest
    for k in sorted(D,reverse=True):
        r = set()
        c = set()
        for i,j in D[k]:        # cut to to height k
            if i in R and j in C:
                return 'NO'     # no option left
            r.add(i)
            c.add(j)
        R |= r
        C |= c
    return 'YES'

def check_test(A, B, data='', case=[0]):
    print
    print "test %d:" % case[0]
    print A
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
    A, ans = ((2,1,2),
              (1,1,1),
              (2,1,2),), 'YES'
    check_test(solve(A), ans, A)

    A, ans = ((2,2,2,2,2),
              (2,1,1,1,2),
              (2,1,2,1,2),
              (2,1,1,1,2),
              (2,2,2,2,2),), 'NO'
    check_test(solve(A), ans, A)

    A, ans = ((1,2,1),), 'YES'
    check_test(solve(A), ans, A)

def output():
    for case in xrange(1, int(stdin.next()) + 1):
        N,M = [int(i) for i in stdin.next().split()]
        A = []
        for _ in range(N):
            a = [int(i) for i in stdin.next().split()]
            A.append(a)
        ans = solve(A)
        print 'Case #%d:' % case, ans
        print >>stderr, 'Case #%d:' % case, ans

if __name__ == '__main__':
#    unit_test()
    output()
