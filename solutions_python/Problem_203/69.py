# Vladimir Burian, 2017 (vladaburian@gmail.com)

import string
import sys
import math
from itertools import *
import operator
from collections import Counter
import copy

class Tee:
    def __init__(self, ofile):
        self.file = ofile

    def write(self, ostr):
        sys.stdout.write(ostr)
        self.file.write(ostr)

    def close(self):
        self.file.close()

def read_int(fin):
    return int(fin.readline())

def read_ints(fin):
    return [int(x) for x in fin.readline().split()]

###############################################################################

def solve(fin):
    R,C = read_ints(fin)
    g = [[x for x in fin.readline().strip()] for _ in xrange(R)]
    
    for y in xrange(R):
        ch = g[y][0]
        isempty = True
        
        for x in xrange(C):
            if g[y][x] <> "?":
                isempty = False
                ch = g[y][x]
                break

        if isempty:
            continue
        
        for x in xrange(C):
            if g[y][x] == "?":
                g[y][x] = ch
            else:
                ch = g[y][x]

    for y in xrange(1,R):
        if g[y][0] == "?":
            g[y] = copy.copy(g[y-1])

    for y in reversed(xrange(0,R-1)):
        if g[y][0] == "?":
            g[y] = copy.copy(g[y+1])
    
    r = "\n".join(["".join(row) for row in g])
    return r

###############################################################################

name = "test"
name = "A-small-attempt0"
name = "A-large"

sys.setrecursionlimit(5000)

fin = open(name+".in", "r")
fout = open(name+".out", "w")
fout = Tee(fout)

T = int(fin.readline())

for t in range(1,T+1):
    r = solve(fin);
    print >> fout, "Case #{}:\n{}".format(t, r)
    sys.stdout.flush()

fout.close()

print "=== DONE ==="

