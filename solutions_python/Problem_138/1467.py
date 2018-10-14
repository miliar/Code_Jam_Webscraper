#!/usr/bin/env python

T = int(raw_input())
for t in xrange(T):
	N = int(raw_input())
	a = set(map(float,raw_input().split()))
	b = set(map(float,raw_input().split()))
	A,B = a.copy(),b.copy()
	y = 0
	while len(a)>0:
		if max(a)>max(b):
			y += 1
			be=min(b)
			e = min(e for e in a if e>be)
			a.remove(e)
			b.remove(be)
		elif len(a)>1:
			a.remove(min(a))
			b.remove(max(b))
		else:
			be = b.pop()
			ae = a.pop()
	z = 0
	while len(A)>0:
		if min(A)<max(B):
			ae = min(A)
			e = min(e for e in B if e>ae)
			A.remove(min(A))
			B.remove(e)
		else:
			A.remove(min(A))
			B.remove(min(B))
			z += 1
	print 'Case #%d: %d %d' % (t+1,y,z)

	

