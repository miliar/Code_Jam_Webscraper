#!/usr/bin/env python

from __future__ import division

import collections
import itertools
import sys

class gcj:
    IN = sys.stdin
    number = 0

    @classmethod
    def case(cls):
        cls.number += 1
        return 'Case #%d:' % cls.number

    @classmethod
    def line(cls, type=str):
        line = cls.IN.readline()
        return type(line.strip('\n'))

    @classmethod
    def splitline(cls, type=str):
        line = cls.IN.readline()
        return [type(x) for x in line.split()]

def solve():
    return 0

def go():
    t = gcj.line(int)
    for _ in xrange(t):
        n = gcj.line(int)
        A = list()
        B = list()
        for _ in xrange(n):
            a, b = gcj.splitline(int)
            A.append(a)
            B.append(b)
        cross = 0
        for i in xrange(n):
            a = A[i]
            b = B[i]
            for j in xrange(i, n):
                if A[j] > a and B[j] < b:
                    cross += 1
                if A[j] < a and B[j] > b:
                    cross += 1                    
        print gcj.case(), cross

go()
