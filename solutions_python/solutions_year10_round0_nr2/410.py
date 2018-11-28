#!/usr/bin/python
from fractions import gcd

def gcdv(v, p, r):
	if (r == p + 1):
		return gcd(v[p], v[r]);
									
	if (r == p):
		return v[p];

	q = (p + r) / 2;
	return gcd(gcdv(v, p, q), gcdv(v, q + 1, r));


C=int(raw_input())

for case in range(C):
	r=raw_input().split()
	n=int(r[0])
	t=map(int,r[1:])
	gaps=[]
	for i in range(n):
		for j in range(i+1,n):
			gaps.append(abs(t[i]-t[j]))

	gcds=[]
	divisor=gcdv(gaps,0,len(gaps)-1)

	result=0
	for e in t:
		if (e%divisor==0):
			tr=0
		else:
			tr=divisor-(e%divisor)
		if result<tr:
			result=tr


	print "Case #"+str(case+1)+": "+str(result)
