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

def analyzeStr(s):
    l = []
    c = []
    
    prevch = s[0]
    count = 1
    
    for i in xrange(1,len(s)):
        if prevch == s[i]:
            count += 1
        else:
            l.append(prevch)
            c.append(count)
            count = 1
            prevch = s[i]
            
    l.append(prevch)
    c.append(count)
    
    return c, l

def getNSteps(Cs, i, n):
    steps = 0
    for c in Cs:
        steps += abs(c[i] - n)
    return steps

def mean(Cs, i):
    s = 0
    for c in Cs:
        s += c[i]
    n = len(Cs)
    return int((s+(n/2)) / n)

def getMinSteps(Cs, i):
    m = mean(Cs, i)
    steps = min(getNSteps(Cs, i, m), getNSteps(Cs, i, m-1), getNSteps(Cs, i, m+1))
    return steps
    

def solve(N, S):
    c, L = analyzeStr(S[0])
    
    Cs = [c]
    
    for i in xrange(1,N):
        c, l = analyzeStr(S[i])
        if (l != L):
            return False
        else:
            Cs.append(c)

    steps = 0
    for i in xrange(len(L)):
        steps += getMinSteps(Cs, i)
    
    return steps


name = "test"
name = "A-small-attempt0"
#name = "A-large-practice"

fin = open(name+".in", "r")
fout = open(name+".out", "w")
fout = Tee(fout)

T = int(fin.readline())

for t in range(1,T+1):
    N = int(fin.readline())
    S = [fin.readline().strip() for _ in xrange(N)]

    r = solve(N, S);

    if (r is False):
        r = "Fegla Won"

    print >> fout, "Case #{}: {}".format(t, r)

print "=== DONE ==="
