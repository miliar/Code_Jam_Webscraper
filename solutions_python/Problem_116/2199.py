#!/usr/bin/env python

import re
import sys


def read_file(filename):
	with open(filename, 'r') as f:
		lines = f.readlines()
		n = int(lines[0])

		boards = []
		for i in range(0, 5*n, 5):
			b = ""
			for j in range(1, 5):
				b += lines[i+j].strip()
			boards.append(b)

		return boards


def process(board):
	# Horizontal
	for n in range(0, 4*4, 4):
		row = board[n:n+4]
		if re.findall(r"[XT]{4}", row):
			return "X won"
		if re.findall(r"[OT]{4}", row):
			return "O won"

	# Vertical
	for n in range(0, 4):
		col = board[n:4*4:4]
		if re.findall(r"[XT]{4}", col):
			return "X won"
		if re.findall(r"[OT]{4}", col):
			return "O won"

	# Diagonal
	d1 = board[0:16:5]
	if re.findall(r"[XT]{4}", d1):
		return "X won"
	if re.findall(r"[OT]{4}", d1):
		return "O won"

	d2 = board[3:15:3]
	if re.findall(r"[XT]{4}", d2):
		return "X won"
	if re.findall(r"[OT]{4}", d2):
		return "O won"

	if "." in board:
		return "Game has not completed"
	else:
		return "Draw"



boards = read_file(sys.argv[1])

for i, board in enumerate(boards):
	result = process(board)
	print "Case #{0}: {1}".format(i+1, result)


