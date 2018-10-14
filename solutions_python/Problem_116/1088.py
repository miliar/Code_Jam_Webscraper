f = open('tictac.in')
num_tests = int(f.readline())
test_number = 0

def test_array(letter, array, extra = "T", exclude = "."):
	if exclude in array:
		return False
	for elem in array:
		if elem != letter and elem != extra:
			return False
	return True

def full_board(grid, empty = "."):
	for array in grid:
		if empty in array:
			return False
	return True

def test_rows(grid):
	for array in grid:
		if test_array(array[0] ,array) or test_array(array[1], array):
			win_printer(array)
			return True
	return False

def test_cols(grid):
	for i in range(4):
		array = []
		for j in range(4):
			array.append(grid[j][i])
		if test_array(array[0] ,array) or test_array(array[1], array):
			win_printer(array)
			return True
	return False

def win_printer(array):
	if "O" in array:
		print("Case #{0}: O won".format(test_number))
	else:
		print("Case #{0}: X won".format(test_number))


for i in range(num_tests):
	test_number += 1
	grid = [[]]

	for i in range(4):
		grid.append(list(f.readline()))
		if("\n" in grid[i]):
			grid[i].remove("\n")

	grid.pop(0)

	'''clear the line if not last grid'''
	if test_number < num_tests:
		f.readline()


	'''test rows and cols'''
	if test_rows(grid) or test_cols(grid):
		continue

	'''test diagonals'''
	array = []
	for i in range(4):
		array.append(grid[i][i])

	if test_array(array[0] ,array) or test_array(array[1], array):
		win_printer(array)
		continue

	array = []
	for i in range(4):
		array.append(grid[3-i][i])


	if test_array(array[0] ,array) or test_array(array[1], array):
		win_printer(array)
		continue

	'''test if rows and cols all full'''
	if full_board(grid):
		print("Case #{0}: Draw".format(test_number))

	else:
		print("Case #{0}: Game has not completed".format(test_number))



