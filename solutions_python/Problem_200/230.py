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
		
def main():
	import sys

	T = int(raw_input().strip())
	
	for t in xrange(T):
		S = raw_input().strip()
		
		Num = [0]*len(S)
		
		for k in range(len(S)):
			Num[k] = int(S[k])
		
		for k in range(len(S)-1,0,-1):
			if Num[k-1] > Num[k]:
				Num[k] = 9
				Num[k-1] -= 1
		
		sol = 0
		k = 0
		while ( k < len(S) ) and ( Num[k] == 0):
			k += 1
		
		_str = ''
		while ( k < len(S) ):
			if (Num[k] == 9):
				_str = _str + '9'* (len(S) - k)
				break
				
			_str = _str + str(Num[k])
			k += 1
		
		
		#print _str
		
		
		print "Case #" + str(t+1) + ": "+ _str
	
	
	
	
	
	
if __name__ == "__main__":
	
	#import time
	#the_start_time = time.time()
	main()
	
	
	#A = [3,5,6]
	
	#print lower_bound(A,5)
	#print upper_bound(A,5)
	
	#print time.time() - the_start_time
	
	
		
	
