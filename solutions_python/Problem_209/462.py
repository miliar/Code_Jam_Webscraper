#usr/bin/python
from __future__ import division
import sys
import random
from math import pi

fin = open(sys.argv[1], "r")
fout = open("A.out", "w")

	

T = int(fin.readline())
for ii in xrange(T):
	N, K = map(int,fin.readline().split(' '))
	R = []
	H = []
	for r in range(N):
		R1, H1 = map(int,fin.readline().split(' '))
		R.append(R1)
		H.append(H1)

	out = 0	
	for i in range (N):
		R1 = R[i]
		H1 = H[i]
		base = (R1**2 + 2*R1*H1)
		rest_p_p = []
		for j in range (N):
			if  R[j] <= R1 and i!=j:
				rest_p_p.append(R[j]*H[j])
			if len(rest_p_p) >= K-1:
				rest_p_p = sorted(rest_p_p, reverse = True)
	
				out1 = base + 2* sum(rest_p_p[:(K-1)])
								#print out1
				if out1 > out:
					out = out1
					sol = [out1, base, rest_p_p, K]
					#print base, rest_p_p
	print sol				
	fout.write("Case #" + str(ii+1) + ": %f" %(pi *out) + "\n")	