#!/bin/python
import time
import math
import copy

from decimal import *
getcontext().prec = 50
from Queue import PriorityQueue


#pi = pi / Decimal(10**100)

def naive():
	return -1

def test():
	return -1
	
def main():
	
	import sys
	#from operator import itemgetter
	#from sets import Set
	

	T= int(sys.stdin.readline().strip())
	
	for t in xrange(T):
		
		(D,N) = map(int, sys.stdin.readline().strip().split())
		pq = PriorityQueue()
		
		for _ in xrange(N):
			
			(K,S) = map(int, sys.stdin.readline().strip().split())
			pq.put((D-K,S))
		

		
		(minK, minS) = pq.get()
		preK = minK
		preS = minS
		T = []
		
		T.append((1.0*minK)/(1.0*minS) )
		stop = D
		n = 0
		while (not  pq.empty() ):
		
			(K,S) = pq.get()
			
			if (S <= minS):
				minK = K
				minS = S
				T = [(1.0*minK)/(1.0*minS)]
				n = 0
				stop = D
				
				preK = K
				preS = S
				continue
				
			if (S <= preS):
				T[n] = (1.0* (stop - D+K))	/(1.0*S)
			else:
				p =  (   1.0*(preS*(D-K) - S*(D-preK)) / (1.0*(preS - S))  )
				
				if (p >= stop):
					T[n] = (1.0* (stop - D+K))/(1.0*S)
				
				else:
					T[n] = (1.0 * (stop-p))/ (1.0*preS)
					stop = p
					
					T.append((1.0* (stop - D+K))/(1.0*S))
					n += 1
			
			
			preK = K
			preS = S

		#print sum(T)
			
				
			
			
		_minv = (1.0*D)/(1.0 * sum(T))
		
		#print mS, mK
		
		#print 1.0*D*mS/(D-mK)
	
	
		
		print "Case #" + str(t+1) +": " + '{:16.10f}'.format(_minv)
		
		
		
	
if __name__ == "__main__":
	
	#s= time.time()
	main()
	
	#print time.time()-s
	