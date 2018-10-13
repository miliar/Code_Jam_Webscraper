def check(grid):
	case = 0 #0 = error, 1 = x won, 2 = o won, 3, not complete, 4 = draw

	for line in grid:
		if line.count('X') == 3:
			if line.count('T') == 1:
				case = 1
				break
		elif line.count('X') == 4:
			case = 1
			break
		elif line.count('O') == 3:
			if line.count('T') == 1:
				case = 2
				break
		elif line.count('O') == 4:
			case = 2
			break

	if case == 0:
		for line in grid:
			if line.count('.') > 0:
				case = 3
				break
			else:
				case = 4

	return case


lines = [line.strip() for line in open('input.txt')]
cases = lines[0]

grids = []
for i in range(0, int(cases)):
	grids.append([])
	for j in range(1, 5):
		grids[i].append(lines[(i * 5) + j])
	for j in range(0,4):
		grids[i].append(lines[(i * 5) + 1][j] + lines[(i * 5) + 2][j] + lines[(i * 5) + 3][j] + lines[(i * 5) + 4][j])
	grids[i].append(lines[(i * 5) + 1][0] + lines[(i * 5) + 2][1] + lines[(i * 5) + 3][2] + lines[(i * 5) + 4][3])
	grids[i].append(lines[(i * 5) + 1][3] + lines[(i * 5) + 2][2] + lines[(i * 5) + 3][1] + lines[(i * 5) + 4][0])

i = 0
f = open('output.txt', 'w')
for grid in grids:
	i += 1
	state = check(grid)

	if state == 0:
		print "YOU DUN FUCKED UP BOY"
		break
	elif state == 1:
		f.write("Case #"+str(i)+": X won\n")
	elif state == 2:
		f.write("Case #"+str(i)+": O won\n")
	elif state == 3:
		f.write("Case #"+str(i)+": Game has not completed\n")
	elif state == 4:
		f.write("Case #"+str(i)+": Draw\n")
