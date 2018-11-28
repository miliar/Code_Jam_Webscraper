#!/usr/bin/python

from heapq import *


def solve(n, k,q):



	for i in range(0,k):

		ref = n >> 1
		if(n%2==0):
			ls = ref -1
			lr = ref

		else:
			ls = ref
			lr = ref


		heappush(q,-ls)
		heappush(q,-lr)

	 	n = -heappop(q)
	 	
	 	if ls==0 and lr==0:
	 		break

	 	k = k-1

	return ls,lr



if __name__ == '__main__':
	t = int(raw_input())

	for i in xrange(1, t + 1):

		n, k = [int(s) for s in raw_input().split(" ")] 

		if(n==k or k>n):
			result = 0
			result2 = 0
		else:
			q = []
	  		result,result2 = solve(n,k,q)

	  	x = str(i)
	  	y = str(max(result,result2))
	  	z = str(min(result,result2))

	  	print "Case #{}: {} {}".format(x,y,z)