#!/usr/bin/python

import os
import sys
import itertools
from math import sqrt, ceil
from fractions import gcd
import numpy as np


def pal(i):
    l = list(str(i))
    return l[:] == l[::-1]

def fs(l):
    l = np.array(l)
    return (l[:]*l[::-1]).sum()<10

def list2int(l):
    return long(''.join([str(item) for item in l]))


def insfig(org, ins):
    n = len(org)
    return org[:n/2] + ins + org[n/2:]

def make_fslist():
    l = [[] for i in xrange(51)]
    l[1] = [[1],[2],[3]]
    l[2] = [[1,1],[2,2]]

    lins1 = [[0],[1],[2]]
    lins2 = [[0,0],[1,1]]

    for i in xrange(2,50,2):
        for item in l[i]:
            for ins in lins1:
                new = insfig(item,ins)
                if fs(new): l[i+1].append(new)
            for ins in lins2:
                new = insfig(item,ins)
                if fs(new): l[i+2].append(new)

    fslist = []
    for line in l:
        for item in line:
            fslist.append(list2int(item)**2)

    return fslist


fslist = make_fslist()

def solve(f):
    a, b = f.read_long_list()

    return len([x for x in fslist if a <= x <= b])


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
    def read_long(self):
        self.linenum += 1
        return long(self.f.readline().strip())
    def read_str(self):
        self.linenum += 1
        return self.f.readline().strip()

    def read_int_list(self):
        self.linenum += 1
        return [int(item) for item in self.f.readline().split()]
    def read_float_list(self):
        self.linenum += 1
        return [float(item) for item in self.f.readline().split()]
    def read_long_list(self):
        self.linenum += 1
        return [long(item) for item in self.f.readline().split()]
    def read_str_list(self):
        self.linenum += 1
        return self.f.readline().split()

if __name__ == '__main__':
    filename = sys.argv[1]
    cnum = int(sys.argv[2]) if len(sys.argv) > 2 else None
    output = filename[:-3]+'.out' if filename[-3:] == '.in' else filename+'.out'
    f = Reader(filename)
    g = open(output, 'w')
    cases = f.read_int()
    for case in xrange(cases):
        if cnum == case+1: print 'line: %d'%f.linenum
        line = 'Case #%d: %s\n'%(case+1,str(solve(f)))
        g.write(line)
        if not cnum or cnum == case+1: print line,
