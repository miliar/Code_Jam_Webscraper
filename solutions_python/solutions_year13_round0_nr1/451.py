import sys

# The name of the file
FILE_NAME = 'A-large'

f_in = open(FILE_NAME + '.in', 'r')
f_out = open(FILE_NAME + '.out', 'w')

# The number of tests
T = int(f_in.readline())

# Translate to numbers
def translate(c): 
	if c == '.': return 0
	if c == 'X': return 2
	if c == 'O': return 3
 	if c == 'T': return 1

# For each test...
for t in range(T):
	board = list()

	# Default result
	result = "Draw"

	# Read the board
	for i in range(4):
		board.append(map(translate, list(f_in.readline().strip())))

	# Transpose the matrix
	board.extend([[row[i] for row in board] for i in range(4)])

	# Get one diagonal
	board.append([board[i][i] for i in range(4)])

	# Get the other diagonal
	board.append([board[i][3 - i] for i in range(4)])

	# Check results line by line
	for i in range(10):
		p = reduce(lambda x,y: x*y, board[i])

		if p == 0: 
			result = "Game has not completed"
		elif p % 2 == 0 and p % 3 != 0: 
			result = "X won"
			break;
		elif p % 2 != 0 and p % 3 == 0:
			result = "O won"
			break
		
	# Write the output
	f_out.write("Case #" + str(t + 1) + ": " + result)

	if t + 1 < T: f_out.write("\n")

	f_in.readline()

f_out.close()
f_in.close()


