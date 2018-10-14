filename = 'A-large.in'

f = open(filename,'r')

t = int(f.readline())

def winningFourChars(fourChars, character):
	numChars = sum(x == character for x in fourChars)
	numT = sum(x == 'T' for x in fourChars)
	if numChars == 4:
		return True
	if numChars == 3 and numT == 1:
		return True
	return False;

for i in range(1,t+1):
	board = [];
	for z in range(0,4):
		line = f.readline().strip()
		board.append(line)
	f.readline()
	#X wins?
	good = False
	for row in board:
		if winningFourChars(row,'X'):
			good = True
			break;
	for row in zip(*board):
		if winningFourChars(row,'X'):
			good = True
			break;
	
	if winningFourChars(board[0][0] + board[1][1] + board[2][2] + board[3][3],'X'):
		good = True
	
	if winningFourChars(board[3][0] + board[2][1] + board[1][2] + board[0][3],'X'):
		good = True;

	if good:
		print 'Case #' + str(i) + ': X won'
		continue
	#Y wins?
	good = False
	for row in board:
		if winningFourChars(row,'O'):
			good = True
			break;
	for row in zip(*board):
		if winningFourChars(row,'O'):
			good = True
			break;
	
	if winningFourChars(board[0][0] + board[1][1] + board[2][2] + board[3][3],'O'):
		good = True
	
	if winningFourChars(board[3][0] + board[2][1] + board[1][2] + board[0][3],'O'):
		good = True;

	if good:
		print 'Case #' + str(i) + ': O won'
		continue
	#draw
	if sum(x != '.' for x in "".join(board)) == 16:
		print 'Case #' + str(i) + ': Draw'
	else:
		print 'Case #' + str(i) + ': Game has not completed'

