n = int(input())
for k in range(0, n):
	m = list(map(int, input().strip().split()))
	grid = []
	for j in range(0, m[0]):
		grid.append(input().strip())
	new_grid = []
	for line in grid:
		new_row = []
		for letter in line:
			new_row.append(letter)
		new_grid.append(new_row)
	i = 0
	while i < m[0]:
		j = 0
		while j < m[1]:
			if new_grid[i][j] != "?":
				new = new_grid[i][j]
				j += 1
				while j < m[1] and new_grid[i][j] == "?":
					new_grid[i][j] = new
					j += 1
			new = "?"
			tmp = j + 1
			while j < m[1] and new_grid[i][j] == "?" and tmp < m[1] and new == "?":
				if new_grid[i][tmp] != "?":
					new = new_grid[i][tmp]
				tmp += 1 
			if tmp == m[1] and new == "?":
				j = m[1]
			if new != "?":
				while j < m[1] and new_grid[i][j] == "?":
					new_grid[i][j] = new
					j += 1
			#print(i, j)
		i += 1

	i = 0
	while i < m[0]:
		j = 0
		while j < m[1]:
			if new_grid[i][j] == "?":
				tmp = i + 1
				while tmp < m[0] and new_grid[tmp][j] == "?":
					tmp += 1
				if new_grid[tmp-1][j] != "?":
					new_grid[i][j] = new_grid[tmp-1][j]
				elif tmp < m[0] and new_grid[tmp][j] != "?":
					new_grid[i][j] = new_grid[tmp][j]
			j += 1
		i += 1

	i = m[0] - 1
	while i > -1:
		j = 0
		while j < m[1]:
			if new_grid[i][j] == "?":
				tmp = i - 1
				while tmp > -1 and new_grid[tmp][j] == "?":
					tmp -= 1
				if new_grid[tmp+1][j] != "?":
					new_grid[i][j] = new_grid[tmp+1][j]
				elif tmp > -1 and new_grid[tmp][j] != "?":
					new_grid[i][j] = new_grid[tmp][j]
			j += 1
		i -= 1

	i = 0
	while i < m[0]:
		j = 0
		while j < m[1]:
			if new_grid[i][j] == "?":
				tmp = i + 1
				while tmp < m[0] and new_grid[tmp][j] == "?":
					tmp += 1
				if new_grid[tmp-1][j] != "?":
					new_grid[i][j] = new_grid[tmp-1][j]
				elif tmp < m[0] and new_grid[tmp][j] != "?":
					new_grid[i][j] = new_grid[tmp][j]
			j += 1
		i += 1	

	i = m[0] - 1
	print("Case #{}:".format(k+1)) 
	for line in new_grid:
		print("".join(line))


