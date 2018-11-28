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
from math import pi
from sys import stderr

def test():
    n, k = iline()
    sizes = [iline() for i in xrange(n)]

    yield
    
    sizes.sort(key=lambda (r, h) : r*h)

    maybe = sizes[:-k+1] if k > 1 else sizes
    certain = sizes[-k+1:] if k > 1 else []


    certain_r = max(r for r, h in certain) if certain else 0
    certain_area = sum(2*r*h for r, h in certain) + (certain_r ** 2)

    maybe_best = max(2*r*h + max(0, (r**2) - (certain_r ** 2)) for r, h in maybe)

    print '{:.9f}'.format(pi*(certain_area+maybe_best))
        
        
        
if __name__ == '__main__':
    def main():
        T = input()
        for i in xrange(1, T+1):
            print 'Case #%d:' % i,
            solver = test()
            if hasattr(solver, 'next'):
                list(solver)
            elif callable(solver):
                solver()
    main()

