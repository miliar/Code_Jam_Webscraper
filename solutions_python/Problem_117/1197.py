#!/usr/bin/python3

import sys

def main(infile, outfile):
	for case in range(int(next(infile))):
		rows, columns = tuple(int(i) for i in next(infile).split())
		board = [[int(j) for j in next(infile).split()] for i in range(rows)]

		possible = True

		for y in range(rows):
			for x in range(columns):
				if any(board[y][x]<board[y][i] for i in range(columns)) and any(board[y][x]<board[i][x] for i in range(rows)):
					possible = False
					break

			if not possible: break

		outfile.write("Case #{0}: {1}\n".format(case+1, ("NO","YES")[possible]))

if __name__ == "__main__":
	with open(sys.argv[1]) as infile:
		with open(sys.argv[1][:-2] + "out", "w") as outfile:
			main(infile, outfile)
