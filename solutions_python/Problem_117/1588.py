import sys
import re

def check(lawn):
	highestrow = []
	for r in lawn:
		highestrow.append(max(r))

	columns = []
	for i in range(len(lawn[0])):
		col = []
		for j in range(len(lawn)):
			col.append(lawn[j][i])
		columns.append(col)

	highestcolumn = []
	for c in columns:
		highestcolumn.append(max(c))

	for i in range(len(lawn)):
		for j in range(len(lawn[i])):
			height = lawn[i][j]
			if height != highestrow[i] and height != highestcolumn[j]:
				return False

	return True

def main(file):
	f = open(file, 'r')
	howmany = int(f.readline()) # how many test cases are there?
	stage = 0

	fo = open('B-small-attempt1.out', 'wd')
	
	while stage < howmany:
		lawnsize = f.readline().split()
		N,M = int(lawnsize[0]), int(lawnsize[1])
		lawn = []
		for i in range(0,N):
			heights = f.readline().split()
			lawn.append(heights)

		if check(lawn):
			msg = "YES\n"
		else:
			msg = "NO\n"

		stage += 1
		fo.write("Case #" + str(stage) + ": " + msg)

if __name__ == '__main__':
	main('B-small-attempt1.in')





















