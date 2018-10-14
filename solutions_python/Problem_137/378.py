#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, operator, string

test_content = open(sys.argv[1]).read().split('\n')
test_count = int(test_content[0])

def solution(R, C, M):

	tmp_R = R
	tmp_C = C

	board = [['.' for x in xrange(C)] for x in xrange(R)]
	board[0][0] = 'c'

	while min(R, C) > 2:
		if M >= min(R, C):
			# - R
			if R >= C:
				for x in xrange(C):
					board[R-1][C-1-x] = '*'
				M -= C
				R -= 1
			# - C	
			else:
				for x in xrange(R):
					board[x][C-1] = '*'
				M -= R
				C -= 1
		else:
			# R-2 + C-2 -1 >= M
			if R + C >= M + 5:
				# first fill in the last row, then last column
				if C-2 < M:
					for x in xrange(C-2):
						board[R-1][C-1-x] = '*'
					for x in xrange(M-C+2):
						board[R-2-x][C-1] = '*'
				# all fill in the last row
				else:
					for x in xrange(M):
						board[R-1][C-1-x] = '*'

				for x in xrange(tmp_R):
					for c in xrange(tmp_C):
						sys.stdout.write(board[x][c])
					sys.stdout.write('\n')
				return
			else:
				print 'Impossible'
				return
	if min(R, C) == 2:
		if M % 2 == 0 and R*C - M >= 4:
			if R == 2:
				for x in xrange(M/2):
					board[0][C-1-x] = '*'
					board[1][C-1-x] = '*'
			else:
				for x in xrange(M/2):
					board[R-1-x][0] = '*'
					board[R-1-x][1] = '*'
		elif R*C - M == 1:
			for x in xrange(R):
				for y in xrange(C):
					board[x][y] = '*'
			board[0][0] = 'c'
		else:
			print 'Impossible'
			return
	elif R == 1:
		for x in xrange(M):
			board[0][C-1-x] = '*'
	# C == 1
	else:
		for x in xrange(M):
			board[R-1-x][0] = '*'

	for x in xrange(tmp_R):
		for c in xrange(tmp_C):
			sys.stdout.write(board[x][c])
		sys.stdout.write('\n')
	

case_num = 1
position = 1
while case_num <= test_count:
	test_case = test_content[position].split()
	position += 1
	print 'Case #{0:d}:'.format(case_num)
	solution(int(test_case[0]), int(test_case[1]), int(test_case[2]))
	case_num += 1
