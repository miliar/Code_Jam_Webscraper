#!/usr/bin/env python

FILE_NAME_BASE = 'A-small-attempt0'
NUM_PROCESSES = 0

def parse(inp):
	n, k = (int(x) for x in inp.readline().split())
	board = tuple(inp.readline().rstrip() for _ in xrange(n))
	return board, k

def rotate(board):
	# Instead of rotating the board clockwise, we rotate gravity
	# counter-clockwise.
	n = len(board)
	return tuple(
		line.replace('.', '').zfill(n)
		for line in board
		)

def findChain(board, length):
	n = len(board)
	winners = set()

	def followVector(x, y, dx, dy):
		prev = None
		count = None
		while 0 <= x < n and 0 <= y < n:
			piece = board[y][x]
			if piece == prev:
				count += 1
			else:
				prev = piece
				count = 1
			if count == length:
				winners.add(piece)
			x += dx
			y += dy

	for x in xrange(n):
		followVector(x, 0, 0, 1)
		followVector(x, 0, 1, 1)
		followVector(x, n - 1, 1, -1)
	for y in xrange(n):
		followVector(0, y, 1, 0)
		followVector(0, y, 1, 1)
		followVector(n - 1, y, -1, 1)

	return winners

def solve(board, k):
	rotatedBoard = rotate(board)
	if False:
		for line in board:
			print line
		print
		for line in rotatedBoard:
			print line
		print '---'
	winners = findChain(rotatedBoard, k)
	if 'R' in winners and 'B' in winners:
		return 'Both'
	elif 'R' not in winners and 'B' in winners:
		return 'Blue'
	elif 'R' in winners and 'B' not in winners:
		return 'Red'
	else:
		return 'Neither'

if __name__ == '__main__':
	inp = open(FILE_NAME_BASE + '.in', 'r')
	numCases = int(inp.readline())
	if NUM_PROCESSES == 0:
		results = [
			solve(*parse(inp))
			for _ in range(numCases)
			]
	else:
		from multiprocessing import Pool
		pool = Pool(NUM_PROCESSES)
		results = [
			pool.apply_async(solve, parse(inp))
			for _ in range(numCases)
			]
	inp.close()
	out = open(FILE_NAME_BASE + '.out', 'w')
	for case, result in enumerate(results):
		value = result if NUM_PROCESSES == 0 else result.get()
		out.write('Case #%d: %s\n' % (case + 1, value))
		out.flush()
	out.close()
