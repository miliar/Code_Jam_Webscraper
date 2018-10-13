T = int(raw_input())
for t in xrange(T):
	board = []
	for i in xrange(4):
		board.append(raw_input())
	try:
		raw_input()
	except:
		pass
	
	flag = False
	for row in board:
		if row.count('X') + row.count('T') == 4:
			print 'Case #%d: X won' % (t+1)
			flag = True
			break
		if row.count('O') + row.count('T') == 4:
			print 'Case #%d: O won' % (t+1)
			flag = True
			break
	if flag == True:
		continue
	
	boardT = [''.join((board[j][i] for j in xrange(4))) for i in xrange(4)]
	for row in boardT:
		if row.count('X') + row.count('T') == 4:
			print 'Case #%d: X won' % (t+1)
			flag = True
			break
		if row.count('O') + row.count('T') == 4:
			print 'Case #%d: O won' % (t+1)
			flag = True
			break
	if flag == True:
		continue
	
	diagonals = [''.join((board[i][i] for i in xrange(4))), ''.join((board[i][3-i] for i in xrange(4)))]
	for diagonal in diagonals:
		if diagonal.count('X') + diagonal.count('T') == 4:
			print 'Case #%d: X won' % (t+1)
			flag = True
			break
		if diagonal.count('O') + diagonal.count('T') == 4:
			print 'Case #%d: O won' % (t+1)
			flag = True
			break
	if flag == True:
		continue
	
	for row in board:
		if '.' in row:
			print 'Case #%d: Game has not completed' % (t+1)
			flag = True
			break
	if flag == True:
		continue
	
	print 'Case #%d: Draw' % (t+1)
	
