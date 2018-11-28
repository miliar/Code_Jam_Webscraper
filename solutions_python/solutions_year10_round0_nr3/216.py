#!/usr/bin/python3
#
# Google CodeJam 2010
# Qualification Round
#  Problem C
#
# Author: David Volgyes
#

import sys

def solve(R,k0,N,gi):
	money=0
	ptr=0
	g=int(gi[ptr])
	for r in range(0,R):
		k=k0
		G=0
		while g<=k and G<len(gi):
			k=k-g
			money+=g
			G=G+1
			if ptr+1<len(gi):
				ptr=ptr+1
			else:
				ptr=0
			g=int(gi[ptr])
	return money

T=int(sys.stdin.readline())

for case in range(1,T+1):
	inputwords=sys.stdin.readline().strip().split()
	R=int(inputwords[0])
	k=int(inputwords[1])
	N=int(inputwords[2])
	gi=sys.stdin.readline().strip().split()
	print("Case #%i: %s" % (case,solve(R,k,N,gi)))