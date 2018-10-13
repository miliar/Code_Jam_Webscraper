#-*- coding: utf-8 -*-

import os
import sys
import time
import math
import itertools

def solve(f):
    C, F, X = f.read_float_list()

    n = max(0,int((F*X-C*(2.0+F))/(C*F)))
    time = min([ sum([C/(2.0+fnum*F) for fnum in xrange(farms)]) + X/(2+farms*F)
                 for farms in xrange(n,n+2)])


    return '%.7f'%time

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
