#!/usr/bin/python
import sys

#solve case function
def solve_case(combine_list, opposed_list, element_string, case_number):
	result_list = []
	for ch in element_string:
		result_list.append(ch)
		if len(result_list) > 1:
			#check combine
			check_target = []
			check_target.append(result_list[len(result_list) - 1] + result_list[len(result_list) - 2])
			check_target.append(result_list[len(result_list) - 2] + result_list[len(result_list) - 1])
			for combine in combine_list:
				if (combine[0] == check_target[0]) or (combine[0] == check_target[1]):
					del result_list[len(result_list) - 1]
					del result_list[len(result_list) - 1]
					result_list.append(combine[1])
			#check opposed
			for opposed in opposed_list:
				if (opposed[0] in result_list) and (opposed[1] in result_list):
					result_list = []
	result_string = "["
	for ch in result_list:
		result_string += ch + ", "
	if result_string.endswith(", "):
		result_string = result_string[:len(result_string) - 2]
	result_string += "]"
	print "Case #" + str(case_number) + ": " + result_string
#main
r = sys.stdin

if len(sys.argv) > 1:
	r = open(sys.argv[1], 'r')

total_cases = r.readline()
for case_number in range(1, int(total_cases) + 1):
	case_string = r.readline().strip()
	case_list = case_string.split(' ')
	combine_list = []
	opposed_list = []
	for combine_index in range(0, int(case_list[0])):
		combine_list.append((case_list[combine_index + 1][0:2],case_list[combine_index + 1][2:]))
	for opposed_index in range(0, int(case_list[len(combine_list) + 1])):
		opposed_list.append(case_list[opposed_index + len(combine_list) + 2])
	element_index = case_list[len(combine_list) + len(opposed_list) + 2]
	element_string = case_list[len(combine_list) + len(opposed_list) + 3]
	solve_case(combine_list, opposed_list, element_string, case_number)

