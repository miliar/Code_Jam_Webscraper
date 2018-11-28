# Qualification Round : Problem A

import sys
import os

def ReadBoards(filename,boardsize):
	if not os.path.exists(filename):
	   sys.exit('ERROR: could not open input file')

	f = open(filename,'r')

	boards = []

	count = int(f.readline())

	for i in range(count):
		bstr = ''
		j = 0
		stemp = ''
		while j < boardSize:
			stemp = f.readline()
			if len(stemp) == 0:
				break # EOF
			stemp = stemp.strip()
			if stemp:
				bstr += stemp
				j    += 1
		if len(stemp) == 0:
			break # EOF
		boards.append(bstr)

	f.close()

	if count != len(boards):
		sys.exit('ERROR: only found %d/%d boards' % (len(boards),count))

	return boards

def DetermineOutcome( bstr, boardSize ):
	boardFilled = True
	count = 0

	oLine = False
	xLine = False

	xFull = ord('X') * boardSize
	oFull = ord('O') * boardSize
	xWithT = ord('X') * (boardSize-1) + ord('T')
	oWithT = ord('O') * (boardSize-1) + ord('T')

	# sum columns and rows
	for i in range(boardSize):
		rowSum = 0
		colSum = 0

		for j in range(boardSize):
			col = bstr[i*boardSize+j]
			row = bstr[j*boardSize+i]

            # determine if board is full of player moves
			boardFilled = boardFilled and (col == 'O' or col == 'X' or col == 'T') and (row == 'O' or row == 'X' or row == 'T')
			count = count + 1

			rowSum += ord(col)
			colSum += ord(row)

		oLine = oLine or (rowSum == oFull) or (rowSum == oWithT) or (colSum == oFull) or (colSum == oWithT)
		xLine = xLine or (rowSum == xFull) or (rowSum == xWithT) or (colSum == xFull) or (colSum == xWithT)

		if xLine or oLine:
			break

    # sum diagonals
 	NegativeDiagonal = 0
	PostiveDiagonal  = 0

	for i in range(boardSize):
		pos = bstr[i*boardSize+i]
		neg = bstr[i*boardSize+(boardSize-i-1)]

		NegativeDiagonal += ord(neg)
		PostiveDiagonal  += ord(pos)

	oLine = oLine or (NegativeDiagonal == oFull) or (NegativeDiagonal == oWithT) or (PostiveDiagonal == oFull) or (PostiveDiagonal == oWithT)
	xLine = xLine or (NegativeDiagonal == xFull) or (NegativeDiagonal == xWithT) or (PostiveDiagonal == xFull) or (PostiveDiagonal == xWithT)

	if (xLine and oLine) or (boardFilled and count == 16):
		return 'Draw'
	elif xLine:
		return 'X won'
	elif oLine:
		return 'O won'
	else:
		return 'Game has not completed'

filename = sys.argv[1]
outputFile = sys.argv[2]
boardSize = 4

f = open(outputFile,'w')

boards = ReadBoards(filename,boardSize)
for i in range(len(boards)):
	f.write("Case #%s: %s" % (i+1, DetermineOutcome(boards[i],boardSize))) 
	f.write('\n')

f.close()