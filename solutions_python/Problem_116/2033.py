#!/usr/bin/env python

import sys

def solve( board ):
	'''
	takes 4x4 of char (X,T,O,.) and outputs string Case #[\d]: (X won, Draw, O won, Game has not complete)
	Win condition 4 in a row of [X|O] or 3 in a row of [X|O] and T in that same row.
	Draw - There is no empty points, but no winner
	GNC - No win with empty points
	'''
#	print "Board:",board
	mapX = {'T':1,'X':2,'O':0,'.':0}
	mapO = {'T':1,'X':0,'O':2,'.':0}
	#Diag
	check = 1
	check2 = 1
	for x in range(4):
#		print "checking<",x,",",x,">:",board[x][x]
		check *= mapX[board[x][x]]
		check2 *= mapO[board[x][x]]
#	print "check",check
#	print "check2",check2
	if( check != 0 ):
		return "X won"
	if( check2 != 0 ):
		return "O won"
	check = 1
	check2 = 1
	for y in range(4):
#		print "checking<",y,",",y,">:",board[y][3-y]
		check *= mapX[board[y][3-y]]
		check2 *= mapO[board[y][3-y]]
#		print "check",check
#		print "check2",check2
	if( check != 0 ):
		return "X won"
	if( check2 != 0 ):
		return "O won"
	#Hor
	for x in range(4):
		check = 1
		check2 = 1
		for y in range(4):
			check *= mapX[board[x][y]]
			check2 *= mapO[board[x][y]]
#		print "check",check
#		print "check2",check2
		if( check != 0 ):
			return "X won"
		if( check2 != 0 ):
			return "O won"
	#Ver
	check = 1
	for x in range(4):
		check = 1
		check2 = 1
		for y in range(4):
			check *= mapX[board[y][x]]
			check2 *= mapO[board[y][x]]
#		print "check",check
#		print "check2",check2
		if( check != 0 ):
			return "X won"
		if( check2 != 0 ):
			return "O won"
	#Empty Search
	for x in range(4):
		for y in range(4):
			if( board[x][y] == '.' ):
				return "Game has not completed"
	return "Draw"
	

def run():
	if len(sys.argv) < 2:
		print "Missing arg"
	else:
		f = open(sys.argv[1],'r')
		data = f.read().split("\n")
		f.close()
		line_pos = 1
		number_of_tests = int(data[0])
		for x in range(number_of_tests):
			current_board = []
			for y in range(4):
				current_board.append(data[line_pos][:4])
				line_pos += 1
#			print current_board
			line_pos += 1
			print "Case #" + str(x+1) + ": " + solve( current_board )


if __name__ == "__main__":
	run()
