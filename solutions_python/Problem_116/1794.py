#!/usr/bin/python

import sys
import itertools

empty_squares=['.']
full_squares=['X','O','T']

winning_positions = [
[0,1,2,3],
[4,5,6,7],
[8,9,10,11],
[12,13,14,15],
[0,4,8,12],
[1,5,9,13],
[2,6,10,14],
[3,7,11,15],
[0,5,10,15],
[12,9,6,3]
]

def is_winner(board, symbols):
	for w in winning_positions:
		winner=True
		for i in w:
			if board[i] not in symbols:
				winner=False
		if winner:
			return winner

def is_uncompleted(board):
	for i in board:
		if i in empty_squares:
			return True
	return False

def main():
	boards = []
	lines = [i.strip() for i in sys.stdin.readlines()]
	n_samples = int(lines[0])
	n_sample = 0
	for i in xrange(1,n_samples*5,5):
		n_sample+=1
		board=list(itertools.chain(*lines[i:i+4]))
		if is_winner(board, ['X','T']):
			print 'Case #{0}: X won'.format(n_sample)
		elif is_winner(board, ['O','T']):
			print 'Case #{0}: O won'.format(n_sample)
		elif is_uncompleted(board):
			print 'Case #{0}: Game has not completed'.format(n_sample)
		else:
			print 'Case #{0}: Draw'.format(n_sample)
		

if __name__ == '__main__':
    main()
