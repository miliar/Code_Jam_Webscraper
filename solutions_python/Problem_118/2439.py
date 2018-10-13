#!/usr/bin/python
import sys
import math

def contains(x):
	pals = [0,1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99,
 101,111,121,131,141,151,161,171,181,191,202,212,
  222,232,242,252,262,272,282,292,303,313,323,333,
	 343,353,363,373,383,393,404,414,424,434,444,454,
	  464,474,484,494,505,515];
	tmp = [ i for i in pals if i == x]
	if len(tmp) > 0:
		return True
	
	return False





try:
	input = raw_input
except NameError:
	foo =1 

T = int(input())
t = 1
A = sys.maxint
B = 0
knownSqrs = []
palSqrs = [0,1,4,9,121,484,676,10201,12321,14641,40804,
 44944,69696,94249,698896,1002001,1234321,4008004,
  5221225,6948496,100020001,102030201,104060401,
	 121242121,123454321,125686521,400080004,404090404,
	  522808225];



while t <= T :
	result = 0
	line = input().split(' ')
	a = int(line[0])
	b = int(line[1])
	#
	bb = [i for i in palSqrs if i >= a and i <= b and contains(i) ]#and any(int(math.sqrt(i)) in s for s in pals)]
	result = len(bb)
	
	print 'Case #{0}: {1}'.format(t,result)
	t = t + 1
##
