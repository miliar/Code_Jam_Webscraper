#!/usr/bin/env python

def main():
	with open('c:\Users\Kornelijus\Downloads\A-large.in', 'r') as f:
		count = int(f.readline())

		for i in xrange(count):
			case = f.readline().strip() + f.readline().strip() + f.readline().strip() + f.readline().strip() 

			f.readline()

			print 'Case #%d: %s' % (i + 1, check(case))

def row(x):
	return ((0, x), (1, x), (2, x), (3, x))

def col(x):
	return ((x, 0), (x, 1), (x, 2), (x, 3))

def check(board):
	tja = [
		row(0), row(1), row(2), row(3),

		((0, 0), (1, 1), (2, 2), (3, 3)),
		((0, 3), (1, 2), (2, 1), (3, 0)),

		col(0), col(1), col(2), col(3)
	]

	for pos in tja:
		letters = [board[x + y*4] for x,y in pos]
		hej = set(letters)
		
		if '.' in hej:
			continue

		if len(hej & {'X', 'O'}) == 1:
			return '%s won' % ('X' if 'X' in hej else 'O')

	if '.' in board:
		return 'Game has not completed'
	else:
		return 'Draw'

if __name__ == '__main__':
	main()
