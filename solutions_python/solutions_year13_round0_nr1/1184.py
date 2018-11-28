import sys

lines = [(0,1),(4,1),(8,1),(12,1),(0,4),(1,4),(2,4),(3,4),(0,5),(3,3)]

data = sys.stdin.readlines()
n = int(data[0])
data = data[1:]

for i in range(n):
	board = "".join(data[:4])
	data = data[5:]
	board = board.translate(None, '\n')
	winner = None
	for start,step in lines:
		for player in ['O','X']:
			cnt = 0
			for f in range(4):
				if board[start+f*step] == player or board[start+f*step] == 'T':
					cnt = cnt+1
			if cnt == 4:
				winner = player
	if winner != None:
		print "Case #%i: %c won"%(i+1,winner)
	elif '.' in board:
		print "Case #%i: Game has not completed"%(i+1)
	else:
		print "Case #%i: Draw"%(i+1)
#	print board

