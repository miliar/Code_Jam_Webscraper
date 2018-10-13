#!/usr/bin/python
#
# Google CodeJam 2010
#  Round 1B
#  Problem A
#
# Author: David Volgyes
#

import sys,os,numpy
from sympy.geometry import *

def add(old,new):
	if new=="/": return old
	old[new]=1
	old=add(old,os.path.dirname(new))
	return old

T=int(sys.stdin.readline().strip())
for case in range(1,T+1):
	inputwords=sys.stdin.readline().strip().split()
	N=int(inputwords[0])
	M=int(inputwords[1])
	oldPaths=dict()
	newPaths=list()
	if N>0:
		for i in range(0,N):
			oldPaths[(sys.stdin.readline().strip())]=1
	if M>0:
		for j in range(0,M):
			newPaths.append(sys.stdin.readline().strip())
	for p in newPaths:
		oldPaths=add(oldPaths,p)
	result=len(oldPaths)-N
	print("Case #%i: %s" % (case,result))
