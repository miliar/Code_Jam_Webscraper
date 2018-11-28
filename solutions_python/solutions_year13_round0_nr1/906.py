#! c:\python33\python.exe

import sys

WC = "T"

input = open( sys.argv[1], "r" )
output = open( sys.argv[2], "w" )

tc_count = int( input.readline().rstrip() )

def hasFreeSpaces( board ):

	for i in board:
		if "." in i:
			return True
			
	return False

def playerWon( player, board ):
	print( "board: {} ".format( board ) )
	diag_one = []
	diag_two = []
	
	for i in range( len(board) ):
		print ( "i {}".format( i ) )
		diag_one.append( board[i][i] )
		diag_two.append( board[-i -1][i] )
		
	#check diag
	for i in ( diag_one, diag_two ):
		if i.count( player ) + i.count( WC ) == len( i ):
			return True
	
	#check horiz
	for i in board:
		if i.count( player ) + i.count( WC ) == len( i ):
			return True
			
	#check vert
	for y in range( len(board) ):
		pc = 0
		for x in range( len(board) ):
			if board[x][y] == player or board[x][y] == WC:
				pc += 1
			
		if pc == len( board ):
			return True

def getWinner(board):
	
	if playerWon( "X", board ):
		return "X won"
		
	if playerWon( "O", board ):
		return "O won"
		
	if hasFreeSpaces( board ):
		return "Game has not completed"
		
	return "Draw"

for i in range( 1, tc_count + 1 ):

	board = []
	for j in range(4):
		board.append( input.readline().rstrip() )
		
	input.readline() # throw away extra line
		
	winner = getWinner(board)
	output.write( "Case #{}: {}\n".format( i, winner ) )
	
input.close()
output.close()