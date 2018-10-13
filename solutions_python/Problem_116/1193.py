#!/usr/bin/env python

from sys import argv

if len(argv) != 2:
	print 'Usage: %s filename' % argv[0]
	exit()

inp = []

with open(argv[1]) as f:
	for line in f:
		inp.append(line[:-1])

T = int(inp.pop(0))

cases = [inp[i:i+5] for i in range(0, len(inp), 5)]

for i in range(len(cases)):
	if len(cases[i]) == 5:
		cases[i] = cases[i][:-1]

def test_row(row, P):
	for square in row:
		if not square == P and not square == 'T':
			return False

	return True

def test_case(case):
	for i in range(4):
		col = []
		for row in case:
			col.append(row[i])

		flag = test_row(col, 'X')
		if flag:
			return 'X won'

		flag = test_row(col, 'O')
		if flag:
			return 'O won'

	for row in case:
		flag = test_row(row, 'X')
		if flag:
			return 'X won'

		flag = test_row(row, 'O')
		if flag:
			return 'O won'

	diag1 = []
	for i in range(4):
		diag1.append(case[i][i])

	if test_row(diag1, 'X'):
		return 'X won'
	if test_row(diag1, 'O'):
		return 'O won'

	diag2 = []
	for i in range(4):
		diag2.append(case[3-i][i])

	if test_row(diag2, 'X'):
		return 'X won'
	if test_row(diag2, 'O'):
		return 'O won'

	drawflag = True
	for row in case:
		for square in row:
			if square == '.':
				drawflag = False
	if drawflag:
		return 'Draw'

	return 'Game has not completed'

for i in range(T):
	print "Case #%s: %s" % (i+1, test_case(cases[i]))
