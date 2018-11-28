#!/usr/bin/python

import sys

boards = open(sys.argv[1], 'r')
rounds = boards.readline()

# For each round...
for round in range(0, int(rounds)):
	# Get the players first move
	firstguess = boards.readline()
	
	# Get the first game board
	board = []
	for i in range(0,4):
		board.append(boards.readline().split())

	# Record the row the player selected
	firstrow = board[int(firstguess)-1]

	# Get the players second move
	secondguess = boards.readline()

	# Get the second game board
	board = []
	for i in range(0,4):
		board.append(boards.readline().split())
	secondrow = board[int(secondguess)-1]

	matches = len(set(firstrow) & set(secondrow))

	if matches == 0:
		print "Case #" + str(round+1) + ": Volunteer cheated!"
	elif matches > 1:
		print "Case #" + str(round+1) + ": Bad magician!"
	elif matches == 1:
		print "Case #" + str(round+1) + ": " + (set(firstrow) & set(secondrow)).pop()

