#! /usr/bin/env python

import os, sys, inspect
# realpath() with make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path:
	sys.path.insert(0, cmd_folder)

from collections import defaultdict


def check_straight(straight):	# (winner, has_empty)
	num_x = 0
	num_o = 0
	num_t = 0
	num_empty = 0
	for elem in straight:
		if(elem == 'X'):
			num_x += 1
		elif(elem == 'O'):
			num_o += 1
		elif(elem == 'T'):
			num_t += 1
		else:
			num_empty += 1

	winner = ''
	if(num_x >= 4 or (num_x >=3 and num_t >= 1)):
		winner = 'X'
	elif(num_o >= 4 or (num_o >=3 and num_t >= 1)):
		winner = 'O'

	return (winner, num_empty > 0)


def find_game_state(board):
	game_completed = True
	# find horizontal
	for row in board:
		(winner, has_empty) = check_straight(row)
		if(winner != ''):
			return winner
		if(has_empty):
			game_completed = False

	for i in range(4):
		straight = [board[0][i], board[1][i], board[2][i], board[3][i]]
		(winner, has_empty) = check_straight(straight)
		if(winner != ''):
			return winner
		if(has_empty):
			game_completed = False

	straight = [board[0][0], board[1][1], board[2][2], board[3][3]]
	(winner, has_empty) = check_straight(straight)
	if(winner != ''):
		return winner
	if(has_empty):
		game_completed = False

	straight = [board[0][3], board[1][2], board[2][1], board[3][0]]
	(winner, has_empty) = check_straight(straight)
	if(winner != ''):
		return winner
	if(has_empty):
		game_completed = False

	return game_completed


def main(argv):
	in_file_path = argv[1]
	in_file = open(in_file_path, 'rb')

	out_file_path = '%s.out' % in_file_path
	out_file = open(out_file_path, 'wb')

	T = int(in_file.readline())
	for case_num in range(T):
		board = list()
		for i in range(4):
			row_str = in_file.readline()
			row = list()
			for i in range(4):
				row.append(row_str[i])
			board.append(row)
		in_file.readline()	# empty line

		state = find_game_state(board)

		if(state == 'X'):
			out_file.write('Case #%d: X won\n' % (case_num+1))
		elif(state == 'O'):
			out_file.write('Case #%d: O won\n' % (case_num+1))
		elif(state == False):
			out_file.write('Case #%d: Game has not completed\n' % (case_num+1))
		elif(state == True):
			out_file.write('Case #%d: Draw\n' % (case_num+1))
		else:
			print '[Warning] Should never reach this case'


if(__name__ == '__main__'):
	ret = main(sys.argv)
	sys.exit(ret)

