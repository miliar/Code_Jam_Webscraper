#!/usr/bin/env sage
Z.<i,j,k>=QuaternionAlgebra(-1,-1)

def g(c):
	return Z.gen('ijk'.index(c))

def sol(s,L,X):
	v=map(g,s)
	T=reduce(lambda x,y:x*y,v)
	if T^X != -1:return "NO"
	t,a=Z(1),L*X+100
	for n in range(L):
		t=t*v[n]
		for m in range(4):
			if  T^m * t == g('i'):
				a=min(a,n+L*m)
		if a==n:break
	t,b=Z(1),L*X+100
	for n in range(L):
		t=v[-n-1]*t
		for m in range(4):
			if  t * T^m == g('k'):
				b=min(b,n+L*m)
		if b==n:break
	return "YES" if a+b+2<L*X else "NO"

for i in range(int(input())):
	L,X=map(int,raw_input().split())
	s=raw_input()
	print "Case #%d: %s"%(i+1,sol(s,L,X))
