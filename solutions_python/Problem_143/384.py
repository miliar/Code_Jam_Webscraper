import string
import sys
import math
from itertools import *
import operator
import cPickle
from collections import Counter

class Tee:
    def __init__(self, file):
        self.file = file
        
    def write(self, str):
        sys.stdout.write(str)
        self.file.write(str)

    def close(self):
        self.file.close()

def solve(A,B,K):
    count = 0
    
    for a in xrange(A):
        for b in xrange(B):
            if (a&b) < K:
                count += 1
    
    return count


name = "test"
name = "B-small-attempt0"
#name = "A-large"

fin = open(name+".in", "r")
fout = open(name+".out", "w")
fout = Tee(fout)

T = int(fin.readline())

for t in range(1,T+1):
    A,B,K = [int(x) for x in fin.readline().split()]

    r = solve(A,B,K);

    print >> fout, "Case #{}: {}".format(t, r)

print "=== DONE ==="
