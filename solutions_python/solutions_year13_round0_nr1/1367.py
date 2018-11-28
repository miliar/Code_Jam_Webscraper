#!/usr/bin/python3

import sys

def main(infile, outfile):
	for case in range(int(next(infile))):
		board = [next(infile) for i in range(4)]
		winner = None
		full = True
		next(infile)

		for i in range(2):
			for j in range (4):
				if "." in board[j]:
					full = False
				elif "O" not in board[j]:
					winner = "X"
					break
				elif "X" not in board[j]:
					winner = "O"
					break

			if winner:
				break

			diagonal = [board[j][j] for j in range(4)]
			if "." in diagonal:
				full = False
			elif "O" not in diagonal:
				winner = "X"
				break
			elif "X" not in diagonal:
				winner = "O"
				break

			if not i: board = turn(board)

		outfile.write("Case #{0}: ".format(case+1))
		if winner:
			outfile.write("{0} won\n".format(winner))
		elif full:
			outfile.write("Draw\n")
		else:
			outfile.write("Game has not completed\n")

def turn(oldBoard):
	newBoard = list(range(4))
	for i in range(4): #funky, from list of strings to list of lists
		newBoard[i] = [oldBoard[3-j][i] for j in range(4)]

	return newBoard

if __name__ == "__main__":
	with open(sys.argv[1]) as infile:
		with open(sys.argv[1][:-2] + "out", "w") as outfile:
			main(infile, outfile)
