#!/bin/sh

import time

fname = 'C-small'
#fname = 'C-large'
#fname = 'C-example'

from itertools import *

def solve():
	outp = open(fname+'.out','w')
	lines = [x[:-1].split(' ') for x in open(fname+'.in')]

	T = int(lines[0][0])
	
	lc = 1
	
	for j in range(0,T):
		N = int(lines[lc][0])
		lc += 1
		st = lines[lc:lc+N]
		lc += N
		
		words = set()
		for s in st:
			words |= set(s)
			
		words = sorted(words)
		ifw = {}
		wi = 0
		for w in words:
			ifw[w] = wi
			wi += 1

		st = [[ifw[w] for w in s] for s in st]			
#		print st
		
#		st = [set(x) for x in st]
#		print st	
		
		best = 999999
		
		common = set(set(st[0]) & set(st[1]))
		st[0] = sorted(set(st[0]) - common)
		st[1] = sorted(set(st[1]) - common)
		
		if j<100:
			for it in (product('EF',repeat=N-2)):
				it = ['E','F'] + list(it)
				e = list(st[0])
				f = list(st[1])
				for si in range(2,N):
					if it[si] == 'E':
						e += st[si]
					else:
						f += st[si]
				e = set(e)
				f = set(f)
				both = len((e & f) | common)
				if both < best:
	#				print e,f,common
	#				print ((e & f) | common),both
					best = both
	
			res = 'Case #%d: %d\n'%(j,best)
			print (time.strftime("%I:%M:%S")), N, res
			outp.write(res)
		

	outp.close()
	print 'finished'
