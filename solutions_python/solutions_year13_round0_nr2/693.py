# grass can be cut if every square is either the tallest in its row/column OR equal to its whole row/column
def test_index(row, column, num_rows, num_columns, lawn):
	cell_value = lawn[row][column]
	
	#if every number in row is equal, we are good
	tallest_in_row = True
	row_equal = True
	for column_index in range(num_columns):
		if lawn[row][column_index] != cell_value:
			row_equal = False
			if lawn[row][column_index] > cell_value:
				tallest_in_row = False
	if row_equal or tallest_in_row:
		return True
	
	#if every number in column is equal, we are good
	column_equal = True
	for row_index in range(num_rows):
		if lawn[row_index][column] != cell_value:
			column_equal = False
			if lawn[row_index][column] != cell_value:
				tallest_in_column = False
	if column_equal or tallest_in_column:
		return True
	
	#if neither, we are bad
	return False

input_file = open('B-small-attempt0.in', 'r')
output_file = open('B-Small.out', 'w+')
line = input_file.readline()
num_cases = int(line)
for case_num in range(1,num_cases+1):
	result = 'YES'
	rows_and_columns = input_file.readline().split()
	num_rows = int(rows_and_columns[0])
	num_columns = int(rows_and_columns[1])

	lawn = [['' for i in range(num_columns)] for j in range(num_rows)]
	# read in lawn
	for row in range(num_rows):
		line = input_file.readline().split()
		for column in range(num_columns):
			lawn[row][column] = line[column]

	# test every lawn square
	for row in range(num_rows):
		for column in range(num_columns):
			index_result = test_index(row,column, num_rows, num_columns, lawn)
			if not index_result:
				result = 'NO'
				break
		if not index_result:
			break

	output_file.write('Case #'+str(case_num)+': '+result+'\n')


