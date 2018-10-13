#!/usr/bin/python3
#
# Google CodeJam 2010
# Qualification Round
#  Problem A
#
# Author: David Volgyes
#

import sys


def power(a,b):
	result=1
	for i in range(0,b):
		result=result*a
	return result

def calcState(N,K):
	if ((K+1)%(power(2,N)))==0:
		return "ON"
	return "OFF"


T=int(sys.stdin.readline())

for case in range(1,T+1):
	inputwords=sys.stdin.readline().strip().split()
	N=int(inputwords[0])
	K=int(inputwords[1])
	state=calcState(N,K)
	print("Case #%i: %s" % (case,state))
