#!/usr/bin/python

import sys

T = int(sys.stdin.readline())

for k in range(0, T):
	input = sys.stdin.readline().split()
	n = int(input[0])
	s = int(input[1])
	p = int(input[2])
	result = 0
	min = p * 3 - 4

	for i in range(0, n):
		t = int(input[i + 3])
		if t > min + 1:
			#print "%d is greater than %d" %(t, min + 1)
			result += 1
		elif t >= min and s != 0 and t >= p:
			#print "%d is gte %d and s is %d" %(t, min , s)
			s -= 1
			result += 1
	print "Case #%d: %d" %(k + 1, result)
			

	

