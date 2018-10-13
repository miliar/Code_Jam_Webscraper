#!/usr/bin/env python

import sys

wins = [
	[0, 1, 2, 3],
	[0, 5, 10, 15],
	[0, 4, 8, 12],
	[1, 5, 9, 13],
	[2, 6, 10, 14],
	[3, 7, 11, 15],
	[3, 6, 9, 12],
	[4, 5, 6, 7],
	[8, 9, 10, 11],
	[12, 13, 14, 15]
]

if len(sys.argv) > 1:
	input = sys.argv[1]
else:
	input = "input.txt"

try:
	with open(input) as f:
		content = f.readlines()
except:
	print("Can not find input file: %s" % input)
	sys.exit()

T = int(content[0])

case = 1
while case <= T:
	line = ((case - 1) * 5) + 1
	board = [list(row)[:-1] for row in content[line:line+4]]

	result = None
	for w in wins:
		items = set(board[int(slot / 4)][slot % 4] for slot in w)
		if len(items - set(('X', 'T'))) == 0:
			result = "X won"
		elif len(items - set(('O', 'T'))) == 0:
			result = "O won"

	if result == None:
		if not any('.' in sublist for sublist in board):
			result = "Draw"
		else:
			result = "Game has not completed"

	print("Case #%d: %s" % (case, result))

	case += 1
