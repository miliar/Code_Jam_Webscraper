#!/usr/bin/env python

import sys, re

re_x_wins = re.compile ('((.{4})*[XT]{4}|.*([XT].{3}){3}[XT]|([XT].{4}){3}[XT]|.{3}([XT].{2}){3}[XT])', re.IGNORECASE)

re_o_wins = re.compile ('((.{4})*[OT]{4}|.*([OT].{3}){3}[OT]|([OT].{4}){3}[OT]|.{3}([OT].{2}){3}[OT])', re.IGNORECASE)

re_incomplete = re.compile ('.*[.].*[.]')

def solve (casenum, board):
	result = "??"

	if (re_x_wins.match (board)):
		result = "X won"
	elif (re_o_wins.match (board)):
		result = "O won"
	elif (re_incomplete.match (board)):
		result = "Game has not completed"
	else:
		result = "Draw"
		
	print "Case #%d: %s" % (casenum, result)


num_testcases = int (sys.stdin.readline())

for case in range (1, num_testcases+1):
	board = ""
	for row in range (1, 5):
		board += sys.stdin.readline().strip()

	sys.stdin.readline()
	#print board, "\n\n"
	solve (case, board)
