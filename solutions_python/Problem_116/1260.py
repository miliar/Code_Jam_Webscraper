T = input()
for t in xrange(T):
	board = [raw_input(), raw_input(), raw_input(), raw_input()]
	rx = [0, 0, 0, 0]
	ro = [0, 0, 0, 0]
	cx = [0, 0, 0, 0]
	co = [0, 0, 0, 0]
	ans = ''
	for i in xrange(4):
		rt = board[i].count('T')
		rx[i] = board[i].count('X') + rt
		ro[i] = board[i].count('O') + rt
		col = ''.join([board[j][i] for j in xrange(4)])
		ct = col.count('T')
		cx[i] = col.count('X') + ct
		co[i] = col.count('O') + ct
		if rx[i] == 4 or cx[i] == 4:
			ans = 'X won'
			break
		elif ro[i] == 4 or co[i] == 4:
			ans = 'O won'
			break
	if ans == '':
		dr = board[0][0]+board[1][1]+board[2][2]+board[3][3]
		dl = board[0][3]+board[1][2]+board[2][1]+board[3][0]
		rt = dr.count('T')
		lt = dl.count('T')
		drx = dr.count('X') + rt
		dro = dr.count('O') + rt
		dlx = dl.count('X') + lt
		dlo = dl.count('O') + lt
		if drx == 4 or dlx == 4:
			ans = 'X won'
		elif dro == 4 or dlo == 4:
			ans = 'O won'
	if ans == '':
		if ''.join(board).count('.') > 0:
			ans = 'Game has not completed'
		else:
			ans = 'Draw'
	print 'Case #%d: %s' % (t+1, ans)
	raw_input()
