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
    i = fin.readline().split();
    
    s = list(iter(i[0]))
    k = int(i[1])
    
    # left / right indexes
    l = 0
    r = len(s) - 1

    # flips
    f = 0

    while True:    
        while (0 <= l < len(s)) and s[l] == '+':
            l += 1
        
        while (0 <= r < len(s)) and s[r] == '+':
            r -= 1
        
        if l > r:
            return f
    
        if (r-l+1) < k:
            return "IMPOSSIBLE"
    
        f += 1
    
        for i in xrange(l,l+k):
            s[i] = '-' if s[i] == '+' else '+'
    

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
    print >> fout, "Case #{}: {}".format(t, r)
    sys.stdout.flush()

fout.close()

print "=== DONE ==="

