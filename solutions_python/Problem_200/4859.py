import sys, os
import re

tCase = int(sys.stdin.readline())


def isTidy(arr):

	for i in xrange(0, len(arr)-1):
		if arr[i] <= arr[i+1]:
			continue
		else:
			return False
			
	return True
	
	
def task(case):
	
	last_n = 0
	j = case
	while j > 0:
	
		arr = str(j)
	
		if len(arr) == 1:
			return j
			
		minus = 1
		if '0' in arr:
			ix = arr.rfind('0')
			ix = len(arr) - ix - 1
			minus = 10**ix
			if minus == 10:
				minus = 1
			#print j, minus
	
		if isTidy(arr):
			return j
		j-=minus

	return last_n



for i in xrange(tCase):	
	case = int(sys.stdin.readline())
	#print case+1
	#case.append(frase)
	print "Case #%d: %d" % (i+1, task(case))

	
	

