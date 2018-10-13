import sys
##print sys.argv[1:]
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

t = int(lines[0])  # read a line with a single integer
##print t


def copyLeft(array, position):
	item = array[position]
	for x in range (position-1, -1, -1):
		if(array[x] == "?"):
			array[x] =item
		else:
			return array;
	return array;


def copyRight(array, position):
	item = array[position]
	for x in range ( position+1, len(array)):
		if(array[x] == "?"):
			array[x] =item
		else:
			return array;
	return array;

def copyUpArray(matrix, row):
	for y in range ( row -1, -1, -1):
		item = matrix[y][0]
		if(item == "?"):
			matrix[y] = matrix[row]
		else:
			return matrix;
	return matrix;

def copyDownArray(matrix, row):
	for y in range ( row+1, len(matrix)):
		item = matrix[y][0]
		if(item == "?"):
			matrix[y] = matrix[row]
		else:
			return matrix;
	return matrix;

def solveMatrix(matrix):
	for y in range ( 0, len(matrix)):
		if(matrix[y][0] != "?"):
			matrix = copyUpArray(matrix, y)
			matrix = copyDownArray(matrix, y)
	return matrix

def writeresults(writer, case, matrix):
	resultsString = "Case #{}:".format(case)
	f.write(resultsString+'\n')
	for row in matrix:
		resultsString  = "".join(row)
		f.write(resultsString+'\n')

################# main
f = open(sys.argv[2], 'w')
matrix = [[]]
row = 0
rowmax = 0
case = 0
for line in range (1, len(lines)):
	split = lines[line].rstrip('\n').split(" ")
	if len(split) >1:
		splitint = map(int, split)
		rowmax = splitint[0]
		matrix = [[0 for x in range(int(splitint[1]))] for y in range(splitint[0])]
		row =0
	else:
		if row <= rowmax:
			matrix[row] = list(lines[line].rstrip('\n'))
			# solve the row
			for x in range (0, len(matrix[row])):
				if matrix[row][x] != "?":					
					matrix[row] = copyLeft(matrix[row], x)					
					matrix[row] = copyRight(matrix[row], x)
			row +=1

		if row == rowmax:
			#print matrix
			resultsmatrix = solveMatrix(matrix)
			print resultsmatrix
			case +=1
			writeresults(f, case, resultsmatrix)

f.close() 
  # check out .format's specification for more formatting options



