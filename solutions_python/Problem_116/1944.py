#!/usr/bin/python
#
# Tic-Tac-Toe-Tomek
import sys

if len(sys.argv) != 2:
	print "Usage: tttt.py <input file>"
	exit()

try:
	f = open( sys.argv[1], 'r' )
except:
	print "Could not open the file: " + sys.argv[1]
	exit()

def is_player(space, player):
	if space == player or space == 'T':
		return True
	return False

def player_won(game, player):
	for i in game:
		if is_player(i[0], player) and \
		   is_player(i[1], player) and \
		   is_player(i[2], player) and \
		   is_player(i[3], player):
			return True

	for i in range(0, 4):
		if is_player(game[0][i], player) and \
		   is_player(game[1][i], player) and \
		   is_player(game[2][i], player) and \
		   is_player(game[3][i], player):
			return True
	
	if is_player(game[0][0], player) and \
	   is_player(game[1][1], player) and \
	   is_player(game[2][2], player) and \
	   is_player(game[3][3], player):
		   return True
	
	if is_player(game[0][3], player) and \
	   is_player(game[1][2], player) and \
	   is_player(game[2][1], player) and \
	   is_player(game[3][0], player):
		   return True

	return False

def game_full(game):
	for i in game:
		for j in i:
			if j == '.':
				return False
	return True

num_games = int(f.readline())



for i in range(0, num_games):
	game = [f.readline(),f.readline(),f.readline(),f.readline()]

	print 'Case #' + str(i+1) + ':',
	if player_won(game, 'X'):
		print 'X won'
	elif player_won(game, 'O'):
		print 'O won'
	elif game_full(game):
		print 'Draw'
	else:
		print 'Game has not completed'

	f.readline() #clear empty line
