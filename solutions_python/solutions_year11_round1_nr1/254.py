#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def doit(D,PD,PG):
	'''
	>>> doit(1,100,50)

	>>> doit(10,10,100)

	>>> doit(9,80,56)
	
	'''
	r = False
	if (PG == 100 and PD != 100) or (PG == 0 and PD != 0):
		return r
	
	for n_games in xrange(1, D+1):
		t = PD / 100.0 * n_games
		
		print float(int(t)), t, n_games
		if float(int(t)) == t:
			r = True 

	return r
	
	
def test():
	import doctest, a
	doctest.testmod(a)

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
		D, PD, PG = map(int, f.readline().split())
		r = doit(D, PD, PG)
		if r:
			r = 'Possible'
		else:
			r = 'Broken'
		l.append('Case #%d: %s' % (n+1, r))

#	print(''.join(l))
	f2.write('\n'.join(l))
	f2.close()
	f.close()

if __name__ == "__main__":
#	test()
	cl()
