#!/usr/bin/python

from optparse import OptionParser , SUPPRESS_HELP
import os
import re
import sys

usage = "usage: %prog [options]"
description = """CodeJam tic tac toe"""
parser = OptionParser(usage, description=description)
(options, args) = parser.parse_args()

if len(args) != 1:
	print "Need a file for input"
	exit()

row = 1
boards = []
current_board = []

with open(args[0], 'r') as f:
	linenum = 1
	for line in f:
		if linenum == 1:
			T = linenum
		elif line.strip():
			current_board.append(line.strip())
			if row >= 4:
				#print "\n".join(current_board)
				boards.append(current_board)
				current_board = []
				row = 0
			row += 1
		linenum += 1

def letter_won(letter, board):
	# rows
	for i in range(0, 4):
		invalid_found = False
		for j in range(0, 4):
			invalid_found = invalid_found or board[i][j] not in ('T', letter)
		if not invalid_found:
			return True

	# cols
	for i in range(0, 4):
		invalid_found = False
		for j in range(0, 4):
			invalid_found = invalid_found or board[j][i] not in ('T', letter)
		if not invalid_found:
			return True

	# diags
	# 0,0 0,1 0,2 0,3
	# 1,0 1,1 1,2 1,3
	# 2,0 2,1 2,2 2,3
	# 3,0 3,1 3,2 3,3
	invalid_found = False
	for i in range(0, 4):
		invalid_found = invalid_found or board[i][i] not in ('T', letter)
	if not invalid_found:
		return True

	invalid_found = False
	for i in range(0, 4):
		invalid_found = invalid_found or board[3-i][i] not in ('T', letter)
	if not invalid_found:
		return True

	return False

def blank_space(board):
	return '.' in ''.join(board)

def evaluate(board):
	if letter_won('X', board):
		return 'X won'
	elif letter_won('O', board):
		return 'O won'
	elif blank_space(board):
		return 'Game has not completed'
	else:
		return 'Draw'

case_num = 1

with open('out.txt','w') as f:
	for board in boards:
		f.write("Case #%s: %s\n" % (case_num, evaluate(board)))
		case_num += 1
	f.write('\n')
