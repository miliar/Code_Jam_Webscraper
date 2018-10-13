f = open('A-large.txt')
no_cases = int(f.readline().strip())
f_write = open('output.txt', 'w')

for case_count in range(no_cases):
	test_case = [f.readline().strip() for i in range(4)]
	f.readline()

	board = [list(test_case[i]) for i in range(4)]
	
	x_won, o_won = False, False
	empty_cells = 0

	for row_count in range(4):
		x, o = 0, 0

		for col_count in range(4):
			cell = board[row_count][col_count]

			if cell=='X': x += 1
			if cell=='O': o += 1
			if cell=='T':
				x += 1
				o += 1
			if cell=='.': empty_cells += 1

		if x==4: x_won = True
		if o==4: o_won = True

	for col_count in range(4):
		x, o = 0, 0

		for row_count in range(4):
			cell = board[row_count][col_count]

			if cell=='X': x += 1
			if cell=='O': o += 1
			if cell=='T':
				x += 1
				o += 1

		if x==4: x_won = True
		if o==4: o_won = True

	x, o = 0, 0

	for dia1_count in range(4):
		cell = board[dia1_count][dia1_count]

		if cell=='X': x += 1
		if cell=='O': o += 1
		if cell=='T':
			x += 1
			o += 1

	if x==4: x_won = True
	if o==4: o_won = True

	x, o = 0, 0

	for dia2_count in range(4):
		cell = board[dia2_count][3-dia2_count]

		if cell=='X': x += 1
		if cell=='O': o += 1
		if cell=='T':
			x += 1
			o += 1

	if x==4: x_won = True
	if o==4: o_won = True

	
	f_write.write("Case #" + str(case_count+1) + ": ")

	if x_won: 
		f_write.write("X won")
	elif o_won: 
		f_write.write("O won")
	elif empty_cells==0: 
		f_write.write("Draw")
	else:
		f_write.write("Game has not completed")

	f_write.write('\n')


f_write.close()
f.close()