import numpy

input_file = 'A-large-attempt0.in'
output_file = 'A-large-attempt0.out'

def checkWinner(X, O, T):
	if X + T == 4:
		return "X won"
	elif O + T == 4:
		return "O won"
	else:
		return None

def findWinner(board):
	matrix = []

	#Create matrix representation of our board and its 90 degree counterpart
	normal = numpy.matrix(board)
	rotated = numpy.rot90(normal, 1)

	matrix.extend(normal.tolist())
	matrix.extend(rotated.tolist())
	matrix.extend(normal.diagonal().tolist())
	matrix.extend(rotated.diagonal().tolist())

	isFinished = True;

	for j in range(0, len(matrix)):
		X = matrix[j].count('X')
		O = matrix[j].count('O')
		T = matrix[j].count('T')

		if matrix[j].count('.') > 0:
			isFinished = False

		result = checkWinner(X, O, T)
		if (result):
			return result

	if isFinished:
		return "Draw"
	else:
		return "Game has not completed"

with open(input_file, 'r') as fin:
	with open(output_file, 'w') as fout:
		T = int(fin.readline())

		for i in range(0, T):
			board = []
			for j in range(0, 4):
				board.append(list(fin.readline().rstrip()))

			result = findWinner(board)
			output = "Case #%s: %s\n" % (str(i+1), result)
			fout.write(output)
			fin.readline()