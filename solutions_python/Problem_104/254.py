# -*- coding: utf-8 -*-
'''
Key Words:

Rules:

a set of positive integers S. 

Example:

Observations:

Goal:

find two non-empty, DISTINCT subsets with the same sum? 

Input:

Each test case begins with N, the number of positive integers 
in S. It is followed by N DISTINCT POSITIVE integers, all on
the same line. 

Limits

Each number in S will be a positive integer less than 1E5.

N is exactly equal to 500.

Output:

If there are two different subsets of S that have the same sum, 
then output these subsets, one per line. Each line should contain
the numbers in one subset, separated by spaces.

If it is impossible, then you should output the string
"Impossible" on a single line.

If there are multiple ways of choosing two subsets with the
same sum, any choice is acceptable. 
'''

from collections import deque
from decimal import Decimal
import copy
import fractions
import heapq
import itertools
import math
import random
import re
import sys

sys.setrecursionlimit(100)

stdin, stderr = sys.stdin, sys.stderr

INF = sys.maxint

def solve(A):
    S = dict()         
    S[0] = []
    def next_choice(S,k,a):
        C = k
        R = S[k]
        yield C,R      
        c,r = a,[a]
        yield c,r
        yield C+c,R+[a]
    while A:
        a = A.pop()
        T = dict()
        for k1 in S:
            for k2,v2 in next_choice(S,k1,a):
                if k2 in T:
                    if T[k2] != v2:
                        return T[k2], v2
                T[k2] = v2
        S = T
    return 'Impossible'

def check_test(A, B, case=[0]):
    print "test %d:" % case[0]
    print A
    if A != B:
        print '>>>', A
        print '<<<', B
        print "!!!!!!!! FAIL !!!!!!!!"
    else:
        print ":::::::) OK"
    case[0] += 1

def unit_test():
    print
    A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    print solve(A)
    
    A = [120,266,858,1243,1657,1771,2328,2490,2665,2894,3117,4210,4454,4943,5690,6170,7048,7125,9512,9600]
    print solve(A)

if __name__ == '__main__':
#    unit_test()

    for case in xrange(1, int(stdin.next()) + 1):
        A = [int(i) for i in stdin.next().strip().split()]
        # if case in [12]:
        #     print A
        #     break
        print 'Case #%d:' % case
        ans = solve(A[1:])
        if ans == 'Impossible':
            print ans
        else:
            for a in ans:
                print ' '.join([str(i) for i in a])

