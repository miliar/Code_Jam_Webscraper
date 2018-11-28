if __name__ == '__main__':
	r = open('A-large.in', 'r')
	w = open('out.txt', 'w')
	n = int(r.readline())

	for i in range(n):
		board = []
		for j in range(4):
			line = r.readline()
			line = line.rstrip()
			board.append(line)

		XO = []
		dot_count = 0
		empty = 0
		x_hor = 0
		o_hor = 0
		for x in range(4):
			x_hor = 0
			o_hor = 0
			for y in range(4):
				if board[x][y] == 'X':
					x_hor += 1
				elif board[x][y] == 'O':
					o_hor += 1
				elif board[x][y] == 'T':
					x_hor += 1
					o_hor += 1
				elif board[x][y] == '.':
					dot_count += 1
			XO.append((x_hor, o_hor))

		x_vert = 0
		o_vert = 0
		for x in range(4):
			x_vert = 0
			o_vert = 0
			for y in range(4):
				if board[y][x] == 'X':
					x_vert += 1
				elif board[y][x] == 'O':
					o_vert += 1
				elif board[y][x] == 'T':
					x_vert += 1
					o_vert += 1
			XO.append((x_vert, o_vert))

			
		x_diag = 0
		o_diag = 0
		for x in range(4):
			for y in range(4):
				if x==y:
					if board[x][y] == 'X':
						x_diag += 1
					elif board[x][y] == 'O':
						o_diag += 1
					elif board[x][y] == 'T':
						x_diag += 1
						o_diag += 1
		XO.append((x_diag, o_diag))
		
		x_diag = 0
		o_diag = 0
		for x in range(4):
			for y in range(4):
				if x+y == 3:
					if board[x][y] == 'X':
						x_diag += 1
					elif board[x][y] == 'O':
						o_diag += 1
					elif board[x][y] == 'T':
						x_diag += 1
						o_diag += 1
		XO.append((x_diag, o_diag))

		for tup in XO:
			if tup[0] == 4:
				w.write('Case #%d: X won\n' % (i+1))
				break
			elif tup[1] == 4:
				w.write('Case #%d: O won\n' % (i+1))
				break
		else:
			if dot_count == 0:
				w.write('Case #%d: Draw\n' % (i+1))
			else:
				w.write('Case #%d: Game has not completed\n' % (i+1))
		r.readline()