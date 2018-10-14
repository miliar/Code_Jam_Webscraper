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

def next_one(key,chest,C):
    keytype = set(key)
    n = len(chest)
    for i in range(n):
        c = chest[i]
        k = C[c][0]
        if k in keytype:        # k can open c
            K = list(key)
            K.remove(k)
            X = chest[:i] + chest[i+1:]
            free = False
            for newkey in C[c][1]:
                K.append(newkey)
                if k == newkey:
                    free = True
            K = tuple(sorted(K))
            yield (K,X),(c,)
            if free:
                break

def solve(K,C):
    n = len(C)
    X = tuple(range(n))
    D = dict()
    D[tuple(K),X] = ()
    ans = None
    for _ in range(n):
        T = dict()
        for k in D:
            key,chest = k
            for kk,v in next_one(key,chest,C):
                if kk in T:
                    T[kk] = min(T[kk],D[k]+v)
                else:
                    T[kk] = D[k]+v
        D = T
        # print '--',
        # for k in T:
        #     print k,T[k]
        # print '<<'
    ans = 'IMPOSSIBLE'
    if D:
        for k in D:
            L = []
            for i in D[k]:
                L.append(i+1)   # convert to 1 based
            ans = tuple(L)      # there can be only 1 k in D
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
    K,N = 1,4
    key = (1,)
    C = ((1,()), (1,(1,3)), (2,()), (3,(2,)))
    ans = (2,1,4,3)
    check_test(solve(key,C), ans, (key,C))

    K,N = 3,3
    key = (1,1,1)
    C = ((1,()), (1,()), (1,()))
    ans = (1,2,3)
    check_test(solve(key,C), ans, (key,C))

    K,N = 1,1
    key = (2,)
    C = ((1,(1,)),)
    ans = 'IMPOSSIBLE'
    check_test(solve(key,C), ans, (key,C))

def output():
    for case in xrange(1, int(stdin.next()) + 1):
        _,N = [int(i) for i in stdin.next().split()]
        K = [int(i) for i in stdin.next().split()]
        C = []
        for _ in range(N):
            A = [int(i) for i in stdin.next().split()]
            t = A[0]
            k = A[2:]
            C.append((t,k))
        ans = solve(K,C)
        if isa(ans,tuple):
            ans = ' '.join([str(i) for i in ans])
        print 'Case #%d:' % case, ans
        print >>stderr, 'Case #%d:' % case, ans

if __name__ == '__main__':
#    unit_test()
    output()
