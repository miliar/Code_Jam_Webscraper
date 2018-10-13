#! /usr/bin/env python

import sys

def analyze(grid):
	grid.append([grid[0][0], grid[1][0], grid[2][0], grid[3][0]])
	grid.append([grid[0][1], grid[1][1], grid[2][1], grid[3][1]])
	grid.append([grid[0][2], grid[1][2], grid[2][2], grid[3][2]])
	grid.append([grid[0][3], grid[1][3], grid[2][3], grid[3][3]])
	grid.append([grid[0][0], grid[1][1], grid[2][2], grid[3][3]])
	grid.append([grid[0][3], grid[1][2], grid[2][1], grid[3][0]])
	maybe_not_done = False
	for line in grid:
		line.sort()		
		if '.' in line:
			maybe_not_done = True
		if line == ['O', 'O', 'O', 'O'] or line == ['O', 'O', 'O', 'T']:
			return 'O won'
		if line == ['X', 'X', 'X', 'X'] or line == ['T', 'X', 'X', 'X']:
			return 'X won'
	if maybe_not_done:
		return "Game has not completed"
	return "Draw"

def main():
	cases = int(sys.stdin.readline().rstrip())
	for case in range(1, cases + 1):
		grid = []
		grid.append(list(sys.stdin.readline().rstrip()))
		grid.append(list(sys.stdin.readline().rstrip()))
		grid.append(list(sys.stdin.readline().rstrip()))
		grid.append(list(sys.stdin.readline().rstrip()))
		sys.stdin.readline()
		print "Case #%d: %s" % (case, analyze(grid))
	

if __name__ == "__main__":
	main()