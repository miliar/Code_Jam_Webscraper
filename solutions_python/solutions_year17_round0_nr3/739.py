#!/usr/bin/python3

# author: Jakob Lindqvist
# date:   April 8 2017
# email:  jakoblindqvist1990@gmail.com

import sys
import fileinput

def solve(case):
	case = case.split()
	n = int(case[0])
	k = int(case[1])
	while(k>1):
		if((n%2 == 0) and (k%2 == 1)):
			k = k//2
			n = (n//2)-1
		else:
			k = k//2
			n = n//2
	l = []
	if(n%2==0):
		l.append(n//2)	
		l.append((n//2)-1)	
	else:
		l.append(n//2)	
		l.append(n//2)	
	return l 

num_test_cases = int(sys.stdin.readline())
for i in range(num_test_cases):
	input_num = (sys.stdin.readline())
	res = solve(input_num)
	print("Case #" + str(i+1) + ": " + str(res[0]) + " " + str(res[1]))

