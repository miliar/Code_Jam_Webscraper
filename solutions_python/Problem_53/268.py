#!/usr/bin/env python

import sys

powers_of_two = []

def generate_powers_of_two():
	
	last = 1
	for i in range(1, 32):
		last = last * 2
		powers_of_two.append(last)
		
def calculate_state(N, k):
	if ((k + 1) % (powers_of_two[N - 1]) == 0):
		return 'ON'
	else:
		return 'OFF'
		
if __name__ == '__main__':
	
	generate_powers_of_two()
	
	inp_file = sys.argv[1]
	op_file = sys.argv[2]
	
	inp = open(inp_file, 'r')
	op = open(op_file, 'w')
	
	T = int(inp.readline())
	
	for i in range(1, T+1):
		str = inp.readline()
		nums = str.split()
		N = int(nums[0])
		k = int(nums[1])
		op.write('Case #%d: %s\n' % (i, calculate_state(N, k)))
		
	inp.close()
	op.close()