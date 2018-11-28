import sys, itertools

def open_mine(R, C, M, field, board, i, j):
	d = [[0, 1], [1, 1], [1, 0], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
	c = 0
	for xy in d:
		if i + xy[0] >= 0 and i + xy[0] < R and j + xy[1] >= 0 and j + xy[1] < C and field[i + xy[0]][j +xy[1]] == '*':
			c = c + 1
	board[i][j] = chr(ord('0') + c)

def is_possible(R, C, M, field, xc, yc):
	board = [['#'] * C for i in range(R)]
	open_mine(R, C, M, field, board, xc, yc)
	d = [[0, 1], [1, 1], [1, 0], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
	
	opened = True
	while opened:
		opened = False
		#print '\n'.join([str(r) for r in board])
		#print '---'
		for i in range(R):
			for j in range(C):
				if board[i][j] == '0':
					for xy in d:
						if i + xy[0] >= 0 and i + xy[0] < R and j + xy[1] >= 0 and j + xy[1] < C and board[i + xy[0]][j + xy[1]] == '#':
							open_mine(R, C, M, field, board, i + xy[0], j + xy[1])
					board[i][j] = '.'
					#print "Opened", i, j
					opened = True

	#print '\n'.join([str(r) for r in board])
	#print sum([r.count('#') for r in board])
	return sum([r.count('#') for r in board]) == M


def solve(R,C, M):
	for indexes in itertools.combinations(range(R * C), M):
		field = [['.'] * C for i in range(R)]
		for ix in indexes:
			field[ix / C][ix % C] = '*'

		#print "Check field\n", '&'.join([str(r) for r in field])
		#print indexes

		for i in range(R):
			for j in range(C):
				if field[i][j] != '*':
					if is_possible(R, C, M, field, i, j):
						field[i][j] = 'c'
						return '\n'.join([''.join(r) for r in field])

		#return "stop"
	return "Impossible" 


f = open(sys.argv[1])
T = int(f.readline().strip())

#Couple of hard one cases
#Precalculated with the same code, but it takes long time ~ 1-2 minutes to finish
predef_impossible = [
	[5,5,18],
	[5,5,20],
	[4,5,13],
	[4,5,15],
	[5,4,13],
	[5,4,15]
]

for t in range(T):
	(R, C, M) = f.readline().strip().split()
	R, C, M = int(R), int(C), int(M)

	predefined = False
	for p in predef_impossible:
		if p[0] == R and p[1] == C  and p[2] == M:
			ans = "Impossible"
			predefined = True

	if not predefined:
		ans = solve(R, C, M)

	print "Case #" + str(t + 1) + ":\n" + ans
