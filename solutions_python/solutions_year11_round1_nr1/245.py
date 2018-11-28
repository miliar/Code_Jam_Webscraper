#!/usr/bin/env python
import math
import sys
import os
from os import system


def divide(d,b):
	print d,b,b
	return (d - (b*math.floor(d/b)))

def Calculate(N,PD,PG):
	if PG is 100 and PD < 100:
		return "Broken"
	if PG is 0 and PD > 0:
		return "Broken"
	if PD is 0:
		return "Possible"
	r = divide(100,PD)
	d = PD
	while r > 0:
		print d, r
		r1 = divide(d,r)
		d = r
		r = r1
	#print float(float(100/d)), 100/d, PD/d, N
	#print float(float(100)/d) is 100/d 
	if (float(float(100)/d) - 100/d) < 0.00000001 and (100/d) <= N:
		return "Possible"
	else :
		return "Broken"


fp = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
str = fp.readline()
T = int(str)
for i in range(T):
	l = fp.readline().split()
	N = int(l[0])
	PD = int(l[1])
	PG = int(l[2])
	
	ret = Calculate(N,PD,PG)


	fout.write('Case #%d: %s\n'%((i+1),ret))
