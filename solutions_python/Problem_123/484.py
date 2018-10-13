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
INF = 1 << 66

def is_yes(x,i,k,B):
    p = math.pow(2,x)
    V = p*k-(p-1)
    return V > B[i]

def first_yes(lo,hi,i,k,B):
    while lo < hi:
        mid = lo + (hi-lo)/2
        if is_yes(mid,i,k,B):
            hi = mid
        else:
            lo = mid + 1
    if is_yes(lo,i,k,B) is False:
#        print lo,i,k,B[i]
        assert(False)
    return lo

def next_one(i,k,B):
    if k > B[i]:
        yield k+B[i],0
    else:
        yield k,1
        if k > 1:
            lo = 1
            hi = 66
            N = first_yes(lo,hi,i,k,B)
            p = math.pow(2,N)
            kk = p*k-(p-1) + B[i]
            yield kk,N

def solve(A,B):
    B = sorted(B)
    n = len(B)
    D = dict()
    D[A] = 0
    for i in xrange(n):
#        print '--',i
        # for k in sorted(D):
        #     print k,D[k]
        T = dict()
        for k in D:
            for kk,v in next_one(i,k,B):
                if kk in T:
                    T[kk] = min(T[kk],D[k]+v)
                else:
                    T[kk] = D[k]+v
        D = T
    ans = min(D.values())
    return ans

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
    print
    A,B, ans = 2,(2,1), 0
    check_test(solve(A,B), ans, (A,B))

    A,B, ans = 2,(2,1,1,6), 1
    check_test(solve(A,B), ans, (A,B))

    A,B, ans = 10,(25,20,9,100), 2
    check_test(solve(A,B), ans, (A,B))

    A,B, ans = 1,(1,1,1,1), 4
    check_test(solve(A,B), ans, (A,B))

    A,B, ans = 1,[100, 100, 100, 100, 100, 100, 100, 100, 100, 100], 10
    check_test(solve(A,B), ans, (A,B))

    A,B,ans = 15, [34, 41] , 2
    check_test(solve(A,B), ans, (A,B))

    A,B, ans = 10, [9, 20, 25, 100], 2
    check_test(solve(A,B), ans, (A,B))


def output():
    for case in xrange(1, int(stdin.next()) + 1):
        A,_ = [int(i) for i in stdin.next().strip().split()]
        B = [int(i) for i in stdin.next().strip().split()]
        print >>stderr, '--', case
        print >>stderr, A
        print >>stderr, sorted(B), "\n"
        ans = solve(A,B)
        print 'Case #%d:' % case, ans
        print >>stderr, 'Case #%d:' % case, ans

if __name__ == '__main__':
#    unit_test()
    output()
