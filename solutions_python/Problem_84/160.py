#!/usr/bin/env python3

import sys
from pprint import pprint

T = int(sys.stdin.readline())
for t in range(T):
	print('Case #{}:'.format(t+1))
	R, C = map(int, sys.stdin.readline().split())
	matrix = []
	for r in range(R):
		matrix.append(list(sys.stdin.readline().strip()))
	try:
		for i in range(R):
			for j in range(C):
				if matrix[i][j] == '#' and matrix[i+1][j] == '#' \
						and matrix[i][j+1] == '#' and matrix[i+1][j+1] == '#':
					matrix[i][j] = '/'
					matrix[i+1][j] = '\\'
					matrix[i][j+1] = '\\'
					matrix[i+1][j+1] = '/'
				if matrix[i][j] == '#':
					raise ValueError
	except IndexError:
		print('Impossible')
	except ValueError:
		print('Impossible')
	else:
		print('\n'.join(map(lambda c: ''.join(c), matrix)))
