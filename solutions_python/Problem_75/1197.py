#!/usr/bin/env python
# encoding: utf-8
"""
ProblemB.py

Created by Angus Fletcher on 2011-05-07.
"""

import sys
import os

#The number of cases we'll have.
t = int(sys.stdin.readline())

#For each test case
for i in range(0, t, 1):
	elem_combinations = []
	elem_oppositions = []
	test_case_string = sys.stdin.readline().strip('\n')
	test_case_string = test_case_string.split(' ')
	num_combinations = int(test_case_string.pop(0))

	#Pull the number of combinations, add them to a tuple
	for j in range(0, num_combinations, 1):
		curr_combination = test_case_string.pop(0)
		curr_combination = (curr_combination[:2], curr_combination[2])
		elem_combinations.append(curr_combination)
	
	num_oppositions = int(test_case_string.pop(0))
	
	#Pull the number of combinations, add them to a tuple.
	for k in range(0, num_oppositions, 1):
		curr_opposition = test_case_string.pop(0)
		curr_opposition
		elem_oppositions.append(curr_opposition)
		
	invocation_length = int(test_case_string.pop(0))
	
	curr_invocation = test_case_string.pop(0)
	
	new_invocation = ""
	
	for slice_index in range(0, len(curr_invocation), 1):
		current_slice = curr_invocation[slice_index:slice_index+1]
		comb_found = False
		if len(new_invocation) == 0:
			new_invocation += current_slice
		else:
			poss_comb = new_invocation[-1] + current_slice
			for comb in elem_combinations:
				if poss_comb == comb[0] or poss_comb[::-1] == comb[0]:
					new_invocation = new_invocation[:-1] + comb[1]
					comb_found = True
					break
			if not comb_found:
				new_invocation += current_slice
				
			for opp in elem_oppositions:
				#Check to see if this character is in an opposition
				if new_invocation.find(opp[0]) >= 0 and new_invocation.find(opp[1]) >= 0:
					new_invocation = ""
	
	case_string = "Case #" + str(i+1) + ": "
	
	new_invocation = list(new_invocation)
	
	case_string += str(new_invocation).replace('\'', '' )
		
	print case_string
	