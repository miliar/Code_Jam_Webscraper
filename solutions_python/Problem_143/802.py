#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cj_2014_r1b_b.py
#  
#  Created by b00
#  
#  

# global - test cases
test_cases = 0

lottery = {}

import sys

def reader(filename):
	
	global test_cases
	
	with open(filename, 'r') as data_file:
		test_cases = int(data_file.readline())
		
		data = True
		
		test_case = 1
		
		while data:
			data = data_file.readline().strip()
			
			if data == '':
				continue
			
			lottery[test_case] = data
			
			test_case += 1

def solution(test_case):
	a, b, k = lottery[test_case].split(' ')
	
	all_winning_nums = []
	
	for old_machine_num in xrange(0, int(a)):
		for new_machine_num in xrange(0, int(b)):
			o_m_num = str(old_machine_num)
			n_m_num = str(new_machine_num)
			
			win_num = int(o_m_num) & int(n_m_num)
			
			all_winning_nums.append(win_num)
	
	possible_comb = 0
	for win_num in all_winning_nums:
		if win_num < int(k):
			possible_comb += 1
	
	return possible_comb

def main():
	
	try:
		# Input file
		filename = sys.argv[1]
	except IndexError:
		print('You do not give input file!')
		return 1
	
	reader(filename)
	
	for test_case in range(1, test_cases + 1):
		answer = solution(test_case)
		print('Case #' + str(test_case) + ': ' + str(answer))
	
	
	return 0

if __name__ == '__main__':
	main()
