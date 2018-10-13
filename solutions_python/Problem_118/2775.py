#!/usr/bin/env python
def seed(c):
	s=len(c)
	if s<l:
		for d in range(10):
			for s in seed(c+[d]):
				yield s
	else:
		yield c+[c[L-s] for s in range(l+1, L+1)]
def fair(c):
	L=len(c)
	l=int(ceil(L*0.5))
	for s in range(l, L):
		if not c[L-s-s]==c[l]:
			return False
	return True
from math import ceil, floor
from sys import stdin, stderr
for T in range(1, 1+int(stdin.readline())):
	A, B=map(lambda c: int(c)**0.5, stdin.readline().split())
	a, b=int(ceil(A)), int(floor(B))
	A, B=str(a), str(b)
	#print>>stderr, A, B
	C=0
	M, N=len(A), len(B)
	for L in range(M, N+1):
		l=int(ceil(L*0.5))
		#print>>stderr, L, l
		for c in range(1,10):
			for c in seed([c]):
				c=int(''.join(map(str,c)))
				if a<=c<=b:
					c=str(c**2)
					if fair(c): C+=1
	print 'Case #%d:'%T, C