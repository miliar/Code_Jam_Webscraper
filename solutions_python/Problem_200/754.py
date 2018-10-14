#!/usr/bin/python3

# author: Jakob Lindqvist
# date:   April 8 2017
# email:  jakoblindqvist1990@gmail.com

import sys
import fileinput

def is_tidy(n):
	l = ''.join(n)
	for i in range(len(l)-1):
		if(int(l[i]) > int(l[i+1])):
			return False
	return True

def solve(v):
	l = list(str(v))
	n = len(l) - 1
	while(n>0):
		s1 = l[n]
		s2 = l[n-1]
		if(not is_tidy(l)):
			s1 = '9'
			if(s2 == '0'):
				s2 = '0'
			else:
				s2 = str((int(s2) - 1))
		l[n] = s1
		l[n-1] = s2
		n -= 1
	res = (''.join(l)).lstrip('0')
	if(not is_tidy(l)):
		raise AssertionError("Error: " + str(v) + " => " + str(res))
	if(int(res) > v):
		raise AssertionError("Error: " + str(v) + " => " + str(res))
	return res 

num_test_cases = int(sys.stdin.readline())
for i in range(num_test_cases):
	input_num = int(sys.stdin.readline())
	res = solve(input_num)
	print("Case #" + str(i+1) + ": " + str(res))

