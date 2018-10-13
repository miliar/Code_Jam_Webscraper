import sys;

def rowWon(board, who):
    for r in xrange(4):
        n = board[r].count(who)
        if n == 4 or (n == 3 and board[r].count('T') == 1):
            return who
    return "NON"

def columnWon(board, who):
    for cl in xrange(4):
        col = [row[cl] for row in board]
        n = col.count(who)
        if n == 4 or (n == 3 and col.count('T') == 1):
            return who
    return "NON"

def diagonalWon(board, who):
    col = [board[i][i] for i in xrange(4)]
    n = col.count(who)
    if n == 4 or (n == 3 and col.count('T') == 1):
        return who
    return "NON"

def diagonal2Won(board, who):
    col = [board[4-1-i][i] for i in xrange(4)]
    n = col.count(who)
    if n == 4 or (n == 3 and col.count('T') == 1):
        return who
    return "NON"

def Draw(board):
	for r in xrange(4):
		if board[r].count('.'):
			return False
	return True

filename = sys.argv[1]
lines = open(filename, 'r')
num = int(lines.readline())

for i in xrange(1, num + 1):
    board = []
    for j in xrange(4):
        board.append(list(lines.readline().rstrip()))
    lines.readline()

    if rowWon(board, 'X') == 'X':
        win = 'X'
    elif rowWon(board, 'O') == 'O':
        win = 'O'
    elif columnWon(board, 'X') == 'X':
        win = 'X'
    elif columnWon(board, 'O') == 'O':
        win = 'O'
    elif diagonalWon(board, 'X') == 'X':
        win = 'X'
    elif diagonalWon(board, 'O') == 'O':
        win = 'O'
    elif diagonal2Won(board, 'X') == 'X':
        win = 'X'
    elif diagonal2Won(board, 'O') == 'O':
        win = 'O'
    elif Draw(board):
    	win = "Draw"
    else:
        win = 'not'

    if win == 'X' or win == 'O':
        print 'Case #'+ str(i)+': ' + win + ' won'
    elif win == 'Draw':
        print 'Case #'+ str(i)+': ' + win
    else:
    	print 'Case #'+ str(i)+': Game has not completed'