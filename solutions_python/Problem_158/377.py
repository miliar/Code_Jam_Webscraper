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

def solve(x,r,c):
    D = dict()
    D[4,4,4] = 'L'
    D[4,3,4] = 'L'
    D[4,2,4] = 'W'
    D[4,1,4] = 'W'

    D[3,4,4] = 'W'
    D[3,3,4] = 'L'
    D[3,2,4] = 'W'
    D[3,1,4] = 'W'

    D[3,3,3] = 'L'
    D[3,2,3] = 'L'
    D[3,1,3] = 'W'

    D[2,4,4] = 'L'
    D[2,3,4] = 'L'
    D[2,2,4] = 'L'
    D[2,1,4] = 'L'

    D[2,3,3] = 'W'
    D[2,2,3] = 'L'
    D[2,1,3] = 'W'

    D[2,2,2] = 'L'
    D[2,1,2] = 'L'

    if r > c:
        r,c = c,r
    if x == 1:
        return 'L'
    if (x,r,c) in D:
        return D[x,r,c]
    else:
        return 'W'

def output():
    for case in xrange(1, int(stdin.next()) + 1):
        x,r,c = [ int(a) for a in stdin.next().strip().split() ]
        ans = 'RICHARD' if solve(x,r,c) == 'W' else 'GABRIEL'
        print 'Case #%d:' % case, ans
        print >>stderr, 'Case #%d:' % case, ans


#if __name__ == '__main__':
# unit_test()
output()
