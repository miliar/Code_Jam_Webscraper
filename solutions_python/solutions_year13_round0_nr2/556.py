import sys

from math import log, floor, ceil
from itertools import takewhile, imap, count

def is_accessible(i, j, board):
	height = board[i][j]
	line = board[i]
	col = (line[j] for line in board)

	less_than_height = lambda n: n <= height
	return all(map(less_than_height, line)) or all(map(less_than_height, col))

def parse_case(inp):
	n, m = map(int, inp.readline().split())
	lawn = [map(int, inp.readline().split()) for _ in range(n)]
	for line in lawn:
		assert len(line) == m
	
	positions = ((i, j) for i in range(n) for j in range(m))

	if all(map(lambda (i, j): is_accessible(i, j, lawn), positions)):
		return "YES"
	else:
		return "NO"

def parse(fileName):
	results = []
	with open(fileName) as f:
		cases = int(f.readline())
		for i in range(cases):
			results.append(parse_case(f))

		next_line = f.readline()
		assert "" == next_line, "Unexpected line: %s" % next_line
	return results

if __name__ == "__main__":
	for (i, result) in enumerate(parse(sys.argv[1])):
		print "Case #%d: %s" % (i + 1, result)
