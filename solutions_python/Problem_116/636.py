def p(s):
	print s

def check(c, prev):
	global incomplete
	if c == 'T':
		return prev
	if c == '.':
		incomplete = True
		return False
	if prev is None:
		return c
	if c != prev:
		return False
	return c

def checkLine(l):
	global incomplete
	p = None
	for c in l:
		p = check(c, p)
		if p == False:
			return None
	return p

def solve(grid):
	global incomplete
	incomplete = False

	#Rows
	for l in ran:
		winner = checkLine(grid[l])
		if winner:
			return winner + " won"
		#Columns
		row = []
		for r in ran:
			row.append(grid[r][l])
		winner = checkLine(row)
		if winner:
			return winner + " won"

	#Diagonals
	ltr = []
	rtl = []
	for i in ran:
		ltr.append(grid[i][i])
		rtl.append(grid[i][3-i])

	winner = checkLine(ltr)
	if winner:
		return winner + " won"
	winner = checkLine(rtl)
	if winner:
		return winner + " won"

	#No Winner
	if incomplete:
		return "Game has not completed"
	return "Draw"

f = open("input.txt")
ran = range(4)
incomplete = False
o = open("output.txt", "w+")
for case in range(int(f.readline())):
	grid = []

	for l in ran:
		grid.append(f.readline().rstrip())
	f.readline()
	o.write("Case #" + str(case+1) +  ": " + solve(grid) + "\n")

o.close()