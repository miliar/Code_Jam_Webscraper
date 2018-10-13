T = int(input())

from copy import deepcopy

for t in range(T):
	R, C = list(map(int, input().split()))

	grid = []
	for _ in range(R):
		grid.append(list(str(input())))

	pos = []
	todo = []
	for r in range(R):
		if grid[r].count('?') != C:
			char = '#'
			for c in range(C):
				if grid[r][c] != '?':
					char = grid[r][c]
					break

			for c in range(C):
				if grid[r][c] == '?':
					grid[r][c] = char
				else:
					char = grid[r][c]
		else:
			todo.append(r)

	do_first = False
	for r in todo:
		if r >= 1:
			grid[r] = deepcopy(grid[r-1])
		else:
			do_first = True

	if do_first:
		grid[0] = deepcopy(grid[1])

	for r in reversed(todo):
		if r < (R-1):
			grid[r] = deepcopy(grid[r+1])
		else:
			do_first = True


	for tu in pos:
		propagate(tu[0], tu[1])

	print("Case #{}:".format(t+1))
	for r in range(R):
		s = ''
		for c in range(C):
			s += grid[r][c]
		print(s)