#!/usr/bin/python
#This program requires python ver 2.6 or higher. (itertools.combinations)
import sys
import itertools

#solve case function
def solve_case(candy_list, case_number):
	maximum_sum = -1
	for select in range(1, (len(candy_list) / 2) + 1):
		candidate_list = list(itertools.combinations(candy_list, select))
		for left_list in candidate_list:
			right_list = candy_list[:]
			for x in left_list:
				right_list.remove(x)
			left_xor_sum = 0
			for l in left_list:
				left_xor_sum ^= l
			right_xor_sum = 0
			for r in right_list:
				right_xor_sum ^= r
			if left_xor_sum == right_xor_sum:
				left_sum = sum(left_list)
				right_sum = sum(right_list)
				if left_sum > right_sum and left_sum > maximum_sum:
					maximum_sum = left_sum
				elif right_sum > maximum_sum:
					maximum_sum = right_sum
	if maximum_sum > 0:
		print "Case #" + str(case_number) +": " + str(maximum_sum)
	else:
		print "Case #" + str(case_number) +": NO"

#main
r = sys.stdin

if len(sys.argv) > 1:
	r = open(sys.argv[1], 'r')

total_cases = r.readline()
for case_number in range(1, int(total_cases) + 1):
	candy_length = int(r.readline().strip())
	candy_string = r.readline().strip()
	candy_string_list = candy_string.split(' ')
	candy_list = []
	for string in candy_string_list:
		candy_list.append(int(string))
	solve_case(candy_list, case_number)

