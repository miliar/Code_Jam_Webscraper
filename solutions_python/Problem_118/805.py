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

def is_palindrome(A):
    A = str(A)
    i,j = 0,len(A)-1
    while i <= j:
        if A[i] != A[j]:
            return False
        i += 1
        j -= 1
    return True

def is_square_palindrome(A):
    r = int(math.sqrt(A))
    if r*r == A:
        if is_palindrome(r):
            return True
    return False
    
def palindrome(N):              # generate palindrome up to N digits
    if N == 1:
        for i in range(10):
            yield i
    elif N == 2:
        for i in range(10) + [11,22,33,44,55,66,77,88,99]:
            yield i
    else:
        for p in palindrome(2):
            yield p
        A,B = range(1,10), [11,22,33,44,55,66,77,88,99] 
        n = 3                   # number of digit to generate
        while n <= N:
            for i in range(1,10):
                p = i * 10**(n-1) + i   # i0..0i case
                yield p
            C = []
            for i in range(1,10):
                for j in A:
                    p = i * 10**(n-1) + j * 10 + i
                    yield p
                    C.append(p)
            A,B = B,C
            n += 1

def solve(A,B):
    n = len(str(B))
    ans = 0
    for p in palindrome(n+1):
        if A <= p <= B:
            if is_square_palindrome(p):
                ans += 1
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
    A,B, ans = 1,4, 2
    check_test(solve(A,B), ans, (A,B))

    A,B, ans = 10,120, 0
    check_test(solve(A,B), ans, (A,B))

    A,B, ans = 100,1000, 2
    check_test(solve(A,B), ans, (A,B))

def output():
    for case in xrange(1, int(stdin.next()) + 1):
        A,B = [int(i) for i in stdin.next().split()]
        ans = solve(A,B)
        print 'Case #%d:' % case, ans
        print >>stderr, 'Case #%d:' % case, ans

if __name__ == '__main__':
#    unit_test()
    output()
