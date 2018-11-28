#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, operator, string

test_content = open(sys.argv[1]).read().split('\n')
test_count = int(test_content[0])

def DW_solution(N, naomi, ken):
	naomi.sort()
	ken.sort()
	Cn_idx = 0

	n_max = N-1
	k_max = N-1
	while k_max >= 0 and naomi[n_max] < ken[k_max]:
		k_max -= 1

	n_head = N - (k_max + 1)
	k_head = 0
	points = k_max + 1
	while n_head < N:
		if naomi[n_head] < ken[k_head]:
			points -= 1
			n_head += 1
		else:
			n_head += 1
			k_head += 1
	return points

def W_solution(N, naomi, ken):
	naomi.sort()
	ken.sort()
	index = 0
	n = 0
	while n < N and index < N:
		if naomi[n] < ken[index]:
			n += 1
		index += 1

	return N - n



case_num = 1
position = 1
while case_num <= test_count:
	num_blk = int(test_content[position])
	position += 1
	naomi_blk = [float(i) for i in test_content[position].split()]
	position += 1
	ken_blk = [float(i) for i in test_content[position].split()]
	position += 1
	print 'Case #{0:d}: {1:d} {2:d}'.format(case_num, 
		DW_solution(num_blk, naomi_blk, ken_blk), W_solution(num_blk, naomi_blk, ken_blk))
	case_num += 1
