
def checker(board, i):
	pieces = 0
	# test each line
	# test rows
	for r in range(0, 20, 5):
		X = 0
		O = 0
		for inc in range(1, 5, 1):
			index = r + inc
			if board[index] == 'X': 
				X+=1
				pieces+=1
			elif board[index] == 'O': 
				O+=1
				pieces+=1
			elif board[index] == "T":
				X+=1
				O+=1
				pieces+=1
		if X == 4:
			return 'Case #{0}: X won\n'.format(i)
		elif O == 4:
			return 'Case #{0}: O won\n'.format(i)
	# test columns
	for c in range(1, 5, 1):
		X = 0
		O = 0
		for inc in range(0, 20, 5):
			index = c + inc
			if board[index] == 'X': 
				X+=1
			elif board[index] == 'O': 
				O+=1
			elif board[index] == "T":
				X+=1
				O+=1
		if X == 4:
			return 'Case #{0}: X won\n'.format(i)
		elif O == 4:
			return 'Case #{0}: O won\n'.format(i)
	# test diagonals
	X = 0
	O = 0
	for index in range(1, 25, 6):
		if board[index] == 'X': 
			X+=1
		elif board[index] == 'O': 
			O+=1
		elif board[index] == "T":
			X+=1
			O+=1
		if X == 4:
			return 'Case #{0}: X won\n'.format(i)
		elif O == 4:
			return 'Case #{0}: O won\n'.format(i)
	X = 0
	O = 0
	for index in range(0, 20, 4):
		if board[index] == 'X': 
			X+=1
		elif board[index] == 'O': 
			O+=1
		elif board[index] == "T":
			X+=1
			O+=1
		if X == 4:
			return 'Case #{0}: X won\n'.format(i)
		elif O == 4:
			return 'Case #{0}: O won\n'.format(i)

	if pieces == 16:
		return 'Case #{0}: Draw\n'.format(i)
	else:
		return 'Case #{0}: Game has not completed\n'.format(i)

input_file = open('large_input', 'r')
output_file = open('large_output', 'w')
N = int(input_file.readline())
output = ''

for i in range(1, N+1):
	board = '\n'
	for j in range(5):
		board += input_file.readline()
	#print "board {0} is:\n {1}".format(i, board)
	output += checker(board, i)
output_file.write(output)

output_file.close()
input_file.close()