# Vladimir Burian, 2017 (vladaburian@gmail.com)

import string
import sys
import math
from itertools import *
import operator
from collections import Counter
import copy
import multiprocessing

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

# https://pypi.python.org/pypi/PuLP/1.6.5
from pulp import *


def gen_diagonals(n):
    diags = []
    
    for x in xrange(n-1):
        diags.append([(x+i, i) for i in xrange(n-x)])
        diags.append([(x+i, n-1-i) for i in xrange(n-x)])
    
    for y in xrange(1,n-1):
        diags.append([(i, y+i) for i in xrange(n-y)])
        diags.append([(i, n-1-(y+i)) for i in xrange(n-y)])
    
    return diags

def parse_input(fin):
    n,m = read_ints(fin)

    # grid
    g = [['.']*n for _ in xrange(n)]
    
    for _ in xrange(m):
        ch,x,y = fin.readline().split()
        g[int(x)-1][int(y)-1] = ch

    return n,m,g

def solve(n,m,g):
    xy = [(x,y) for x in xrange(n) for y in xrange(n)]
    
    prob =  LpProblem("fashion problem", LpMaximize)
    d = LpVariable.dicts("decision", ((x,y,t) for x,y in xy for t in ('+','x','o')), 0, 1, LpBinary)
    
    for x,y in xy:
        prob += lpSum(d[(x,y,t)] for t in ('+','x','o')) <= 1
        
        ch = g[x][y]
        
        if ch == '+':
            prob += lpSum(d[(x,y,t)] for t in ('+','o')) == 1

        if ch == 'x':
            prob += lpSum(d[(x,y,t)] for t in ('x','o')) == 1

        if ch == 'o':
            prob += lpSum(d[(x,y,t)] for t in ('o')) == 1

    for x in xrange(n):
        prob += lpSum(d[(x,y,t)] for y in xrange(n) for t in ('x','o')) <= 1
    
    for y in xrange(n):
        prob += lpSum(d[(x,y,t)] for x in xrange(n) for t in ('x','o')) <= 1
    
    for diag in gen_diagonals(n):
        prob += lpSum(d[(x,y,t)] for x,y in diag for t in ('+','o')) <= 1
    
    prob += (
        lpSum(d[x,y,t] for x,y in xy for t in ('+','x')) + 
        lpSum(d[x,y,t] for x,y in xy for t in ('o')) * 2
    )
    
    prob.solve()
    st = LpStatus[prob.status]
    ob = int(value(prob.objective))
    assert(st == 'Optimal')

    ops = []
    z = 0
    
    for x in xrange(n):
        for y in xrange(n):
            ch = '.'
            
            for t in ('+','x','o'):
                if d[(x,y,t)].varValue == 1:
                    ch = t
                    break

            if ch <> '.' and g[x][y] <> ch:
                ops.append((ch, x, y))
                z += 1
    
    r = []
    r.append('{} {}'.format(ob, z))
    
    for ch,x,y in ops:
        r.append('{} {} {}'.format(ch, x+1, y+1))
    
    r = '\n'.join(r)
    
    return r
    
###############################################################################

name = "test"
name = "D-small-attempt2"
name = "D-large"

sys.setrecursionlimit(5000)

fin = open(name+".in", "r")
fout = open(name+".out", "w")
fout = Tee(fout)

T = int(fin.readline())

pool = multiprocessing.Pool()
results = [pool.apply_async(solve, parse_input(fin)) for _ in xrange(T)]

for t in xrange(T):
    print >> fout, "Case #{}: {}".format(t+1, results[t].get())
    sys.stdout.flush()


fout.close()

print "=== DONE ==="

