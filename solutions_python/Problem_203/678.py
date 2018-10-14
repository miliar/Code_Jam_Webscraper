t = int(raw_input()) # this is the number of test cases
for i in xrange(1, t+1):
	row, col = str(raw_input()).split()
	row_size = int(row)
	col_size = int(col)

	grid = []
	for row in range(row_size):
		#print list(str(raw_input()))
		grid.append(list(str(raw_input())))

	for row in range(row_size):
		initials = []
		for cell in range(col_size):
			if grid[row][cell] != '?':
				initials += [cell]

		if len(initials) >= 1:
			last_char = grid[row][initials[0]]
			cell = 0
			for k in range(col_size):
				if grid[row][k] == '?':
					grid[row][k] = last_char
				else:
					last_char = grid[row][k]

		else: # no initials in row
			if row > 0: # fill in from above
				for col in range(col_size):
					grid[row][col] = grid[row - 1][col]

			else:
				pass # 

	empty_row = 0
	while '?' in grid[empty_row]:
		empty_row += 1 # gets the number of top rows which are still not filled	

	if empty_row > 0:
		for col in range(col_size):
			for row in range(empty_row,0,-1):
				grid[row-1][col] = grid[row][col]

	print  "Case #{0}:".format(i)
	for row in range(row_size):
		init_str = ''
		for char in grid[row]:
			init_str += char
		print init_str
