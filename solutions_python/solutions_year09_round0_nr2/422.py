f = open('B-large.in', 'r')

first_line = f.readline()
T = int(first_line)

for i in range(T):
	size_line = f.readline()
	size_line_list = size_line.split(' ')
	H = int(size_line_list[0])
	W = int(size_line_list[1])

	matrix = list()
	drains_to_matrix = list()

	for y in range(H):
		drains_to_matrix.append(list())
		row = f.readline()
		row_list = row.split(' ')
		for j in range(len(row_list)):
			row_list[j] = int(row_list[j])
			drains_to_matrix[y].append(None)
		matrix.append(row_list)

	for y in range(H):
		for x in range(W):
			#check drainage direction
			lowest_altitude = matrix[y][x]

			if y-1 >= 0:
				if(lowest_altitude > matrix[y-1][x]):
					lowest_altitude = matrix[y-1][x]
					drains_to_matrix[y][x] = (y-1, x)

			if x-1 >= 0:
				if(lowest_altitude > matrix[y][x-1]):
					lowest_altitude = matrix[y][x-1]
					drains_to_matrix[y][x] = (y, x-1)

			if x+1 < W:
				if(lowest_altitude > matrix[y][x+1]):
					lowest_altitude = matrix[y][x+1]
					drains_to_matrix[y][x] = (y, x+1)

			if y+1 < H:
				if(lowest_altitude > matrix[y+1][x]):
					lowest_altitude = matrix[y+1][x]
					drains_to_matrix[y][x] = (y+1, x)

	char_index = 97

	for y in range(H):
		for x in range(W):
			if drains_to_matrix[y][x] is None:
				drains_to_matrix[y][x] = char_index
				char_index = char_index + 1

	for j in range(H*W):
		for y in range(H):
			for x in range(W):
				if type(drains_to_matrix[y][x]) is tuple:
					t = drains_to_matrix[y][x]
					if drains_to_matrix[t[0]][t[1]] is not None:
						drains_to_matrix[y][x] = drains_to_matrix[t[0]][t[1]]

		good = True
		for y in range(H):
			for x in range(W):
				if type(drains_to_matrix[y][x]) is not tuple:
					good = False
					break

		if good:
			break;

	char_index = 97
	asdf = dict()
	for y in range(H):
		for x in range(W):
			if drains_to_matrix[y][x] not in asdf:
				asdf[drains_to_matrix[y][x]] = chr(char_index)
				char_index = char_index + 1

	for y in range(H):
		for x in range(W):
			drains_to_matrix[y][x] = asdf[drains_to_matrix[y][x]]

	print "Case #" + str(i+1) + ":"
	for y in range(H):
		qwer = ""
		for x in range(W):
			qwer = qwer + drains_to_matrix[y][x] + " "
		print qwer[0:len(qwer)-1]







