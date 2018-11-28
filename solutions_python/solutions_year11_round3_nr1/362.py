#!/usr/bin/python
import sys

finput = sys.argv[1]
fi = open(finput)
num = int(fi.readline())

def process(board):
	rboard = board[:]
	R = len(rboard)
	C = len(rboard[0])
	for i in range(R):
		for j in range(C):
			if not rboard[i][j] == '#': continue
			if i == R-1 or j == C-1: return None
			if not rboard[i+1][j] == '#' \
				or not rboard[i][j+1] == '#' \
				or not rboard[i+1][j+1] == '#': return None
			rboard[i][j] = '/'
			rboard[i+1][j] = chr(92)
			rboard[i][j+1] = chr(92)
			rboard[i+1][j+1] = '/'
	return rboard

for case in range(num):
	tmp = fi.readline().strip("\n").split()
	R = int(tmp[0])
	C = int(tmp[1])
	board = []
	for i in range(R):
		board.append([])
		for j in fi.readline().strip("\n"):
			board[-1].append(j)
	print ("Case #%i:") % (case+1)
	res = process(board)
	if res:
		for l in res: 
			for c in l: sys.stdout.write(c)
#			for c in l: print c,
			print ''
	else:
		print 'Impossible'
