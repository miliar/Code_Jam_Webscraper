def fill_row(cake, row_num):

	row = cake[row_num]

	curr_col = 0
	while curr_col < len(row):
		char = row[curr_col]
		if char == '?':
			curr_col += 1
			continue

		k = curr_col - 1
		while 0 <= k < len(row) and row[k] == '?':
			row[k] = char
			k -= 1

		k = curr_col + 1
		while 0 <= k < len(row) and row[k] == '?':
			row[k] = char
			k += 1

		curr_col = k

def fill_col(cake, row_num, col_num):

	char = '?'
	k = row_num - 1
	while 0 <= k < len(cake):
		if cake[k][col_num] != '?':
			char = cake[k][col_num]
			break
		k -= 1

	if char == '?':
		k = row_num + 1
		while 0 <= k < len(cake):
			if cake[k][col_num] != '?':
				char = cake[k][col_num]
				break
			k += 1

	if char == '?':
		print('Error!')

	k = row_num
	while 0 <= k < len(cake):
		if cake[k][col_num] != '?':
			break
		cake[k][col_num] = char
		k -= 1

	k = row_num + 1
	while 0 <= k < len(cake):
		if cake[k][col_num] != '?':
			break
		cake[k][col_num] = char
		k += 1


num_tests = int(input())

results = []
for i in range(num_tests):
	num_rows, num_cols = input().split()
	num_rows = int(num_rows)
	num_cols = int(num_cols)

	cake = []

	for j in range(num_rows):
		cake.append(list(input()))

	for row_num in range(num_rows):
		fill_row(cake, row_num)

	for row_num in range(num_rows):
		if cake[row_num][0] == '?':
			for col_num in range(num_cols):
				fill_col(cake, row_num, col_num)

	results.append(cake)

for i in range(num_tests):
	print('Case #{}:'.format(i + 1))
	result = results[i]
	for j in range(len(result)):
		str_row = ''
		for char in result[j]:
			str_row += char
		print(str_row)
