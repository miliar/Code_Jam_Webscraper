#! /usr/bin/python

from sys import stdin
from cStringIO import StringIO
import math

def dist(A,B):
	def sqr(x):
		return x*x
	return math.sqrt(sqr(A[0]-B[0])+sqr(A[1]-B[1]))
	
def minradius(plants):
	#small case
	N=len(plants)
	if N==1:
		return float(plants[0][-1])
	elif N==2:
		return float(max(plants[0][-1], plants[1][-1]))
	elif N==3:
		[A,B,C]=plants
		case1=max((dist(A,B)+A[-1]+B[-1])/2.0, C[-1])
		case2=max((dist(A,C)+A[-1]+C[-1])/2.0, B[-1])
		case3=max((dist(B,C)+B[-1]+C[-1])/2.0, A[-1])
		return float(min([case1,case2,case3]))
	else:
		print "???"
		
if __name__=='__main__':
	data=StringIO(stdin.read())
	T=int(data.readline())
	for case in xrange(1,T+1):
		N=int(data.readline())
		plants=[map(int, data.readline().split()) for i in xrange(N)]
		#print minradius(plants)
		print "Case #%d: %.7f"%(case, minradius(plants))
		
