#!/usr/bin/python

import sys

def solve(cases):
	solution = []
	for case in cases:
		rowC = case[0]
		colC = case[1]
		rows = case[2]

		total = 0
		sol = [['.' for j in range(colC)] for i in range(rowC)]
		for i in range(rowC):
			for j in range(colC):
				if rows[i][j] == '#':
					total += 1
	
		if total % 4 != 0:
			solution.append(["Impossible"])
		else:
			cRow = 0
			cCol = 0
			fail = False
			while total != 0 and not fail:
				if rows[cRow][cCol] == '#':
					if cRow != rowC - 1 and cCol != colC - 1 and rows[cRow][cCol + 1] == '#' and rows[cRow + 1][cCol] == '#' and rows[cRow + 1][cCol + 1] == '#':
						sol[cRow][cCol] = '/'
						rows[cRow][cCol] = '.'
						sol[cRow][cCol + 1] = '\\'
						rows[cRow][cCol + 1] = '.'
						sol[cRow + 1][cCol] = '\\'
						rows[cRow + 1][cCol] = '.'
						sol[cRow + 1][cCol + 1] = '/'
						rows[cRow + 1][cCol + 1] = '.'
						total -= 4
						if cCol + 2 > colC - 1:
							cRow += 1
						cCol = (cCol + 2) % colC
					else:
						solution.append(["Impossible"])
						fail = True
				else:
					if cCol + 1 > colC - 1:
						cRow += 1
					cCol = (cCol + 1) % colC

			if not fail:
				grandsol = []
				for row in sol:
					chars = ""
					for char in row:
						chars += char
					grandsol.append(chars)
				solution.append(grandsol)

	
	return solution


f = open(sys.argv[1],'r')
caseCount = int(f.readline().strip('\n'))
cases = []
for i in range(caseCount):
	[rowC,colC] = map(int,f.readline().strip('\n').split(' '))
	rows = []
	for j in range(rowC):
		rows.append(list(f.readline().strip('\n')))

	cases.append((rowC,colC,rows))

solution = solve(cases)

for i in range(len(solution)):
	print "Case #" + str(i + 1) + ": "
	for j in solution[i]:
		print j
