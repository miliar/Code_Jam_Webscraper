

f = open("input.txt", "r")
f.readline()

num_lines = int(f.readline())

print num_lines

o = open("output.txt", "w")

for case in range(0, num_lines):
	board = []
	for a in range(0, 4):
		line = f.readline()
		board.append(list(line[:-1]))
	f.readline()
	print board
	
	x_in_l_diag = 0
	o_in_l_diag = 0
	x_in_r_diag = 0
	o_in_r_diag = 0
	
	x_has_won = False
	o_has_won = False
	
	place_count = 0
	
	for b in range(0, 4):
		x_in_a_row = 0
		o_in_a_row = 0
		x_in_a_col = 0
		o_in_a_col = 0
		
		if board[b][b] == 'T':
			x_in_l_diag += 1
			o_in_l_diag += 1
		if board[b][b] == 'X':
			x_in_l_diag += 1
		if board[b][b] == 'O':
			o_in_l_diag += 1
		
		if board[b][3-b] == 'T':
			x_in_r_diag += 1
			o_in_r_diag += 1
		if board[b][3-b] == 'X':
			x_in_r_diag += 1
		if board[b][3-b] == 'O':
			o_in_r_diag += 1
		
		for c in range(0, 4):

			if board[b][c] != '.':
				place_count += 1
				
			if board[b][c] == 'T':
				x_in_a_row += 1
				o_in_a_row += 1
			if board[b][c] == 'X':
				x_in_a_row += 1
			if board[b][c] == 'O': 
				o_in_a_row += 1
			
			if board[c][b] == 'T':
				x_in_a_col += 1
				o_in_a_col += 1
			if board[c][b] == 'X':
				x_in_a_col += 1
			if board[c][b] == 'O': 
				o_in_a_col += 1
		
		if x_in_a_row == 4 or x_in_a_col == 4:
			x_has_won = True
		if o_in_a_row == 4 or o_in_a_col == 4:
			o_has_won = True
	if x_in_l_diag == 4 or x_in_r_diag == 4:
		x_has_won = True
	if o_in_l_diag == 4 or o_in_r_diag == 4:
		o_has_won = True
	
	if x_has_won:
		o.write("Case #"+str(case+1)+": X won\n")
	elif o_has_won:
		o.write("Case #"+str(case+1)+": O won\n")
	elif place_count == 16:
		o.write("Case #"+str(case+1)+": Draw\n")
	else:
		o.write("Case #"+str(case+1)+": Game has not completed\n")


f.close()