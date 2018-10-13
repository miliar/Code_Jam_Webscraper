T = int(raw_input())
for t in xrange(T):
	board = []
	for i in xrange(4):
		board.extend(raw_input())
	#print board
	#X = int("".join([('1' if i in ['X', 'T'] else '0') for i in board)
	not_compl = any((i=='.') for i in board)
	X = int("".join([('1' if i in ['X', 'T'] else '0') for i in board]),2)
	O = int("".join([('1' if i in ['O', 'T'] else '0') for i in board]),2)

	#print int("1111000000000000",2)
	#print int("0000111100000000",2)
	#print int("0000000011110000",2)
	#print int("0000000000001111",2)
	#print int("1000100010001000",2)
	#print int("0100010001000100",2)
	#print int("0010001000100010",2)
	#print int("0001000100010001",2)
	#print int("1000010000100001",2)
	#print int("0001001001001000",2)
	#print 

	lucky_numbers = [61440,3840,240,15,34952,17476,8738,4369,33825,4680]

	X_won = any((X & n) == n for n in lucky_numbers)
	O_won = any((O & n) == n for n in lucky_numbers)
	#print X_won, O_won, not_compl
	def winning_text(X,O,ncl):
		if X == True:
			if O == True:
				return "Draw"
			else:
				return "X won"
		else:
			if O == True:
				return "O won"
			elif ncl == True:
					return "Game has not completed"
			else:
				return "Draw"

	print "Case #%d: %s" % (t+1, winning_text(X_won,O_won,not_compl))
	raw_input()
