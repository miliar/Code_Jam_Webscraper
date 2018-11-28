#!/usr/bin/python
 
import math
from Queue import PriorityQueue
#from decimal import *
#import fractions 
#getcontext().prec = 50
#_modulo = 10**9 + 7


def lower_bound(nums, target):
	l, r = 0, len(nums) - 1
	while l <= r:
		mid = l + (r - l) / 2
		if nums[mid] >= target:
			r = mid - 1
		else:
			l = mid + 1
	return l
	
def upper_bound(nums, target):
	l, r = 0, len(nums) - 1
	while l <= r:
		mid = l + (r - l) / 2
		if nums[mid] > target:
			r = mid - 1
		else:
			l = mid + 1
	return l

def naive(N,K):
	
	
	q = PriorityQueue()
	q.put(-N)
	
	for k in range(K-1):
		cur = -1 * q.get()
		
		q.put(-1 * (cur/2) )
		
		r = 1 if (cur > 0 and cur%2 ==0) else 0
		#print r
		q.put(-1 * (cur/2 - r) )
		
	cur = -1*q.get()
	
	#print cur
	
	r = 1 if (cur > 0 and cur%2 ==0) else 0
	
	_max = str(cur/2)
	_min = str(cur/2 - r)
	
	return _max + " " + _min
	
	
def main():
	import sys

	T = int(raw_input().strip())
	
	for t in xrange(T):
		N, K  = map( int, raw_input().strip().split() )
		
		low_bin = len(bin(K)) -  3
		
		lowest = 1<<low_bin
		
		values = {N: 1}
		
		for i in range(low_bin):
			
			keys = values.keys()
			for k in keys:
				r = 1 if (k >0 and  k% 2 ==0 ) else 0
				cur = k/2
				if (not cur in values ):
					values[cur] = 0
				values[cur] += values[k]
				cur = cur - r
				if (not cur in values ):
					values[cur] = 0
				values[cur] += values[k]
				
				del values[k]
		
		#print cur
		
		#print values
		keys = sorted(values.keys(), reverse=True)
		
		total = 0
		target = K - lowest
		#print target
		val = -1
		for k in keys:
			total += values[k]
			if target < total:
				val = k
				break
		
		_max = str(val/2)
		r = 1 if (val >0 and  val% 2 ==0 ) else 0
		_min = str(val/2 -r )
		
		print "Case #" + str(t+1) + ": "+ _max + " " + _min
		
		#print "Case #" + str(t+1) + ": "+ naive(N,K)
		
		#print "Case #" + str(t+1) + ": "+ _str
	
	
	
	
	
	
if __name__ == "__main__":
	
	#import time
	#the_start_time = time.time()
	main()
	
	
	#A = [3,5,6]
	
	#print lower_bound(A,5)
	#print upper_bound(A,5)
	
	#print time.time() - the_start_time
	
	
		
	
