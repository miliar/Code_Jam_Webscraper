#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, re


def doit(l):
	'''
	>>> doit(['###','###'])
	None
	
	#>>> doit(['.##..','.####','.####','.##...'])

	#>>> doit(['.#.##.','.#.##'])

	#>>> doit(['.###.','.###'])

	#>>> doit(['.'])

	>>> doit(['##'])

	'''
	r = []

	must = []
	
	for i, row in enumerate(l):
		for req in must:
			if row[req:req+2] != '##': return False
			row = row[:req] + '\\/' + row[req+2:]
		
		must = []
		
		for m in re.finditer('##', row):
			must.append(m.start())
			row = row[:m.start()] + '/\\' + row[m.end():]
			
		if '#' in row: return False
		
		r.append(row)
	
	if must != []: return False

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
		R, C = map(int, f.readline().strip().split())
		Rs = []
		for i in range(R):
			Rs.append(f.readline().strip())
		
		l.append('Case #%d:' % (n+1))
		r = doit(Rs)
		if not r:
			l.append('Impossible')
		else:
			l.extend(r)
			
	if f2:
		f2.write('\n'.join(l))
		f2.close()
	
	if f:
		f.close()

if __name__ == "__main__":
#	test()
	cl()
