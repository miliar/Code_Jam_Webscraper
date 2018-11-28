import fileinput

i = -1
outs = 0
grid = []
possibilities = []
for line in fileinput.input("A-small-attempt0.in"):
	if i == -1:
		i = 0
		continue
	if i % 5 == 0:
		row = int(line)
	elif 0 < i % 5 <= 4:
		grid.append(line.split())
	if i % 5 == 4:
		if len(possibilities) > 0:
			couldbe = []
			for poss in possibilities:
				for poss2 in grid[row - 1]:
					if poss == poss2:
						couldbe.append(poss)
			outs += 1
			s = "Case #" + str(outs) + ": "
			if len(couldbe) == 1:
				s += couldbe[0]
			elif len(couldbe) == 0:
				s += "Volunteer cheated!"
			elif len(couldbe) > 1:
				s += "Bad magician!"
			print(s)
			possibilities = []
		else:
			possibilities = grid[row - 1]
		grid = []
	i += 1