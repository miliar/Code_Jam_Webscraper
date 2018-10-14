def has_dif(board, y0, y1, x0, x1, c):
	for i in xrange(y0, y1+1):
		for j in xrange(x0, x1+1):
			if board[i][j] != c and board[i][j] != '?':
				return True


def max_rec(R, C, board, i, j):
	max_area = 0
	max_rec = [-1, -1, -1, -1]
	for y0 in xrange(i+1):
		for y1 in xrange(i, R):
			for x0 in xrange(j+1):
				for x1 in xrange(j, C):
					if (y1-y0+1) * (x1-x0+1) > max_area:
						if not has_dif(board, y0, y1, x0, x1, board[i][j]):
							max_area = (y1-y0+1) * (x1-x0+1)
							max_rec = [y0, y1, x0, x1]
	return max_rec


def fill_rec(R, C, board, y0, y1, x0, x1, c):
	for i in xrange(y0, y1+1):
		for j in xrange(x0, x1+1):
			board[i][j] = c


def solve(R, C, board):
	done = set([])
	for i in xrange(R):
		for j in xrange(C):
			if board[i][j] == '?' or board[i][j] in done:
				continue
			y0, y1, x0, x1 = max_rec(R, C, board, i, j)
			fill_rec(R, C, board, y0, y1, x0, x1, board[i][j])
			done.add(board[i][j])
	return board



def print_board(board):
	for row in board:
		print ''.join(row)

def verify(R, C, orig, sol):
	charset = set([])
	oriset = set([])
	for i in xrange(R):
		for j in xrange(C):
			charset.add(sol[i][j])
			if orig[i][j] != '?':
				oriset.add(orig[i][j])
				if orig[i][j] != sol[i][j]:
					return False
	if oriset != charset:
		return False
	for c in charset:
		ct = 0
		y0, x0 = 1000, 1000
		y1, x1 = -1, -1
		for i in xrange(R):
			for j in xrange(C):
				if sol[i][j] == c:
					ct += 1
					y0 = min(y0, i)
					y1 = max(y1, i)
					x0 = min(x0, j)
					x1 = max(x1, j)
		if (y1-y0+1) * (x1-x0+1) != ct:
			return False
	return True

T = int(raw_input())
for case in xrange(1, T+1):
	R, C = map(int, raw_input().split())
	board = [[c for c in raw_input()] for row in xrange(R)]
	ori = [[c for c in row] for row in board]
	solution = solve(R, C, board)
	#print_board(ori)
	print "Case #{}:".format(case)
	print_board(solution)
	if not verify(R, C, ori, solution):
		print "WRONG"


