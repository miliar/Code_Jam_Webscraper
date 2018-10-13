# -*- coding: utf-8 -*-
'''
Problem B. Infinite House of Pancakes

Small input
9 points

Large input
12 points

At the Infinite House of Pancakes, there are only finitely many
pancakes, but there are infinitely many diners who would be willing to
eat them! When the restaurant opens for breakfast, among the
infinitely many diners, exactly D have non-empty plates; the ith of
these has Pi pancakes on his or her plate. Everyone else has an empty
plate.

Normally, every minute, every diner with a non-empty plate will eat one
pancake from his or her plate. However, some minutes may be special.
In a special minute, the head server asks for the diners' attention,
chooses a diner with a non-empty plate, and carefully lifts some number
of pancakes off of that diner's plate and moves those pancakes onto one
other diner's (empty or non-empty) plate. No diners eat during a
special minute, because it would be rude.

You are the head server on duty this morning, and it is your job to
decide which minutes, if any, will be special, and which pancakes will
move where. That is, every minute, you can decide to either do nothing
and let the diners eat, or declare a special minute and interrupt the
diners to make a single movement of one or more pancakes, as described
above.

Breakfast ends when there are no more pancakes left to eat. How
quickly can you make that happen?

Input

The first line of the input gives the number of test cases, T. T test
cases follow. Each consists of one line with D, the number of diners
with non-empty plates, followed by another line with D space-separated
integers representing the numbers of pancakes on those diners' plates.

Output

For each test case, output one line containing "Case #x: y", where x
is the test case number (starting from 1) and y is the smallest number
of minutes needed to finish the breakfast.

Limits

1 ≤ T ≤ 100.
Small dataset

1 ≤ D ≤ 6.
1 ≤ Pi ≤ 9.
Large dataset

1 ≤ D ≤ 1000.
1 ≤ Pi ≤ 1000.
Sample

Input

3
1
3
4
1 2 1 2
1
4

Output

Case #1: 3
Case #2: 2
Case #3: 3
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

def next_one(A):
    A = tuple([ a for a in A if a > 0 ])
    B = [ a-1 for a in A ]
    B = [ b for b in B if b > 0 ]
    B = sorted(B)
    yield tuple(B)
    n = len(A)
    for i in range(n):
        for j in range(1,A[i]):
            B = list(A)
            B[i] = A[i] - j
            B.append(j)
            B = sorted(B)
            yield tuple(B)

def solve(A):
    D = dict()
    D[tuple(A)] = 0
    for _ in range(1005):
        T = dict()
        # for x in D:
        #     print x,D[x]
        for x in D:
            if len(x) == 0:
                return D[x];
            for y in next_one(x):
                if y in T:
                    T[y] = min(T[y], D[x]+1)
                else:
                    T[y] = D[x]+1;
        D = T
    assert(False)

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
    A, ans = (9,), 5
    check_test(solve(A), ans, A)

    # A, ans = (3,), 3
    # check_test(solve(A), ans, A)

    # A, ans = (1,2,1,2), 2
    # check_test(solve(A), ans, A)

    # A, ans = (4,), 3
    # check_test(solve(A), ans, A)

def output():
    for case in xrange(1, int(stdin.next()) + 1):
        D = int(stdin.next().strip())
        A = [ int(a) for a in stdin.next().strip().split() ]

        # print >>stderr, '--', case
        # if case in [62]:
        #     print >>stderr, A
        #     break
        # print >>stderr, A

        ans = solve(A)
        print 'Case #%d:' % case, ans
        print >>stderr, 'Case #%d:' % case, ans

#if __name__ == '__main__':
# unit_test()
output()
