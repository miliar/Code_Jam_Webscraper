def read_file(filename):
	f = open(filename)
	count = int(f.readline())
	cases = f.read().split("\n\n")[:-1]
	f.close()

	for i in range(count):
		cases[i] = cases[i].split("\n")
	
	return cases

def solve(case):
	draw_counter = 0
	for x in range(4):
		ch_X = 0
		ch_Y = 0
		cv_X = 0
		cv_Y = 0
		cdr_X = 0
		cdr_Y = 0
		cdl_X = 0
		cdl_Y = 0
		for y in range(4):
			c = case[x][y]
			C = case[y][x]
			if c == 'X' or c == 'T':
				ch_X += 1
			if c == 'O' or c == 'T':
				ch_Y -= 1
			if ch_X == 4:
				return 'X'
			if ch_Y == -4:
				return 'O'

			if C == 'X' or C == 'T':
				cv_X += 1
			if C == 'O' or C == 'T':
				cv_Y -= 1
			if cv_X == 4:
				return 'X'
			if cv_Y == -4:
				return 'O'

			if c != '.':
				draw_counter += 1
				if draw_counter == 16:
					return 'D'
			if x > 0:
				continue
			if case[y][y] == 'X' or case[y][y] == 'T':
				cdr_X += 1
			if case[y][y] == 'O' or case[y][y] == 'T':
				cdr_Y -= 1
			if cdr_X == 4:
				return 'X'
			if cdr_Y == -4:
				return 'O'
			
			if case[y][3-y] == 'X' or case[y][3-y] == 'T':
				cdl_X += 1
			if case[y][3-y] == 'O' or case[y][3-y] == 'T':
				cdl_Y -= 1
			if cdl_X == 4:
				return 'X'
			if cdl_Y == -4:
				return 'O'
	return ''

cases = read_file("A-large.in")
for i in range(len(cases)):
	case = cases[i]
	out = solve(case)
	if out == 'O':
		print "Case #%d: O won" % (i+1)
	elif out == 'X':
		print "Case #%d: X won" % (i+1)
	elif out == 'D':
		print "Case #%d: Draw" % (i+1)
	else:
		print "Case #%d: Game has not completed" % (i+1)
