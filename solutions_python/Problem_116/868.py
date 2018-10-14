f = open('ain.txt', 'r')
w = open('aout.txt', 'w')

num = int(f.readline())
for n in xrange(0, num):
	grid = [ ]
	for row in xrange(0, 4):
		grid.append(list(f.readline()[:-1]))
	
	filled = True
	
	# check across and up and down
	lists = [ ]
	diagonals = [ [], [], [], [] ]
	for i in xrange(0, 4):
		# get unique values in row 
		lists.append(sorted(list(set(grid[i]))))
		
		# get unique values in columns
		col = [ ]
		for j in xrange(0, 4):
			col.append(grid[j][i])
		lists.append(sorted(list(set(col))))
		
		# get unique in diagonals
		diagonals[0].append(grid[i][i])
		diagonals[1].append(grid[3-i][3-i])
		diagonals[2].append(grid[i][3-i])
		diagonals[3].append(grid[3-i][i])
	
	for diagonal in diagonals:
		lists.append(diagonal);
	
	winner = ''
	for j in lists:
		win = ''
		for item in j:
			if item == 'X' and win != 'O':
				win = item
			elif item == 'O' and win != 'X':
				win = item
			elif item == 'X' and win == 'O':
				win = ''
				break
			elif item == 'O' and win == 'X':
				win = ''
				break
			elif item == '.':
				win = ''
				winner = '.'
				break
	
		if win == 'X' or win == 'O':
			winner = win
			break
	
	print 'Case #{0}:'.format(n+1) ,
	
	if winner == '.':
		print 'Game has not completed'
	elif winner == 'X' or winner == 'O':
		print '{0} won'.format(winner)
	else:
		print 'Draw'
	# next
	f.readline() 