#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  cj_2017_qual_b.py
#  
#  Copyright 2017 b00
#  

import sys

def find_tidy_num(N):
	n = N
	
	while n >= 1:
		# check if current num is tidy
		# if num less than 10, return the num
		if n < 10:
			return n
		
		# make single digits array from num
		n_array = list(map(int, str(n)))
		
		# search for leftmost zero
		try:
			zero_index = n_array.index(0)
		except ValueError:
			zero_index = None
		
		# if zero exists and isn't 
		if zero_index:
			# change all right side digits to zeros (if index isn't the rightmost one)
			if zero_index < len(n_array) - 1:
				n_array[zero_index:] = [0] * (len(n_array) - zero_index)
			# change all left side ones to zeros too (except very first digit)
			zero_l_index = zero_index - 1
			while zero_l_index != 0 and n_array[zero_l_index] == 1:
				n_array[zero_l_index] = 0
				zero_l_index -= 1
			# substract one
			n = int(''.join(map(str,n_array)))
			n -= 1
			n_array = list(map(int, str(n)))
		
		# check condition for every digit
		i = 0
		n_tmp = n
		while i < len(n_array) - 1:
			if n_array[i] > n_array[i + 1]:
				n -= 1
				break
			
			i += 1
		
		if n == n_tmp:
			return n

def main():
	
	T = None
	t = 1
	
	for line in sys.stdin:
		if not T:
			T = int(line.strip())
		else:
			N = int(line.strip())
			tn = find_tidy_num(N)
			
			print('Case #%i: %i' % (t, tn))
			
			t += 1
	
	return 0

if __name__ == '__main__':
	main()

