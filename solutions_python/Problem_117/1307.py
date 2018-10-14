import numpy

def parse(data):
	return list(map(lambda line: list(map(int, line.split())), data))

def solve(data):
	field = parse(data)
	matrix = numpy.matrix(field)

	# print(matrix)

	matrix[matrix == matrix.max()] = 0

	# print(matrix)

	while True:
		new_max = matrix.max()
		matrix_in_list = matrix.tolist()

		found = False

		for i in range(len(matrix_in_list)):
			x = matrix_in_list[i]
			for j in range(len(x)):
				if new_max == x[j]:
					vertical = (matrix[:,j] == 0).any()
					horizontal = (matrix[i] == 0).any()
					if not vertical or not horizontal:
						found = True
						matrix[i,j] = -1

		if found:
			matrix[matrix == -1] = 0

		# print(matrix)

		if (matrix == 0).all():
			return True

		if not found:
			return False

i = 1
numberOfLines = 0
field = []
field_length = 0
for line in open('B-large.in'):
	if numberOfLines == 1:
		field_length = int(line.strip().split()[0])
	if numberOfLines > 1:
		field.append(line.strip())
	numberOfLines += 1
	if field_length and numberOfLines == field_length + 2:
		print('Case #' + str(i) + ': ' + str(solve(field) and 'YES' or 'NO'))
		numberOfLines = 1
		i += 1
		field = []