#!/usr/bin/env python
import sys, os
from numpy import *


ifile=open('C.in', 'r')
ofile=open('C.out','w')
output=''

lines = ifile.readlines()
T = int(lines[0])

def countEuro(R, k, N, gi):
	kasse=0
	for r in range(0,R):
		capacity=0;
		for i in range (0,N):
			if ((capacity+gi[i])>k): break
			else: capacity+=gi[i]
		kasse+=capacity
		
		gi = hstack([gi[i:],gi[0:i]])
		
	return kasse
	
	
i=1
for line in range(1,T+1):
	l=lines[line*2-1].split()
	R = int(l[0]); k = int(l[1]); N = int(l[2])

	l=lines[line*2].split()
	gi=zeros(N,dtype=int)
	a=0
	for z in l:
		gi[a]=int(z)
		a=a+1
	
	if (i<>1): output+='\n'
	output+=('Case #%d: %d' % (i,countEuro(R, k, N, gi)))
	i+=1
	#print i
ofile.write(output)
ofile.close()
ifile.close()


