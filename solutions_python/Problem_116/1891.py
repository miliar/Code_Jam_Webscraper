#Tic-tac-toe-tomek
# Google Code Jam 2013
# Andrew Tarzwell
# April 12th 2013
import sys


game_grids = []

def get_data():
	num_cases = int(sys.stdin.readline())
	for case in xrange(num_cases):
		case = []
		for x in xrange(4):
			line = sys.stdin.readline()
			case.append(line)
		sys.stdin.readline()
		game_grids.append(case)

def solve(grid):
	#Easiest, check horizontally.
	#print "Grid " + str(grid)
	for c in xrange(4):
		x = 0
		o = 0
		t = 0
		for y in xrange(4):
			#print grid[c][y]
			if grid[c][y] == "T":
				t += 1
			elif grid[c][y] == "X":
				x += 1
			elif grid[c][y] == "O":
				o += 1
		if x + t == 4:
			return "X won"
		elif o + t == 4:
			return "O won"

	#Check vertical
	for c in xrange(4):
		x = 0
		o = 0
		t = 0
		for y in xrange(4):
			#print grid[y][c]
			if grid[y][c] == "T":
				t += 1
			elif grid[y][c] == "X":
				x += 1
			elif grid[y][c] == "O":
				o += 1
		if x + t == 4:
			return "X won"
		elif o + t == 4:
			return "O won"

	#Check Crosses... (LR)
	for c in xrange(4):
		x = 0
		o = 0
		t = 0
		for y in xrange(4):
		#	print grid[y][y]
			if grid[y][y] == "T":
				t += 1
			elif grid[y][y] == "X":
				x += 1
			elif grid[y][y] == "O":
				o += 1
		if x + t == 4:
			return "X won"
		elif o + t == 4:
			return "O won"

	#Check Crosses... (RL)
	x = 0
	o = 0
	t = 0
	for y in xrange(4):
		#print grid[y][3-y]
		if grid[y][3-y] == "T":
			t += 1
		elif grid[y][3-y] == "X":
			x += 1
		elif grid[y][3-y] == "O":
			o += 1
	if x + t == 4:
		return "X won"
	elif o + t == 4:
		return "O won"

	#No winner at this point. 
	#Draw or Incomplete?
	d = 0 #dot
	nd = 0 #not dot
	for x in xrange(4):
		for y in xrange(4):
			#print grid[x][y]
			if grid[x][y] == ".":
				d += 1
			else:
				nd +=1
	if d > 0:
		return "Game has not completed"
	else:
		return "Draw"
				

if __name__ == "__main__":
	#get data
	get_data()
	for idx, grid in enumerate(game_grids):
		print "Case #" + str(idx+1) + ": " + solve(grid)
	#print game_grids
