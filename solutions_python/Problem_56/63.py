#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Google Code Jam: Round 1A 2010
# Problem A: 

T = int(input()) # number of test cases

for t in range(1,T+1):
	print('Case #{0}: '.format(t), end='')
	N, K = [ int(x) for x in input().strip().split(' ') ]
	board = []
	for n in range(N):
		board.append(list(input()))
		#print(board[-1])

	board_r = [ [0]*N for n in range(N) ]

	for y in range(N):
		for x in range(N):
			board_r[y][x] = board[N-1 - x][y]

	changed = True
	while changed:
		changed = False
		for y in range(N-1, 0, -1):
			for x in range(N):
				if board_r[y][x] == '.' and board_r[y-1][x] != '.':
					board_r[y][x] = board_r[y-1][x]
					board_r[y-1][x] = '.'
					changed = True

	result = {}
	result['R'] = False
	result['B'] = False

	"""
	print()
	for b in board:
		print(b)
	print('---')
	for b in board_r:
		print(b)
	"""

	for y in range(N):
		for x in range(N):
			if board_r[y][x] != '.':
				dirs = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
				for d in dirs:
					ny = y + (K-1)*d[0]
					nx = x + (K-1)*d[1]
					if ny < 0 or ny >= N:
						continue
					if nx < 0 or nx >= N:
						continue
					bad = False
					for k in range(K):
						ny = y + k*d[0]
						nx = x + k*d[1]
						if board_r[ny][nx] != board_r[y][x]:
							bad = True
							break
					if not bad:
						result[board_r[y][x]] = True

	if result['R']:
		if result['B']:
			print('Both')
		else:
			print('Red')
	else:
		if result['B']:
			print('Blue')
		else:
			print('Neither')
