#!/usr/bin/python 

import re

# REMOVE DEBUG FLAG BEFORE SUBMIT **********************
debugOutput = False
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

xPiece = 'X'
oPiece = 'O'
emptyPiece = '.'
xWonMsg = "X won"
oWonMsg = "O won"
drawMsg = "Draw"
inPlayMsg = "Game has not completed"


maxTestCases = 0
boardSize = 4
gameBoard = []
matchFound = None

#######################################################################
# FUNCTIONS
#######################################################################
def dumpInput(num):
	for x in xrange(0, num):
		if debugOutput:
			print raw_input()

def checkBoard():
	emptySlots = False 

	for c in xrange(0, boardSize):
		#Check Vertical
		checkVertLine = gameBoard[0][c] +gameBoard[1][c] + gameBoard[2][c] + gameBoard[3][c] 

		if re.match("[XT]{4}", checkVertLine): 
			return xWonMsg

		if re.match("[OT]{4}", checkVertLine): 
			return oWonMsg
		
		if emptyPiece in checkVertLine:
			emptySlots = True
	
	# Check diagonal
	checkDiagRtLine = gameBoard[0][0] +gameBoard[1][1] + gameBoard[2][2] + gameBoard[3][3] 
	checkDiagLtLine = gameBoard[0][3] +gameBoard[1][2] + gameBoard[2][1] + gameBoard[3][0] 
	
	if re.match("[XT]{4}", checkDiagRtLine) or re.match("[XT]{4}", checkDiagLtLine): 
		return xWonMsg
	
	if re.match("[OT]{4}", checkDiagRtLine) or re.match("[OT]{4}", checkDiagLtLine): 
		return oWonMsg

	if emptySlots:
		return inPlayMsg 
	else:
		return drawMsg
#************************************************************************
# END FUNCTION
#************************************************************************

maxTestCases = int(raw_input().strip())

for testCase in xrange(1, maxTestCases+1):
	gameBoard = []
	matchFound = None
	msg = inPlayMsg

	#Read current board from input
	for r in xrange(0, boardSize):
		gameBoard.append(raw_input().strip())

		# Check for horizontal matches
		if re.match("[XT]{4}", gameBoard[r]): 
			matchFound = 'X'
			msg = xWonMsg
		elif re.match("[OT]{4}", gameBoard[r]): 
			matchFound = 'Y'
			msg = oWonMsg

		if debugOutput:
			print gameBoard[r]
			
			if matchFound:
				dumpInput(boardSize - (r+1))
				break

	if testCase != maxTestCases:
		discardLine = raw_input()

	if not matchFound:
		msg = checkBoard()

	print "Case #{}: {}".format(testCase, msg)

	if debugOutput:
		print
