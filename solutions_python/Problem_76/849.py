#coding: 1251
#####################################################

from __future__ import division

import os
import sys
import operator
import string
import re
import time

from os.path import splitext
from copy import copy

from math import *
from operator import *
from collections import *
from itertools import *
from functools import *

#####################################################

try:
    from do import report_working_on
except ImportError:
    report_working_on = lambda a,b: None

if sys.argv:
    fin = file(sys.argv[1], 'r')
    fout = file(splitext(sys.argv[1])[0]+'.out', 'w+')
else:
    fin = sys.stdin
    fout = sys.stdout

def dorun():
    cases = int(fin.next())
    for case in xrange(cases):
        report_working_on(case, cases)
        print>>fout, 'Case #%d: %s' % ( 1+case, solve(fin) )
    else:
        report_working_on(0,0)

#####################################################

class piece(object):
    def __init__(self, n):
        self.patric = n
        self.sean = n
        self.makebits()

    def makebits(self):
        bits = ['1' if self.patric & (1 << n) else '0' for n in xrange(21)]
        self.bits = ''.join(bits)

    @staticmethod
    def add(lhs, rhs):
        self = piece(lhs.sean + rhs.sean)
        self.patric= lhs.patric ^ rhs.patric
        self.makebits
        return self

def subsolve(pieces):
    def combs(pieces):
        size = len(pieces)
        for N in xrange(1, 1+size//2):
            for c in combinations(pieces, N):
                yield c

    best =-1
    for p1 in combs(pieces):
        p2 = [x for x in pieces if x not in p1]

        n1 = reduce(piece.add, p1)
        n2 = reduce(piece.add, p2)
        if n1.patric == n2.patric:
            best = max(best, n1.sean, n2.sean)

    return best

def solve(fin):
    N = int(fin.next())
    CS = map(int, fin.next().split())

    pieces = [piece(n) for n in CS]
    for i in xrange(20):
        if sum(1 for p in pieces if p.bits[i]=='1') % 2 == 1:
            big = -1
            break;
    else:
        big = subsolve(pieces)

    return big if big >=0 else 'NO'


#####################################################

if __name__=='__main__': dorun()
