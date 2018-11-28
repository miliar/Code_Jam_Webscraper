#! /usr/bin/env python

from __future__ import print_function
from sys import stdin, stderr


debug = True

def debug_print(s):
	if debug:
		print('    DEBUG: {}'.format(s), file=stderr)


def solve(answer1, board1, answer2, board2):
	intersect = board1[answer1 - 1].intersection(board2[answer2 - 1])
	if len(intersect) == 0:
		return 'Volunteer cheated!'
	elif len(intersect) == 1:
		return list(intersect)[0]
	else:
		return 'Bad magician!'


if __name__ == '__main__':
	num_cases = int(stdin.readline().strip())

	for case in range(1, num_cases + 1):
		answer1, = [int(x) for x in stdin.readline().strip().split()]
		board1 = []
		for row in range(4):
			board1.append(set([int(x) for x in stdin.readline().strip().split()]))
		answer2, = [int(x) for x in stdin.readline().strip().split()]
		board2 = []
		for row in range(4):
			board2.append(set([int(x) for x in stdin.readline().strip().split()]))
		debug_print('  Answer 1: {}'.format(answer1))
		debug_print('  Board 1: {}'.format(board1))
		debug_print('  Answer 2: {}'.format(answer2))
		debug_print('  Board 2: {}'.format(board2))

		out = solve(answer1, board1, answer2, board2)
		print('Case #{}: {}'.format(case, out))

