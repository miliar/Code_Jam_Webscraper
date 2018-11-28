#!/usr/bin/env python
from math import *

f=open('A-large.in','r').readlines()
f1=open('A-large.out','w')
l=f[0]

cnt=0
for line in f[1:]:
	cnt=cnt+1
	input=line.strip().split()
	N=int(input[1])
	off = 0
	for i in range(int(input[0])):
		NN=N-pow(2,i)+1
		if NN <= 0:
			f1.write('Case #'+str(cnt)+": OFF\n")
			off=1
			break


		if ceil(NN / pow(2,i)) % 2 == 0:
			f1.write('Case #'+str(cnt)+": OFF\n")
			off=1
			break
	if off==0:
		f1.write('Case #'+str(cnt)+": ON\n")


