def rc(r,c): return r*4 + c

def winpositions():
	for i in range(4):
		yield [rc(i,j) for j in range(4)]
		yield [rc(j,i) for j in range(4)]
	yield [rc(i,i) for i in range(4)]
	yield [rc(i, 3 - i) for i in range(4)]

def iswinner(board, player):
	return any(all(board[p] in (player,'T') for p in pos) for pos in winpositions())

def isdone(board): return all(b != '.' for b in board)

def readboard(): return ''.join(raw_input().strip() for _ in range(4))
	
T = input()

for t in range(1,T+1):
	if t > 1: raw_input() # eat blank line
	board = readboard()
	print 'Case #' + str(t) + ':',
	if iswinner(board,'X'): print 'X won'
	elif iswinner(board,'O'): print 'O won'
	elif isdone(board): print 'Draw'
	else: print 'Game has not completed'
	


