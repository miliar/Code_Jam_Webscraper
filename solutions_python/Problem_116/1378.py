#!/usr/bin/python

import sys

X = 'X'
O = 'O'
T = 'T'
B = '.'

def is_x(piece):
	return piece == X or piece == T

def is_o(piece):
	return piece == O or piece == T

def analyze_board(board, case_num):
	for y in xrange(4):
		if is_x(board[y][0]) and is_x(board[y][1]) and is_x(board[y][2]) and is_x(board[y][3]):
			print "Case #%(num)d: X won" % {"num": case_num + 1}
			return
		elif is_o(board[y][0]) and is_o(board[y][1]) and is_o(board[y][2]) and is_o(board[y][3]):
			print "Case #%(num)d: O won" % {"num": case_num + 1}
			return

	for x in xrange(4):
		if is_x(board[0][x]) and is_x(board[1][x]) and is_x(board[2][x]) and is_x(board[3][x]):
			print "Case #%(num)d: X won" % {"num": case_num + 1}
			return
		elif is_o(board[0][x]) and is_o(board[1][x]) and is_o(board[2][x]) and is_o(board[3][x]):
			print "Case #%(num)d: O won" % {"num": case_num + 1}
			return

	if is_x(board[0][0]) and is_x(board[1][1]) and is_x(board[2][2]) and is_x(board[3][3]):
		print "Case #%(num)d: X won" % {"num": case_num + 1}
		return
	elif is_o(board[0][0]) and is_o(board[1][1]) and is_o(board[2][2]) and is_o(board[3][3]):
		print "Case #%(num)d: O won" % {"num": case_num + 1}
		return

	if is_x(board[0][3]) and is_x(board[1][2]) and is_x(board[2][1]) and is_x(board[3][0]):
		print "Case #%(num)d: X won" % {"num": case_num + 1}
		return
	elif is_o(board[0][3]) and is_o(board[1][2]) and is_o(board[2][1]) and is_o(board[3][0]):
		print "Case #%(num)d: O won" % {"num": case_num + 1}
		return

	for x in xrange(4):
		for y in xrange(4):
			if board[y][x] == B:
				print "Case #%(num)d: Game has not completed" % {"num": case_num + 1}
				return
	else:
		print "Case #%(num)d: Draw" % {"num": case_num + 1}

def main():
	num_cases = int(raw_input())

	for i in xrange(num_cases):
		board = [0] * 4 
		for p in xrange(4):
			board[p] = raw_input()[:4]

		analyze_board(board, i)

		raw_input()

if __name__ == '__main__':
	main()