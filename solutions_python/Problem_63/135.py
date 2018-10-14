#!/usr/bin/env python
import math
import sys
import os
from os import system


fp = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
str = fp.readline()
T = int(str)
for i in range(T):
	l = fp.readline().split()
	L = int(l[0])
	P = int(l[1])
	C = int(l[2])
	now = L
	fac = C
	num = 0
	print L,P,C,fac
	while 1:
		if now*fac >= P:
			break;
		fac = fac*fac
		num = num + 1
	fout.write('Case #%d: %d\n'%(i+1,num))

