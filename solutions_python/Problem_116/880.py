print 'Problem A'

path = r'F:\Dropbox\workspace\GoogleJam'
filNam = 'A-tiny-practice'
filNam = 'A-small-attempt'
filNam = 'A-large'

inFilNam = '%s\in\%s.in' % (path, filNam)
outFilNam = '%s\in\%s.out' % (path, filNam)

inFile = open(inFilNam, 'r')
outFile = open(outFilNam, 'w')

N = int(inFile.next().strip())

def hasWon(board, res):
	for str in board:
		for c in ['X', 'O']:
			if (str.count(c) + min(1, str.count('T')) == 4):
				return "%s won" % c
	return res

for count in range(N):
	board = []
	for _ in range(4):
		board.append(inFile.next().strip())
		
	if '.' in ''.join(board):
		res = "Game has not completed"
	else:
		res = "Draw"
	
	diag1, diag2 = '', ''
	for i in range(4):
		board.append(''.join([board[j][i] for j in range(4)]))
		diag1 = '%s%s' % (diag1, board[i][i])
		diag2 = '%s%s' % (diag2, board[i][3-i])
	board.append(diag1)
	board.append(diag2)

	outFile.write('Case #%s: %s\n' % (count + 1, str(hasWon(board, res))))
	try:
		inFile.next()
	except:
		continue

inFile.close()
outFile.close()

print 'Done!'
