def formatLine(line):
	s = line.split()
	s = [int(i) for i in s]

	return s

def formatdir(line):
	s= list(line)
	return s[:-1]


def solveTestCase(line):
	line = formatLine(line)




########
dat = open("testfile.txt", 'r')
out = open("answer.txt", "w")
numberCases = int(dat.readline())
#########

for i in range(numberCases):

	r,c = formatLine(dat.readline())

	data = [[0 for x in range(c)] for y in range(r)] 
	for x in range(r):
		a = formatdir(dat.readline())
		for y in range(len(a)):
			data[x][y] = a[y]

	change = 0
	fail = 0
	ends = 0

	for row in range(r):
		for col in range(c):
			orig = data[row][col]
			for j in range(2):

				if data[row][col] == '.':
					ends = 1
				if data[row][col] == '^':
					row2 = row
					col2 = col
					ends = 0
					row2 = row2-1
					while row2 >= 0:
						if data[row2][col2] != '.':
							ends = 1
							break
						row2 -= 1
					if ends == 0:
						data[row][col] = '>'
				if data[row][col] == '>':
					row2 = row
					col2 = col
					ends = 0
					col2 = col+1
					while col2 < c:
						if data[row2][col2] != '.':
							ends = 1
							break
						col2 += 1
					if ends == 0:
						data[row][col] = '<'
				if data[row][col] == '<':
					row2 = row
					col2 = col
					ends = 0
					col2 = col-1
					while col2 >= 0:
						if data[row2][col2] != '.':
							ends = 1
							break
						col2 -= 1
					if ends == 0:
						data[row][col] = 'v'
				if data[row][col] == 'v':
					row2 = row
					col2 = col
					ends = 0
					row2 = row + 1
					while row2 < r:
						if data[row2][col2] != '.':
							ends = 1
							break
						row2 += 1
					if ends == 0:
						data[row][col] = '^'

			if ends == 1 and orig == data[row][col]:
				change = change
			elif ends == 1:
				change += 1
			else:
				fail = 1




	if fail == 0:
		s = "Case #{0:d}: {1:d}\n".format(i+1, change)
		print s
		out.write(s)

	if fail == 1:
		s = "Case #{0:d}: IMPOSSIBLE\n".format(i+1)
		print s
		out.write(s)