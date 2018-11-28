
def small(case_num,a,size):

	failure_msg = "Case #" + str(case_num) + ': Draw'

	#rows
	for row in a:
		cur_e = ''
		for i,e in enumerate(row):
			if not cur_e or cur_e == 'T':
				cur_e = e
			if e == '.' or (e != cur_e and e != 'T'):
				break
			if i == size -1:
				print 'Case #' + str(case_num) + ': ' + cur_e + ' won'
				return

	#cols 
	for j in xrange(size):
		cur_e = ''
		for i in xrange(size):
			e = a[i][j]
			if not cur_e  or cur_e == 'T':
				cur_e = e
			if e == '.' or (e != cur_e and e != 'T'):
				break
			if i == size -1:
				print 'Case #' + str(case_num) + ': ' + cur_e + ' won'
				return

	#diags from left top
	cur_e = ''
	for i in xrange(size):
		
		e = a[i][i]
		if not cur_e  or cur_e == 'T':
			cur_e = e
		if e == '.' or (e != cur_e and e != 'T'):
			break
		if i == size -1:
			print 'Case #' + str(case_num) + ': ' + cur_e + ' won'
			return

	#diags from left bottom
	cur_e = ''
	for i in xrange(size):
		e = a[size-1-i][i]
		if not cur_e or cur_e == 'T':
			cur_e = e
		if e == '.' or (e != cur_e and e != 'T'):
			break
		if i == size -1:	
			print 'Case #' + str(case_num) + ': ' + cur_e + ' won'
			return

	for row in a:
		for col in row:
			if col == '.':
				failure_msg = "Case #" + str(case_num) + ': Game has not completed'

	print failure_msg


def parse_input():
	arr_size = 4
	grids = []
	fname = 'TicTacToe.in'
	inFile =  open(fname, 'r')
	size = int(inFile.readline())
	for i in xrange(size):
		grids.append([])
		cur_grid = grids[i]
		for _ in xrange(arr_size):
			cur_grid.append(list(inFile.readline().strip()))
		inFile.readline()#discard empty line
	return grids


for i,grid in enumerate(parse_input()):
	small(i+1,grid,len(grid))







