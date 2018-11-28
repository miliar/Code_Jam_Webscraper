#!/usr/bin/env python

import sys

def checkRow(board):

	for i in range(4):
		countX = 0
		countO = 0
		
		for j in range(4):
			c = board[i][j]
			if c == "X" or c == "T":
				countX += 1

			if c == "O" or c == "T":
				countO += 1
	

		if countX == 4:
			return "X"
		if countO == 4:
			return "O"

	return 0


def checkCol(board):

	for i in range(4):
		countX = 0
		countO = 0
		
		for j in range(4):
			c = board[j][i]
			if c == "X" or c == "T":
				countX += 1

			if c == "O" or c == "T":
				countO += 1
	

		if countX == 4:
			return "X"
		if countO == 4:
			return "O"

	return 0

def checkDial(board):

	countX = 0
	countO = 0
	
	for j in range(4):
		c = board[j][j]
		if c == "X" or c == "T":
			countX += 1

		if c == "O" or c == "T":
			countO += 1
	

	if countX == 4:
		return "X"
	if countO == 4:
		return "O"

	countX = 0
	countO = 0
	
	for j in range(4):
		c = board[3-j][j]
		if c == "X" or c == "T":
			countX += 1

		if c == "O" or c == "T":
			countO += 1
	

	if countX == 4:
		return "X"
	if countO == 4:
		return "O"


	return 0





def main():
	inp = sys.argv[1]
	out = sys.argv[2]

	fhInp = open(inp)
	fhOut = open(out, 'w')
	num = int(fhInp.readline().strip())
	
	for i in range(num):
		board = []
		fhOut.write("Case #" + str(i+1) + ": ")
		
		for j in range(4):
			line = list(fhInp.readline().strip())
			board.append(line)

		fhInp.readline()
		
		
		ret = checkRow(board)
		if ret == "X":
			fhOut.write("X won\n")
			continue
		if ret == "O":
			fhOut.write("O won\n")
			continue
		
		ret = checkCol(board)
		if ret == "X":
			fhOut.write("X won\n")
			continue
		if ret == "O":
			fhOut.write("O won\n")
			continue
		
		ret = checkDial(board)
		if ret == "X":
			fhOut.write("X won\n")
			continue
		if ret == "O":
			fhOut.write("O won\n")
			continue
		
		draw = True
		for line in board:
			if "." in line:
				draw = False
				break

		if draw == True:	
			fhOut.write("Draw\n")
		else:
			fhOut.write("Game has not completed\n")


if __name__ == "__main__":
	main()
