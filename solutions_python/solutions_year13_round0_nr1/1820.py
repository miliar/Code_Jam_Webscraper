def check(lane, t):
	Xwins = ["XXXX", "XXXT", "XXTX", "XTXX", "TXXX"]
	if any([lane == winCond for winCond in Xwins]):
		print "Case #%d: X won" % (t+1)
		return True

	Ywins = ["OOOO", "OOOT", "OOTO", "OTOO", "TOOO"]
	if any([lane == winCond for winCond in Ywins]):
		print "Case #%d: O won" % (t+1)
		return True

	return False

def hasDot(board):
	return any([c == '.' for l in board for c in l])

f = open(raw_input())
T = int(f.readline())
for t in xrange(T):
	board = [f.readline().strip() for i in xrange(5)]
	#print board
	gameEnded = False

	# check horizontal
	for i in xrange(4):
		lane = board[i]
		gameEnded |= check(lane, t)
	if gameEnded:
		continue

	# check vertical
	for i in xrange(4):
		lane = "".join([board[j][i] for j in xrange(4)])
		gameEnded |= check(lane, t)
	if gameEnded:
		continue

	# check main diagonal
	lane = "".join([board[i][i] for i in xrange(4)])
	gameEnded |= check(lane, t)
	if gameEnded:
		continue

	# check alternate diagonal
	lane = "".join([board[3-i][i] for i in xrange(4)])
	gameEnded |= check(lane, t)

	if not gameEnded:
		if not hasDot(board):
			print "Case #%d: Draw" % (t+1)
		else:
			print "Case #%d: Game has not completed" % (t+1)

f.close()