#!/usr/bin/env python 
import sys

def solve(D):
	R = [ ( i, sum(D[0:i]) ) for i in range(1,len(D)) if D[i]>0 ]
	y = max([ (a-b) for (a,b) in R ] or [0]) 
	return max([0,y])

def main():

	T = int(input())
	for i in range(1,T+1):
		s = sys.stdin.readline().strip().split(' ')
		D = map(int,list(s[-1]))
		y = solve(D)
		print 'Case #%d: %d'%(i,y)
	return 0

if __name__=='__main__':
	sys.exit(main())
