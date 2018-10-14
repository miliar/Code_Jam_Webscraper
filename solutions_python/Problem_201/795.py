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

from utils import iline
from collections import defaultdict

def test():
    n, k = iline()
    
    yield
    
    values = [(n, 1)]
    while True:
        values = sorted(values)[::-1]

        new_values = defaultdict(int)
        for hole, spots in values:
            a = (hole-1)/2
            b = (hole-1) - a

            if k <= spots:
                print max(a, b), min(a, b)
                return
            
            k -= spots

            new_values[a] += spots
            new_values[b] += spots

        values = new_values.items()
        
        
if __name__ == '__main__':
    T = input()
    for i in xrange(1, T+1):
        print 'Case #%d:' % i,
        solver = test()
        if hasattr(solver, 'next'):
            list(solver)
        elif callable(solver):
            solver()

