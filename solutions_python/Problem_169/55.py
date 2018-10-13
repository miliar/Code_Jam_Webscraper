#!/bin/sh

fname = 'B-small-attempt0'
#fname = 'B-large'
#fname = 'B-example'

from itertools import *

def tokreader(filename):
	for line in open(filename):
		for item in line.strip().split():
			yield item

def readn(n):
    r = []
    for i in xrange(n):
        r.append(read)
    return r

def solve():
	inp = tokreader(fname+'.in')
	read = lambda: inp.next()
	readn = lambda x:[read() for i in xrange(x)]
	outp = open(fname+'.out','w')

	T = int(read())
	for j in range(1,T+1):
		N,V,X = map(float,readn(3))
		
		if N == 1:
			R,C = map(float,readn(2))
			if C != X:
				r = 'IMPOSSIBLE'
			else:
				r = str(V / R)
		if N == 2:
			R1,C1 = map(float,readn(2))
			R2,C2 = map(float,readn(2))
			
			r = ''
			
			if (C1 == X) and (not (C2 == X)):
				r = str(V / R1)
			if (not (C1 == X)) and (C2 == X):
				r = str(V / R2)
			if (C1 == X) and (C2 == X):
				r = str(V / (R2+R1))			
			
			if ((C1 < X) and (C2 < X)) or ((C1 > X) and (C2 > X)):
				r = 'IMPOSSIBLE'
			if r == '':
				V1 = V * abs(C2-X) / (abs(C1-X) + abs(C2-X))
				V2 = V * abs(C1-X) / (abs(C2-X) + abs(C1-X))
				T1 = V1 / R1
				T2 = V2 / R2
				T = max(T1,T2)
				r = str(T)
			
		res = 'Case #%d: %s\n'%(j,r)
		print res
		outp.write(res)
		

	outp.close()
	print 'finished'
