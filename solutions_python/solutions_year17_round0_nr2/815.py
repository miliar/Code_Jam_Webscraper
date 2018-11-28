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

from utils import line

def test():
    num, = line()
    
    yield
    
    num = map(int, num)

    i = 1
    while i < len(num) and num[i-1] <= num[i]:
        i += 1

    if i == len(num):
        print ''.join(map(str, num))
        return

    high = max(num[:i])

    if high == 1:
        print '9'*(len(num)-1)
    else:
        i = sum(1 for v in num[:i] if v != high)+1
        num[i-1] -= 1
        print ''.join(map(str, num[:i])) + '9'*len(num[i:])
        
        
if __name__ == '__main__':
    T = input()
    for i in xrange(1, T+1):
        print 'Case #%d:' % i,
        solver = test()
        if hasattr(solver, 'next'):
            list(solver)
        elif callable(solver):
            solver()

