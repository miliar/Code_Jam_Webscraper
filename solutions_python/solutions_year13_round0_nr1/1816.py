def who_won(line):
	chars = {}
	
	for c in line:
		if c == '.':
			return None
		chars[c] = True
	
	if len(chars) == 1:
		return next(chars.iterkeys())
	
	if len(chars) == 2 and 'T' in chars:
		del chars['T']
		return next(chars.iterkeys())
	
	return None

def case(n):
	board = [raw_input() for _ in xrange(4)]
	try:
		raw_input() # empty line?
	except:
		pass
	
	lines = board[:] # copy
	full = True
	
	for x in xrange(4):
		line = []
		
		for y in xrange(4):
			if board[y][x] == '.':
				full = False
			
			line.append(board[y][x])
		
		lines.append(line)
	
	d1 = []
	d2 = []
	for i in xrange(4):
		d1.append(board[i][i])
		d2.append(board[i][4 - i - 1])
	lines.append(d1)
	lines.append(d2)
	
	print 'Case #%d:' % n,
	
	for line in lines:
		who = who_won(line)
		
		if who is not None:
			print who, ' won'
			return
	
	if full:
		print 'Draw'
	else:
		print 'Game has not completed'

if __name__ == '__main__':
	for i in xrange(int(raw_input())):
		case(i + 1)