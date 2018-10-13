import sys
def test(board):
	rowmaxs = map(max, board)
	colmaxs = map(max, zip(*board))
	#print rowmaxs, colmaxs
	for i, row in enumerate(board):
		for j, x in enumerate(row):
			if x != min(rowmaxs[i], colmaxs[j]):
				#print "er", i, j, x, rowmaxs[i], colmaxs[j]
				return False
	return True
T = int(sys.stdin.readline())
for t in range(T):
	N, M = map(int, sys.stdin.readline().split())
	board = [map(int, sys.stdin.readline().split()) for _ in range(N)]
	if test(board):
		print "Case #%d: YES" % (t+1)
	else: print "Case #%d: NO" % (t+1)
