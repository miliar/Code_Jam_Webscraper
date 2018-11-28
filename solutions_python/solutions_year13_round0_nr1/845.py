M = 4

def getWinner(s,o,x):
	O,X = False,False
	count_t = s.count('T')
	if s.count('O') + count_t == M:
		O = True
	if s.count('X') + count_t == M:
		X = True
	return (O or o, X or x)


def check_winner(board):
	O,X = False, False
	s1,s2 = '',''
	count_t, count_o = 0,0
	for y in xrange(M):
		count_t += board[y].count('T')
		count_o += board[y].count('.')

		# horizontal
		O,X = getWinner(board[y],O,X)
		
		# vertical
		s = ''
		for x in xrange(M):
			s += board[x][y]
		O,X = getWinner(s,O,X)

		for x in xrange(M):
			if x == y:
				s1 += board[y][x]
			if x == (M-1)-y:
				s2 += board[y][x]

	O,X = getWinner(s1,O,X)
	O,X = getWinner(s2,O,X)

	if [O,X] == [True,False]:
		return "O won"
	elif [O,X] == [False,True]:
		return "X won"
	elif count_o == 0:
		return "Draw"
	else:
		return "Game has not completed"


T = int(raw_input())
for i in xrange(T):
	board = [raw_input() for j in xrange(M)]
	try:
		raw_input()
	except:
		""
	print "Case #{0}: {1}".format(i+1, check_winner(board))