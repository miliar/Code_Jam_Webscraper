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
    n = [ord(ch) - ord('0') for ch in fin.readline().strip()]
    
    while True:
        assert(all(0 <= x <= 9 for x in n))
        
        istidy = True
        
        for i in xrange(len(n)-1):
            if n[i] > n[i+1]:
                istidy = False
                break;
        
        if istidy:
            break;
        
        n[i] -= 1
        
        for j in xrange(i+1, len(n)):
            n[j] = 9
    
    n = [chr(d + ord('0')) for d in n]
    n = int(''.join(n))
    
    assert(n > 0)
    
    return n

###############################################################################

name = "test"
name = "B-small-attempt0"
name = "B-large"

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

