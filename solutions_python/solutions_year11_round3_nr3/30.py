#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def doit(f1,f2):
	'''
	>>> doit(1,2)
	3
	
	'''	
	N, L, H = map(int, f1.strip().split())
	reqs = map(int, f2.strip().split())

	l = [] 
	
	len_reqs = len(reqs)

	for option in xrange(L, H+1):
		for n, req in enumerate(reqs):
			if req % option == 0 or option % req == 0:
				if n+1 == len_reqs: l.append(option)
				continue
			else:
				break
									
	if not l:
		return 'NO'
	else:
		return min(l)
	
def test():
	import doctest, z
	doctest.testmod(z)

def cl():
	f = sys.stdin
	f2 = None
	if len(sys.argv) >= 2:
		fn = sys.argv[1]
		if fn != '-':
			f = open(fn)
			f2 = open(fn.replace('in','out'), 'w')
			
	cases = int(f.readline())
	l = []
	for n in range(cases):		
		l.append('Case #%d: %s' % (n+1, doit(f.readline(), f.readline())))
			
	if f2:
		f2.write('\n'.join(l))
		f2.close()
	
	if f:
		f.close()

if __name__ == "__main__":
#	test()
	cl()
