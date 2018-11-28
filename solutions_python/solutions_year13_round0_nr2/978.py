import sys

file = sys.stdin

def readboard(file):
	line = file.readline()
	dimensions = line.split(" ")
	n = int(dimensions[0])
	m = int(dimensions[1])
	board = dict()
	for i in range(0,n):
		line = file.readline()
		row = [int(x) for x in line.split(" ")]
		assert(len(row) == m)
		for j in range(0,m):
			board[(i,j)] = row[j]
	return (n,m,board)

def procboard(n,m,board):
	rowbound = 100 * [0]
	colbound = 100 * [0]
	for i in range(0,n):
		for j in range(0,m):
			rowbound[i] = max(rowbound[i], board[(i,j)])
			colbound[j] = max(colbound[j], board[(i,j)])
	for i in range(0,n):
		for j in range(0,m):
			cell = board[(i,j)]
			if cell < rowbound[i] and cell < colbound[j]:
				"print i,rowbound[i],j,colbound[j]"
				return "NO"
	return "YES"

cases = int(file.readline())
for k in range(1,cases+1):
	(n,m,board) = readboard(file)
	res = procboard(n,m,board)
	print "Case #{0}: {1}".format(k,res)
