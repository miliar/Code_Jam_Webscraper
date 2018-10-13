#! /usr/bin/env python
# -*- coding: UTF-8 -*-
	
''' C - Candy Splitter
'''

import sys

if len(sys.argv) <= 1:
	exit('args!')
fn = sys.argv[1]
fc = open(fn).readlines()

v = False
if '-v' in sys.argv:
	v = True

T = int(fc[0])

for i in range(0,T*2,2):
	l1 = fc[i+1].strip()
	l2 = fc[i+2].strip().split(' ')
	
	N = int(l1)
	
	s,p,e = 0,10**6+1,0
	for c in l2:
		v = int(c)
		p = min(p,v)
		s += v
		e ^= v
	s-=p
	
	if e:
		print 'Case #%i: NO'%((i/2)+1)
		continue
	
	print 'Case #%i: %s'%((i/2)+1,s)
