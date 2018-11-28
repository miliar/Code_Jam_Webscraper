#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, operator, string

test_content = open(sys.argv[1]).read().split('\n')
test_count = int(test_content[0])

def solution(C, F, X):
	rate = 2.0
	opt = [X/rate]
	farm_time = 0.0
	farm_count = 0
	while True:
		farm_time += C/(rate + farm_count*F)
		farm_count += 1
		opt.append(farm_time + X/(rate + farm_count*F))
		if opt[farm_count] >= opt[farm_count-1]:
			break
	return opt[farm_count-1]


case_num = 1
position = 1
while case_num <= test_count:
	test_case = test_content[position].split()
	position += 1
	print 'Case #{0:d}: {1:f}'.format(case_num, solution(float(test_case[0]), float(test_case[1]), float(test_case[2])))
	case_num += 1
