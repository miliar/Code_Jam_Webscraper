#!/usr/bin/env python
import math
import sys
import os
from os import system

def calculate(C):
	all = 0
	for i in C:
		all = all^i
	
	if all is not 0:
		return "NO"

	C.sort()
	C.reverse()
	C.pop()
	return sum(C)




fp = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
str = fp.readline()
T = int(str)
for i in range(T):
	l = fp.readline().split()
	N = int(l[0])
	C = []
	l = fp.readline().split()
	for j in range(N):
		C.append(int(l[j]))

	ret = calculate(C)

	fout.write('Case #%d: %s\n'%((i+1),ret))
