import fileinput

answers = []

def anythingGreater(value, arr):
	result = False
	for i in arr:
		if i > value:
			result = True
	return result


def solve(field, numberOfRows, numberOfColumns):
	i = 0
	for row in field:		
		for j in range(numberOfColumns):
			value = row[j]
			column = []
			for k in range(numberOfRows):
				column.append(field[k][j])
			if anythingGreater(value, row) and anythingGreater(value, column):
				return "NO"
		i += 1
	return "YES"

def readfield(inputlines, firstLineIndex, numberOfRows, numberOfColumns):
	field = []
	for i in range(numberOfRows):
		rowStr = inputlines[firstLineIndex + i]
		row = map(int, rowStr.split())
		field.append(row)
	return field

inputlines = []
for line in fileinput.input():
	inputlines.append(line)

numberOfCases = int(inputlines[0])
sizeRow = 1
# sizeRow = int(inputlines[1].split(' ')[0]) + numberOfCases
for i in range(numberOfCases):	
	sizes = inputlines[sizeRow].split()
	(N, M) = (int(sizes[0]), int(sizes[1]))
	field = readfield(inputlines, sizeRow + 1, N, M)
	sizeRow = N + sizeRow + 1

	result = solve(field, N, M);
	answer = 'Case #' + str(i + 1) + ': ' + result + '\n'
	answers.append(answer);

with open ('myfile', 'a') as f:
	for answer in answers:
		f.write (answer)