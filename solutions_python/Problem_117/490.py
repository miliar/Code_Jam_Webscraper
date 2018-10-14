import sys

def go(fname='1toy.txt',verbose=False):
	f = open(fname)
	lines = [line.strip() for line in f.readlines()]
	boards = []
	nn = int(lines[0])
	ct = 1
	for i in range(0, nn):
		nm = str.split(lines[ct],' ')
		n, m = int(nm[0]),int(nm[1])
		#print n, m
		board = lines[ct+1:ct+n+1]
		ct = ct + (n+1)
		print "Case #" + str(i+1) + ": " + examine(board, n, m)
	f.close()

def getnums(nstr=''):
	splits = str.split(nstr,' ')
	ret = []
	for si in splits:
		ret.append(int(si))
	return ret

def examine(board, n, m):
	numboard = []
	mxx = []
	mxy = []
	#print board, len(board)
	for i in range(0, n):
		numboard.append(getnums(board[i]))
	#print numboard
	for i in range(0, n):
		mxx.append(max(numboard[i]))
	for j in range(0, m):
		col = [numboard[i][j] for i in range(0, n)]
		mxy.append(max(col))
	for i in range(0, n):
		for j in range(0, m):
			if numboard[i][j] < mxx[i] and numboard[i][j] < mxy[j]:
				return "NO"
	return "YES"

go(fname=sys.argv[1])
