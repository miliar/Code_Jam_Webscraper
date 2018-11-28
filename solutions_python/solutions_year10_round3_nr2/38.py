#!/usr/bin/env python

from __future__ import division

import collections
import itertools
import sys
import math

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
    res = list()
    res.append(1)
    for i in xrange(0, 1000):
        res.append(res[i] * 2)
    for _ in xrange(t):
        l, p, c = gcj.splitline(int)
        for i in xrange(1000):
            l = l * c
            if l >= p:
                break
        for r in xrange(0, 1000):
            if res[r] > i:
                break
        print gcj.case(), r

go()
