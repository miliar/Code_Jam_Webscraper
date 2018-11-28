#!/usr/bin/env python3

import sys

def analyse_board(board):
	dot_count = 0
	# Try horizontals
	for i in range(4):
		dot_count = dot_count + board[i].count('.')
		for player in ['X', 'O']:
			cnt = board[i].count(player) + board[i].count('T')
			#print('Line', i, 'for player', player, ':', cnt)
			if cnt == 4:
				return player + ' won'
	# Try verticals
	for i in range(4):
		for player in ['X', 'O']:
			cnt = 0
			for j in range(4):
				cnt = cnt + 1 if board[j][i] in [player, 'T'] else cnt
			#print('Vert', i, 'for player', player, ':', cnt)
			if cnt == 4:
				return player + ' won'

	# Try the diagonals:
	for player in ['X', 'O']:
		cnt = 0
		for i in range(4):
			cnt = cnt + 1 if board[i][i] in [player, 'T'] else cnt
		#print('Diag 1', 'for', player, ':', cnt)
		if cnt == 4:
			return player + ' won'
		cnt = 0
		for i,j in [(0,3), (1,2), (2,1), (3,0)]:
			cnt = cnt + 1 if board[i][j] in [player, 'T'] else cnt
		#print('Diag 2', 'for', player, ':', cnt)
		if cnt == 4:
			return player + ' won'

	if dot_count == 0:
		return 'Draw'

	return 'Game has not completed'

if __name__ == '__main__':
	ncases = int(sys.stdin.readline())
	for case in range(ncases):
		board = []
		for i in range(4):
			board.append(sys.stdin.readline().strip())
		result = analyse_board(board)
		print('Case #', case + 1, ': ', result, sep='')
		sys.stdin.readline()
