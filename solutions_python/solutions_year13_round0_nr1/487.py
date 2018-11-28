#!/usr/bin/python

# vim: set expandtab shiftwidth=4 tabstop=4:


sample_input = """6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O
"""

sample_output = """Case #1: X won
Case #2: Draw
Case #3: Game has not completed
Case #4: O won
Case #5: O won
Case #6: O won
"""

DIM = 4
O_WON = 'O won'
X_WON = 'X won'
DRAW = 'Draw'
NC = 'Game has not completed'

def solve_one(input_str):
	input_str = input_str.replace('\n', '')
	# check lines

	def check_win(stripe, player):
		if stripe.replace('T', player) == player*DIM:
			return True
		return False

	for n in range(DIM):
		off = n*DIM
		row = input_str[off:off+DIM]
		if check_win(row, 'X'):
			return X_WON
		if check_win(row, 'O'):
			return O_WON

		col = ''
		for c in range(DIM):
			off = n+c*DIM
			col += input_str[off]
		if check_win(col, 'X'):
			return X_WON
		if check_win(col, 'O'):
			return O_WON

	diag = ''
	for n in range(DIM):
		off = n*DIM+n
		diag += input_str[off]

	if check_win(diag, 'X'):
		return X_WON
	if check_win(diag, 'O'):
		return O_WON

	diag = ''
	for n in range(DIM):
		off = n*DIM+DIM-n-1
		diag += input_str[off]

	if check_win(diag, 'X'):
		return X_WON
	if check_win(diag, 'O'):
		return O_WON

	if '.' in input_str:
		return NC
	else:
		return DRAW

def solve_all(input_file):
	header = input_file.readline().strip()
	count = int(header)

	for i in range(1, count+1):
		problem_str = input_file.read(DIM*DIM+DIM)
		print 'Case #{}: {}'.format(i, solve_one(problem_str))
		input_file.readline() # discard empty line

import StringIO
import sys
#f = StringIO.StringIO(sample_input)

solve_all(open(sys.argv[1]))
