#!/usr/bin/python
import sys
from math import pi

fi = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
fo = open(".".join(sys.argv[1].split('.')[:-1])+".out","w") if len(sys.argv) > 1 else sys.stdout

TC=int(fi.readline())
for i in range(1,TC+1):
	
	N,K=map(int,fi.readline().split())
	C=[]
	for n in range(N):
		R,H=map(int,fi.readline().split())
		C.append([R,H,pi*R*R,pi*2*R*H])
	C.sort()

	max = 0
	if K==1:
		for k in range(N):
			if C[k][2]+C[k][3]>max:
				max=C[k][2]+C[k][3]

	elif K==N:
		max = C[N-1][2]
		for k in range(N):
			max+=C[k][3]
	else:

		S=[]
		for k in range(K-1):
			S.append(C[k][3])
		max = 0
		for k in range(K-1,N):
			S.sort(reverse=True)
			m=C[k][2]+C[k][3]+sum(S[:K-1])
			if m>max:
				max=m
			S.append(C[k][3])
			
		
		

	print("Case #{}: {}".format(i,max),file=fo)

