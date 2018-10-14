import imp, sys

sys.modules["utils"] = __mod = imp.new_module("utils")
exec """#!/usr/bin/python

from itertools import chain, repeat, izip

def line(*args):
	L = raw_input().strip().split()
	L = izip( L, chain( args, repeat(str) ) )
	return [ type(data) for data, type in L ]	
	
def iline(): return map( int, raw_input().strip().split() )
def fline(): return map( float, raw_input().strip().split() )""" in vars(__mod)

#!/usr/bin/python

import sys
from utils import line, fline

def test():
    N, V, X = line(int, float, float)
    data = [ fline() for i in xrange(N) ]
    
    yield
    
    data.sort(key=lambda (r,c) : c)
    if data[0][1] > X or data[-1][1] < X:
        print 'IMPOSSIBLE'
        return
        
    cool = [ (r,c) for r,c in data if c < X ]
    exact = [ (r,c) for r,c in data if c == X ]
    hot = [ (r,c) for r,c in data if c > X ]
    
    if not cool:
        cool += exact
    else:
        hot += exact
    
    r1, q1 = sum( r for r,c in cool ), sum( r*c for r,c in cool )
    r2, q2 = sum( r for r,c in hot ), sum( r*c for r,c in hot )
    Q = X*(r1+r2)
    
    #print >>sys.stderr, (V,X), data
    #print >>sys.stderr, q1, q2, Q, '\t', r1, r2
    
    if abs(q1+q2-Q) < 1e-10:
        k1 = k2 = 1
    elif q1+q2 > Q:
        k1, k2 = 1, (X*r1-q1)/(q2-X*r2)
    else:
        k1, k2 = (X*r2-q2)/(q1-X*r1), 1
           
    #print >>sys.stderr, k1, k2
    T = V / (k1*r1 + k2*r2)
        
    print '%.9f' % T
        
        
        
if __name__ == '__main__':
    T = input()
    for i in xrange(1, T+1):
        print 'Case #%d:' % i,
        solver = test()
        if hasattr(solver, 'next'):
            list(solver)
        elif callable(solver):
            solver()

