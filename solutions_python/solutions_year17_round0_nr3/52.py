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
    n,k = read_ints(fin)
    
    # map of free stand parts : length -> count
    p = Counter({n: 1})
    
    while True:
        # pop the largest available stands part
        l = max(p.iterkeys())
        c = p.pop(l)
        assert(l > 0)
        assert(c > 0)
        
        # division of free stands to two groups - left and right
        la = (l-1) // 2
        lb = l // 2
        assert(la+lb+1 == l)
    
        if k <= c:
            return "{} {}".format(lb, la);
    
        k -= c
        
        if la <> 0:
            p[la] += c
        
        if lb <> 0:
            p[lb] += c

###############################################################################

name = "test"
name = "C-small-1-attempt0"
name = "C-small-2-attempt0"
name = "C-large"

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

