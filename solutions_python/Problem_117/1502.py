#!/bin/env python
#-*- coding: utf_8 -*-


#############
# functions #
#############
def possible (pattern, row_num, col_num):
	rows_cut = []
	for row in range (row_num):
		row_ok = True
		for col in range (col_num):
			if pattern[row][col] != 1:
				row_ok = False
				break
		if row_ok:
			rows_cut.append (row)
	cols_cut = []
	for col in range (col_num):
		col_ok = True
		for row in range (row_num):
			if pattern[row][col] != 1:
				col_ok = False
				break
		if col_ok:
			cols_cut.append (col)
	for row_cut in rows_cut:
		for col in range (col_num):
			pattern[row_cut][col] = 0
	for col_cut in cols_cut:
		for row in range (row_num):
			pattern[row][col_cut] = 0
	for row in range (row_num):
		for col in range (col_num):
			if pattern[row][col] == 1:
				return False
	return True


import sys
if len (sys.argv) > 1:
	sys.stdin = open (sys.argv[1], 'r')


for case in range (int (raw_input().strip())):
	case += 1
	row_num, col_num = map (lambda x: int (x), raw_input().rstrip().split())
	pattern = []
	for row in range (row_num):
		pattern.append (map (lambda x: int (x), raw_input().rstrip().split()))
	print 'Case #%d: %s' % (case, 'YES' if possible (pattern, row_num, col_num) else 'NO')
