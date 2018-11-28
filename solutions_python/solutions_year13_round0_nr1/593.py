#!/usr/bin/env python

from collections import Counter

def test_line_result(line):

	cnt = Counter(line)

	if cnt['X'] == 4 or (cnt['X'] == 3 and cnt['T'] == 1):
		return 'X'
	elif cnt['O'] == 4 or (cnt['O'] == 3 and cnt['T'] == 1):
		return 'O'

	return 'D'

def get_game_result(num_round, board):

	iscomplete = True

	# row by row
	for i in xrange(4):
		line = board[i]

		# must know whether or not it is completed
		if iscomplete and '.' in line:
			iscomplete = False

		result = test_line_result(line)
		if result != 'D':
			print 'Case #%s: %s won' % (num_round, result)
			return

	# column by column
	for i in xrange(4):
		line = map(lambda b: b[i], board)
		result = test_line_result(line)
		if result != 'D':
			print 'Case #%s: %s won' % (num_round, result)
			return

	# diagonal
	line = [board[0][0], board[1][1], board[2][2], board[3][3]]
	result = test_line_result(line)
	if result != 'D':
		print 'Case #%s: %s won' % (num_round, result)
		return

	# diagonal
	line = [board[0][3], board[1][2], board[2][1], board[3][0]]
	result = test_line_result(line)
	if result != 'D':
		print 'Case #%s: %s won' % (num_round, result)
		return

	if iscomplete:
		print 'Case #%s: Draw' % num_round
	else:
		print 'Case #%s: Game has not completed' % num_round


def main():

	test_data = None
	with open('input', 'r') as f:
		test_data = f.read()

	test_data = test_data.split('\n')

	num_test = int(test_data[0])
	test_data_ix = 1
	for test in xrange(num_test):
		board = []
		for i in xrange(4):
			board.append(test_data[test_data_ix])
			test_data_ix += 1

		get_game_result(test + 1, board)

		test_data_ix += 1

if __name__ == "__main__":
	main()