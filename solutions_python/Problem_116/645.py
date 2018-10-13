#!/usr/bin/env python

import sys

SQ_SIDE = 4

def translate(char):
	if char == 'O':
		return 1
	if char == 'X':
		return 2
	if char == '.':
		return 0
	if char == 'T':
		return 3

def winner(who):
	return ('O' if who == 1 else 'X') + ' won'

def checkDiagonal(mtrx):
	line = 3
	line2 = 3
	for i in range(SQ_SIDE):
		line = line & mtrx[i][i]
		line2 = line2 & mtrx[i][SQ_SIDE - 1 - i]
	if line != 0:
		return line
	if line2 != 0:
		return line2
	return 0

def checkVertical(mtrx):
	for i in range(SQ_SIDE):
		row = 3
		for j in range(SQ_SIDE):
			row = row & mtrx[j][i]
		if row != 0:
			return row
	return 0

def checkHorizontal(mtrx):
	for i in range(SQ_SIDE):
		line = 3
		for j in range(SQ_SIDE):
			line = line & mtrx[i][j]
		if line != 0:
			return line
	return 0

def checkBlanks(mtrx, blanks):
	if len(blanks) <= 0:
		return 0
	for i in blanks:
		mtrx[i[0]][i[1]] = 3
	h = checkHorizontal(mtrx)
	if h != 0:
		return h
	v = checkVertical(mtrx)
	if v != 0:
		return v
	d = checkDiagonal(mtrx)
	if d != 0:
		return d
	return 0

def solve():
	mtrx = [[0 for x in xrange(SQ_SIDE)] for x in xrange(SQ_SIDE)];
	result = 0
	hWinner = 0
	blanks = []
	for i in range(SQ_SIDE):
		line = sys.stdin.readline().strip()
		if line == '':
			line = sys.stdin.readline().strip()
		if hWinner != 0:
			continue
		lineadd = 3
		for j in range(SQ_SIDE):
			ch = translate(line[j])
			lineadd = lineadd & ch
			mtrx[i][j] = ch
			if ch == 0:
				blanks.append([i,j])
		if lineadd != 0:
			hWinner = winner(lineadd)
	if hWinner != 0:
		return winner(hWinner)
	v = checkVertical(mtrx)
	if v == 0:
		d = checkDiagonal(mtrx)
		if d == 0:
			b = checkBlanks(mtrx, blanks)
			if (b == 0):
				return "Draw"
			else:
				return "Game has not completed"
		else:
			return winner(d)
	else:
		return winner(v)
	return result

T = int(sys.stdin.readline())

for t in range(T):
	result = solve()
	print "Case #%d: %s" % (t+1, result)
