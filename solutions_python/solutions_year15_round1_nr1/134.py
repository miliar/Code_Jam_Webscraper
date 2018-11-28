#!/usr/bin/python

import os
import sys
import itertools
import numpy as np

def solve(f, skip=False):

    if skip: return 0
    f.read_int()
    l = f.read_int_list()

    r1 = 0
    r2 = 0
    for i in xrange(1, len(l)):
        r1 += max([l[i-1]-l[i], 0])

    r2rate = max([max([l[i-1]-l[i] for i in xrange(1, len(l))]), 0])
    for i in xrange(1, len(l)):
        if l[i-1] < r2rate:
            r2 += l[i-1]
        else:
            r2 += r2rate

    return "%d %d"%(r1, r2)

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
        return map(int, self.f.readline().split())
    def read_float_list(self):
        self.linenum += 1
        return map(float, self.f.readline().split())
    def read_long_list(self):
        self.linenum += 1
        return map(long, self.f.readline().split())
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
