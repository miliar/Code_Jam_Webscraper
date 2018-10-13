#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, operator, string

test_content = open(sys.argv[1]).read().split('\n')
test_count = int(test_content[0])

def read_arr(list_of_arr):
	result = []
	for x in range(0, 4):
		result.append(list_of_arr[x].split())
	return result

def solution(test):
	case_num = 1
	position = 1
	while case_num <= test_count:
		first_ans = int(test[position])
		position += 1
		first_arr = test[position:position+4][first_ans-1].split()
		position += 4

		second_ans = int(test[position])
		position += 1
		second_arr = test[position:position+4][second_ans-1].split()
		position += 4

		result = intersectStrs(first_arr, second_arr)
		if len(result) > 1:
			print 'Case #{0:d}: Bad magician!'.format(case_num)
		elif len(result) == 1:
			print 'Case #{0:d}: {1}'.format(case_num, result[0])
		else:
			print 'Case #{0:d}: Volunteer cheated!'.format(case_num)
		case_num += 1

def intersectStrs(list1, list2):
	result_list = []
	for x in range(0, 4):
		for y in range(0, 4):
			if list1[x] == list2[y]:
				result_list.append(list1[x])
				break
	return result_list

solution(test_content)