def scan(f):
	board=[]
	for i in range(4):
		board.append(f.readline())
	f.readline()
	return board

def horizon(board):
	for i in range(4):
		a, b,c,d=0,0,0,0
		for j in range(4):
			char = board[i][j]
			if char == 'X':
				a += 1
			elif char == 'O':
				b += 1
			elif char == '.':
				c += 1
			elif char == 'T':
				d += 1
		if (a+d) == 4:
			return 'X'
		if (b+d) == 4:
			return 'O'
	if c != 0:
		return 'N'
	else:
		return 'D'

def vertical(board):
	for i in range(4):
		a,b,c,d = 0,0,0,0
		for j in range(4):
			char = board[j][i]
			if char == 'X':
				a += 1
			elif char == 'O':
				b += 1
			elif char == '.':
				c += 1
			elif char == 'T':
				d += 1
		if (a+d) == 4:
			return 'X'
		if (b+d) == 4:
			return 'O'
	
	if c != 0:
		return 'N'
	else:
		return 'D'

def diagonala(board):
	a,b,c,d = 0,0,0,0
	for i in range(4):
		char = board[i][i]
		if char == 'X':
			a += 1
		elif char == 'O':
			b += 1
		elif char == '.':
			c += 1
		elif char == 'T':
			d += 1
	if (a+d) == 4:
		return 'X'
	if (b+d) == 4:
		return 'O'
	if c != 0:
		return 'N'
	return 'D'

def diagonalb(board):
	a,b,c,d = 0,0,0,0
	for i in range(4):
		char = board[i][3-i]
		if char == 'X':
			a += 1
		elif char == 'O':
			b += 1
		elif char == '.':
			c += 1
		elif char == 'T':
			d += 1
	if (a+d) == 4:
		return 'X'
	if (b+d) == 4:
		return 'O'
	if c != 0:
		return 'N'
	return 'D'

def main():
	f = open('A-small-0.in')
	out = open('A-small-0.out','w')
	t,i = int(f.readline()),1
	func = [horizon, vertical, diagonala,diagonalb]
	while (i <= t):
		board = scan(f)
		r, flag = False,True
		for m in func:
			res = m(board)
			if res == 'O':
				out.write("Case #%d: %s won\n"%(i,res))
				r = True
				break
			elif res == 'X':
				out.write("Case #%d: %s won\n"%(i,res))
				r = True
				break
			elif res == 'N':
				flag = False
		if (not r):
			if flag:
				out.write("Case #%d: Draw\n"%(i))
			else:
				out.write("Case #%d: Game has not completed\n"%(i))
		i+=1
	
	out.close()
	f.close()
if __name__ == "__main__":
	main()
