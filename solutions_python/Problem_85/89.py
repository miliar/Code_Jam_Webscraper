#!/usr/bin/env python
import sys
fin=open(sys.argv[1])
cases=int(fin.readline())
for case in range(1,cases+1):
	inp=map(int,fin.readline().split())
	L,t,N,C=inp[:4]
	A=inp[4:]
	vec=[0]
	for star in xrange(N):
		v1=vec[-1]
		for i in reversed(range(len(vec))):
			vec[i]=min(vec[i]+2*A[star%C], vec[i-1]+A[star%C]+0.5*max(min(t-vec[i-1],2*A[star%C]),0)) if i>0 else vec[i]+2*A[star%C]
		if len(vec)<=L: vec.append(v1+A[star%C]+0.5*max(min(t-v1,2*A[star%C]),0))
	print "Case #%d: %d"%(case,min(vec))
