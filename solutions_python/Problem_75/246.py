#! /usr/bin/env python
# -*- coding: UTF-8 -*-
	
''' B - Magicka
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


def list_str(lst):
	if lst:
		return '[%s]'%reduce(lambda x,y:'%s, %s'%(x,y),lst)
	return '[]'

for i in range(T):
	l = fc[i+1].strip().split(' ')
	r = []
	
	C = int(l[0])
	combs = l[1:1+C]
	D = int(l[1+C])
	opds = l[2+C:2+C+D]
	N = int(l[2+C+D])
	invks = l[3+C+D]
	
	transforms = {}
	oppositions = {}
	seen = {}
	
	for c in combs:
		transforms[c[0:2]] = c[2]
	for o in opds:
		oppositions[o[0]] = o[1]
		oppositions[o[1]] = o[0]
	
	if v: print invks, transforms
	
	for c in invks:
		if not c in seen:
			seen[c] = 0
		seen[c] += 1
		r.append(c)
		while len(r) > 1 and ( (r[-2]+r[-1]) in transforms or (r[-1]+r[-2]) in transforms ) :
			nc = ''
			if (r[-2]+r[-1]) in transforms:
				nc = transforms[(r[-2]+r[-1])]
			else:
				nc = transforms[(r[-1]+r[-2])]
			seen[r[-2]] -= 1
			seen[r[-1]] -= 1
			if not nc in seen:
				seen[nc] = 0
			seen[nc] += 1
			r.pop()
			r.pop()
			r.append(nc)
		if len(r) and r[-1] in oppositions and oppositions[r[-1]] in seen and seen[oppositions[r[-1]]] > 0:
			r = []
			seen = {}
	
	print 'Case #%i: %s'%(i+1,list_str(r))
