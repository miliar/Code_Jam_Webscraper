#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from numpy import array, rot90
import re

X = re.compile("[TX][TX][TX][TX]")
O = re.compile("[TO][TO][TO][TO]")

def columns(lines):
	a = ''.join([line[x] for x in range(4) for idx, line in enumerate(lines)])
	return a[0:4], a[4:8], a[8:12], a[12:16]

def diagonals(board):
	return [''.join(board.diagonal(x)) for x in range(-1, 2)] + [''.join(rot90(board).diagonal(x)) for x in range(-1, 2)]

if __name__ == "__main__":
	T = int(sys.stdin.readline())

	for idx in range(T):
		winner = None
		
		lines = [sys.stdin.readline().strip() for x in range(4)]
		board = array(map(list, lines))

		for line in lines:
			if X.match(line):
				winner = 'X'
			elif O.match(line):
				winner = 'O'

		for column in columns(lines):
			if X.match(column):
				winner = 'X'
			elif O.match(column):
				winner = 'O'

		for diagonal in diagonals(board):
			if X.match(diagonal):
				winner = 'X'
			elif O.match(diagonal):
				winner = 'O'

		if winner:
			res = "{winner} won".format(winner=winner)
		elif '.' in ''.join(lines):
			res = "Game has not completed"
		else:
			res = "Draw"

		print "Case #{n}: {res}".format(n=idx+1, res=res)

		sys.stdin.readline()		
