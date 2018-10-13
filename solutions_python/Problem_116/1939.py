def get_winner(l):
	if l.count('X') == 4 or (l.count('X') == 3 and l.count('T') == 1):
		return 'X'
	if l.count('O') == 4 or (l.count('O') == 3 and l.count('T') == 1):
		return 'O'
	return None

def has_won(b):
	bl = list(b)
	for i in xrange(4):
		# check horizontally
		win = get_winner([bl[i * 4 + 0], bl[i * 4 + 1], bl[i * 4 + 2], bl[i * 4 + 3]])
		if win != None:
			return win

		# check vertically
		win = get_winner([bl[i - 1], bl[i + 3], bl[i + 7], bl[i + 11]])
		if win != None:
			return win

	# check diagonally
	win = get_winner([bl[0], bl[5], bl[10], bl[15]])
	if win != None:
		return win

	win = get_winner([bl[3], bl[6], bl[9], bl[12]])
	if win != None:
		return win

	return None

def is_incomplete(b):
	return True if (list(b).count('.') > 0) else False

def main():
	f = open('1.in', 'r')
	o = open('1.out', 'w')

	T = int(f.readline().strip())

	for t in xrange(T):
		b = ''
		for i in xrange(4):
			b += f.readline().strip()
		f.readline()

		if has_won(b) == 'X':
			res = 'X won'
		elif has_won(b) == 'O':
			res = 'O won'
		elif is_incomplete(b):
			res = 'Game has not completed'
		else:
			res = 'Draw'

		s = "Case #%d: %s\n" % (t+1, res)
		#print s
		o.write(s)

if __name__ == "__main__":
    main()
