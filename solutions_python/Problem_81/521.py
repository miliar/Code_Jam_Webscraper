#! /usr/bin/env python
# -*- coding: UTF-8 -*-
	
''' A
'''

import sys, math, random

if len(sys.argv) <= 1:
	exit('args!')
fn = sys.argv[1]
fc = open(fn).readlines()

v = False
if '-v' in sys.argv:
	v = True

T = int(fc[0])

def RPI(N,W,L,T):
	WP = [ float(W[i])/float(W[i]+L[i]) for i in range(N) ]
	OWP = [0.0 for i in range(N)]
	for i in range(N):
		for j,c in enumerate(T[i]):
			if j!=i and not c is None:
				OWP[i] += float(W[j]-(1-c))/float(W[j]+L[j]-1)
		OWP[i] /= float((W[i]+L[i]))
	OOWP = [ sum([ OWP[j] for j,c in enumerate(T[i]) if j!=i and not c is None ]) / (W[i]+L[i]) for i in range(N) ]
	return [ 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i] for i in range(N) ]

k = 1
for i in range(T):
	l1 = fc[k].strip()
	N = int(l1)
	
	W,L = [0 for m in range(N)],[0 for m in range(N)]
	T = [[0 for n in range(N)] for m in range(N)]
	
	for j in range(N):
		k += 1
		for ii,c in enumerate(fc[k].strip()):
			T[j][ii] = None
			if c=='1':
				W[j] += 1
				T[j][ii] = 1
			elif c=='0':
				L[j] += 1
				T[j][ii] = 0
	
	RPIs = RPI(N,W,L,T)
	
	print 'Case #%i:'%(i+1)
	for r in RPIs:
		print r
	
	k += 1
