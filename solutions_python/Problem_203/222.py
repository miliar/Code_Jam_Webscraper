import math

file_strings = []
with open("A-large.in") as data_file:
	for line in data_file:
		file_strings.append(line.strip())

T = file_strings[0] # number of testcases
file_strings.pop(0)
T = int(T)

for i in range(1, T + 1):
	vals = file_strings.pop(0).split()
	R, C = int(vals[0]), int(vals[1]	)
	grid = []
	#grid is grid[R][C]
	for j in range(R):
		grid.append(file_strings.pop(0))
		grid[j] = list(grid[j])

	# put all things above and below the same
	for r in range(R):
		for c in range(C):
			if grid[r][c] != "?":
				above = True
				below = True
				for diff in range(1, R):
					# below
					if r + diff < R:
						if grid[r + diff][c] != "?":
							below = False
						if grid[r + diff][c] == "?" and below == True:
							grid[r + diff][c] = grid[r][c]
					if r - diff >= 0:
						if grid[r - diff][c] != "?":
							above = False
						if grid[r - diff][c] == "?" and above == True:
							grid[r - diff][c] = grid[r][c]

	# fill out the first column, if it hasn't been filled out yet
	if grid[0][0] == "?":
		charIndex = 0
		for c in range(1, C):
			if grid[0][c] != "?":
				charIndex = c
				break
		for r in range(R):
			grid[r][0] = grid[r][charIndex]

	# now to fill out the other columns that are still empty
	for cc in range(C):
		if grid[0][cc] == "?":
			charIndex = 0 # column index of the leftmost column that's full
			for col in range(cc):
				if grid[0][col] != "?":
					if charIndex <= col:
						charIndex = col
			for r in range(R):
				grid[r][cc] = grid[r][charIndex]

	print("Case #{}:".format(i))
	for row in range(R):
		c = ""
		for i in range(len(grid[row])):
			c = c + grid[row][i]
		print(c)

