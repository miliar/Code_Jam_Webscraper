#!/usr/bin/python

import sys
import math


def solve(R,C,arr):
	count = 0
	for i in range(R):
		for j in range(C):
			if arr[i][j] != '.':
				up = False
				down = False
				left = False
				right = False
				for k in range(0,i):
					if arr[k][j] != '.':
						up = True

				for k in range(i+1,R):
					if arr[k][j] != '.':
						down = True

				for k in range(0,j):
					if arr[i][k] != '.':
						left = True

				for k in range(j+1,C):
					if arr[i][k] != '.':
						right = True

				if not up and not down and not left and not right:
					return "Impossible"

				if not (arr[i][j] == '^' and up or arr[i][j] == 'v' and down or arr[i][j] == '<' and left or arr[i][j] == '>' and right):
					count += 1

	return count

if __name__ == "__main__":
	T = int(sys.stdin.readline())

	for t in range(T):
		#N = int(sys.stdin.readline())
		R, C = map(int, sys.stdin.readline().split())
		arr = []
		for r in range(R):
			arr.append(sys.stdin.readline().split()[0])
		#keyboard = sys.stdin.readline().split()[0]
		print "Case #{}: {}".format(t+1, solve(R,C,arr))