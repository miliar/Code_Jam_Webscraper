#!/usr/bin/env python

def rank(b1,b2):
	res = 0
	i1 = 0
	i2 = 0
	while i1< len(b1):
		if b1[i1] > b2[i2]:
			res +=1
			i1+=1
			i2+=1
		else:
			i1+=1
	return res
	
_f = open('in','r')

T = int(_f.readline())

for t in xrange(T):
	N = int(_f.readline())
	b1 = list(float(x) for x in _f.readline().split())
	b2 = list(float(x) for x in _f.readline().split())
	b1.sort()
	b2.sort()
	print 'Case #' + str(t+1) + ': ' + str(rank(b1,b2)) + ' ' + str(N-rank(b2,b1))
