def check(r):
	rx = r.replace('T', 'X')
	ro = r.replace('T', 'O')
	if rx == 'XXXX': return 'X'
	if ro == 'OOOO': return 'O'
	return None

def count_empty(board):
	return sum([row.count('.') for row in board])

def check_board(board):
	for i in range(4):
		r = board[i]
		c = ''.join([board[j][i] for j in range(4)])
		if check(r) == 'O' or check(c) == 'O': return 'O won'
		if check(r) == 'X' or check(c) == 'X': return 'X won'
	d = ''.join([board[i][i] for i in range(4)])
	rd = ''.join([board[3-i][i] for i in range(4)])
	if check(d) == 'O' or check(rd) == 'O': return 'O won'
	if check(d) == 'X' or check(rd) == 'X': return 'X won'
	if count_empty(board) != 0: return 'Game has not completed'
	return 'Draw'

def main():
	T = input()
	for i in range(T):
		board = [raw_input().strip() for j in range(4)]
		s = check_board(board)
		print "Case #%d: %s" % (i+1, s)
		raw_input()

if __name__ == '__main__': main()
