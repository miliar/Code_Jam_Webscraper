#!/usr/bin/python3

# author: Jakob Lindqvist
# date:   April 8 2017
# email:  jakoblindqvist1990@gmail.com

import sys
import fileinput

def solve(n):
	n = n.split()
	stack = list(n[0])
	flipper = int(n[1])
	num_flips = 0
	for i in range(len(stack)):
		if(stack[i] == '-'):
			for j in range(flipper):
				if(i+j >= len(stack)):
					return 'IMPOSSIBLE'
				if(stack[i+j] == '+'):
					stack[i+j] = '-'
				else:
					stack[i+j] = '+'
			num_flips += 1
	return num_flips

num_test_cases = int(sys.stdin.readline())
for i in range(num_test_cases):
	input_num = (sys.stdin.readline())
	res = solve(input_num)
	print("Case #" + str(i+1) + ": " + str(res))

