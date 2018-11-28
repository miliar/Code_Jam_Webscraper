#!/usr/bin/python

import os
import sys
import re
import itertools
import collections
import copy
import fractions
import bisect
import decimal
import math
import random
from fractions import Fraction

# decimal.getcontext().prec = 50
# sys.setrecursionlimit(10000)

def solve(f, skip=False):
    n, p = f.read_int_list()
    r = f.read_int_list()
    q = [f.read_int_list() for _ in xrange(n)]
    if skip: return 0

    qr = [[] for _ in xrange(n)]
    for i in xrange(n):
        for j in xrange(p):
            mi = int(math.ceil(q[i][j]*10.0/(r[i]*11)))
            ma = q[i][j]*10/(r[i]*9)
            if mi > ma: continue
            qr[i].append((mi, ma))

    for i in xrange(n):
        qr[i].sort()

    ans = 0
    while all([len(i) > 0 for i in qr]):
        a = [item[0][1] for item in qr]
        i = a.index(min(a))
        if all([ i == j or qr[j][0][0] <= qr[i][0][1] for j in xrange(n)]):
            ans += 1
            for ii in xrange(n):
                qr[ii].pop(0)
        else:
            qr[i].pop(0)

    return ans

class Reader(object):
    def __init__(self, filename):
        self.f = open(filename)
        self.linenum = 1

    def read_int(self):
        self.linenum += 1
        return int(self.f.readline().strip())
    def read_float(self):
        self.linenum += 1
        return float(self.f.readline().strip())
    def read_decimal(self):
        self.linenum += 1
        return decimal.Decimal(self.f.readline().strip())
    def read_str(self):
        self.linenum += 1
        return self.f.readline().strip()

    def read_int_list(self):
        self.linenum += 1
        return map(int, self.f.readline().split())
    def read_float_list(self):
        self.linenum += 1
        return map(float, self.f.readline().split())
    def read_decimal_list(self):
        self.linenum += 1
        return map(decimal.Decimal, self.f.readline().split())
    def read_str_list(self):
        self.linenum += 1
        return self.f.readline().split()

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else sys.argv[0].replace('.py', '-sample.in')
    cnum = int(sys.argv[2]) if len(sys.argv) > 2 else None
    output = filename[:-3]+'.out' if filename[-3:] == '.in' else filename+'.out'
    f = Reader(filename)
    cases = f.read_int()

    if cnum:
        for case in xrange(cases):
            if cnum == case+1:
                print '(line: %d) '%f.linenum
                line = 'Case #%d: %s\n'%(case+1,str(solve(f)))
                print line,
            else:
                solve(f, skip=True)
    else:
        g = open(output, 'w')
        for case in xrange(cases):
            line = 'Case #%d: %s\n'%(case+1,str(solve(f)))
            g.write(line)
            print line,
