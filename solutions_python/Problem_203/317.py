def solve(row_len, col_len, grid):
	for row_idx in range(row_len):
		last_char = '?'
		for col_idx in range(col_len):
			if grid[row_idx][col_idx] != '?':
				last_char = grid[row_idx][col_idx]
			else:
				grid[row_idx][col_idx] = last_char
		for col_idx in range(col_len)[::-1]:
			if grid[row_idx][col_idx] != '?':
				last_char = grid[row_idx][col_idx]
			else:
				grid[row_idx][col_idx] = last_char
	for row_idx in range(1, row_len):
		for col_idx in range(col_len):
			if grid[row_idx][col_idx] == '?':
				grid[row_idx][col_idx] = grid[row_idx-1][col_idx]

	for row_idx in range(row_len-1)[::-1]:
		for col_idx in range(col_len):
			if grid[row_idx][col_idx] == '?':
				grid[row_idx][col_idx] = grid[row_idx+1][col_idx]
	return grid

def print_grid(row_len, col_len, grid):
	for row_idx in range(row_len):
		for col_idx in range(col_len):
			print(grid[row_idx][col_idx], end='')
		print('')

if __name__ == '__main__':
	tc = int(input())
	for tc_idx in range(1, tc+1):
		row_len, col_len = map(int, input().strip().split())
		grid = [[]] * row_len
		for row_idx in range(row_len):
			grid[row_idx] = list(input().strip())
		res = solve(row_len, col_len, grid)
		print("Case #{0}:".format(tc_idx))
		print_grid(row_len, col_len, res)

"""
3
3 3
G??
?C?
??J
3 4
CODE
????
?JAM
2 2
CA
KE
"""