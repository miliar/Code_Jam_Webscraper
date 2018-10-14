def parse_input(inputfile, outputfile):
	with open(outputfile, 'w') as out:
		with open(inputfile, 'r') as f:
			count = f.readline().strip()
			for each in xrange(int(count)):
				n, m = f.readline().strip().split(" ")
				matrix = []
				for line in xrange(int(n)):
					matrix.append(f.readline().strip().split(" "))
				flag = foo(int(n), int(m), matrix)
				if flag:
					flag = 'YES'
				else:
					flag = 'NO'
				out.write("Case #%d: %s\n" % (each + 1, flag))


def foo(n, m, matrix):
	for i in xrange(n):
		largest = max(matrix[i][0], matrix[i][-1])
		check_first = []
		for j in xrange(m):
			if matrix[i][j] != largest:
				check_first.append(j)
		check_second = []
		for index in check_first:
			for k in xrange(n):
				if matrix[k][index] > matrix[i][index]:
					return False
				if matrix[k][index] < matrix[i][index]:
					check_second.append([k, index])
		for (r, c) in check_second:
			for l in xrange(m):
				if matrix[r][l] > matrix[r][c]:
					return False
	return True


if __name__ == '__main__':
	inputfile = "B-small-attempt2.in"
	outputfile = "out"
	parse_input(inputfile, outputfile)
