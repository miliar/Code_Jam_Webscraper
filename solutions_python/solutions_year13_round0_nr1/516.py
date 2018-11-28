import sys

def go(fname='1toy.txt',verbose=False):
	f = open(fname)
	lines = [line.strip() for line in f.readlines()]
	boards = []
	n = int(lines[0])
	#for i in range(0, n):
	#	boards.append(lines[5*i+1:5*i+5])
	for i in range(0, n):
		print "Case #" + str(i+1) + ": " + wl(lines[5*i+1:5*i+5])
	f.close()

def players(cv):
	return {
			'X': (1,0),
			'O': (0,1),
			'T': (1,1),
			'.': (0,0)
			}.get(cv,(0,0))

def test():
	print players('X')
	print players('O')
	print players('T')
	print players('.')

def addpair(a, b):
	return (a[0]+b[0],a[1]+b[1])

def getmax(a, b):
	return (max(a[0],b[0]),max(a[1],b[1]))

def wl(board,verbose=False):
	n = 0
	for i in range(0, 4):
		for j in range(0, 4):
			if(board[i][j] != '.'):
				n += 1
	if verbose: print n
	mx = (0,0)
	for i in range(0, 4):
		cur = (0,0)
		for j in range(0, 4):
			cur = addpair(cur,players(board[i][j]))
		mx = getmax(mx, cur)
	if verbose: print mx
	for i in range(0, 4):
		cur = (0,0)
		for j in range(0, 4):
			cur = addpair(cur,players(board[j][i]))
		mx = getmax(mx, cur)
	cur = (0,0)
	if verbose: print mx
	for j in range(0, 4):
		cur = addpair(cur,players(board[j][j]))
	mx = getmax(mx, cur)
	cur = (0,0)
	if verbose: print mx
	for j in range(0, 4):
		cur = addpair(cur,players(board[3-j][j]))
	mx = getmax(mx, cur)
	if verbose: print mx
	if mx[0] == 4 and mx[1] == 4:
		return "Draw"
	if mx[0] == 4 and mx[1] != 4:
		return "X won"
	if mx[1] == 4 and mx[0] != 4:
		return "O won"
	if n == 16:
		return "Draw"
	else:
		return "Game has not completed"

go(fname=sys.argv[1])
