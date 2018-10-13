import sys

def main():
	global dot
	T = 0
	oStatus = int(0)
	board = [[0 for x in xrange(4)] for x in xrange(4)]
	for i in range(4):
		for j in range(4) :
			board[i][j] = "."

	INPUT = open("./A-small-attempt2.in","r")	
	T = int(INPUT.readline())
	result = ""
	outWrite = ["X won","O won","Game has not completed","Draw"]
	#Loop for T no of cases
	for i in range(T): 

		for j in range(4) :
			for k in range(4):
				board[j][k] = str(INPUT.read(1))
			INPUT.read(1)

		oStatus = yieldOutput(board)
		OUTPUT = open("./output.txt","w")
		result = result + "Case #" + str(i+1) + ": " + str(outWrite[oStatus]) + "\n"
		OUTPUT.write(result)
		OUTPUT.close()

		INPUT.read(1)

	INPUT.close()

def yieldOutput(board):

	x = "X"
	t = "T"

	for i in range(2) :
		# ALL 4 X wit no T
		if board[0][0] == x :
			if board[0][3] == x:
				if board[0][1] == x and board[0][2] == x:
					return i

			if board[3][0] == x:
				if board[1][0] == x and board[2][0] == x:
					return i

			if board[3][3] == x:
				if board[1][1] == x and board[2][2] == x:
					return i 

		if board[0][1] == x and board[1][1] == x and board[2][1] == x and board[3][1] == x:
			return i

		if board[0][2] == x and board[1][2] == x and board[2][2] == x and board[3][2] == x:
			return i

		if board[0][3] == x:

			if board[1][3] == x and board[2][3] == x and board[3][3] == x:
				return i

			if board[1][2] == x and board[2][1] == x and board[3][0] == x:
				return i

		if board[1][0] == x and board[1][1] == x and board[1][2] == x and board[1][3] == x:
			return i

		if board[2][0] == x and board[2][1] == x and board[2][2] == x and board[2][3] == x:
			return i

		# X wins with T

		if board[0][0] == t :

			if board[0][1] == x and board[0][2] == x and board[0][3] == x :
				return i

			if board[1][0] == x and board[2][0] == x and board[3][0] == x :
				return i

			if board[1][1] == x and board[2][2] == x and board[3][3] == x :
				return i
		
		if board[0][1] == t:

			if board[0][0] == x and board[0][2] == x and board[0][3] == x:
				return i

			if board[1][1] == x and board[2][1] == x and board[3][1] == x:
				return i

		if board[0][2] == t:

			if board[0][0] == x and board[0][1] == x and board[0][3] == x:
				return i

			if board[1][2] == x and board[2][2] == x and board[3][2] == x:
				return i

		if board[0][3] == t:

			if board[0][0] == x and board[0][1] == x and board[0][2] == x:
				return i

			if board[1][3] == x and board[2][3] == x and board[3][3] == x:
				return i			

			if board[1][2] == x and board[2][1] == x and board[3][0] == x:
				return i

		if board[1][0] == t:

			if board[1][1] == x and board[1][2] == x and board[1][3] == x:
				return i

			if board[0][0] == x and board[2][0] == x and board[3][0] == x:
				return i			

		if board[1][1] == t:

			if board[1][0] == x and board[1][2] == x and board[1][3] == x:
				return i

			if board[0][1] == x and board[2][1] == x and board[3][1] == x:
				return i			

			if board[0][0] == x and board[2][2] == x and board[3][3] == x:
				return i

		if board[1][2] == t:

			if board[1][0] == x and board[1][1] == x and board[1][3] == x:
				return i

			if board[0][2] == x and board[2][2] == x and board[3][2] == x:
				return i

			if board[0][3] == x and board[2][1] == x and board[3][0] == x:
				return i			

		if board[1][3] == t:

			if board[1][0] == x and board[1][2] == x and board[1][1] == x:
				return i

			if board[0][3] == x and board[2][3] == x and board[3][3] == x:
				return i	

		if board[2][0] == t:

			if board[2][1] == x and board[2][2] == x and board[2][3] == x:
				return i

			if board[0][0] == x and board[1][0] == x and board[3][0] == x:
				return i			

		if board[2][1] == t:

			if board[2][0] == x and board[2][2] == x and board[2][3] == x:
				return i

			if board[0][1] == x and board[1][1] == x and board[3][1] == x:
				return i

			if board[1][2] == x and board[0][3] == x and board[3][0] == x:
				return i			

		if board[2][2] == t:

			if board[2][1] == x and board[2][0] == x and board[2][3] == x:
				return i

			if board[0][2] == x and board[1][2] == x and board[3][2] == x:
				return i			

			if board[1][1] == x and board[0][0] == x and board[3][3] == x:
				return i

		if board[2][3] == t:

			if board[2][1] == x and board[2][2] == x and board[2][0] == x:
				return i

			if board[0][3] == x and board[1][3] == x and board[3][3] == x:
				return i			

		if board[3][0] == t:

			if board[3][1] == x and board[3][2] == x and board[3][3] == x:
				return i

			if board[0][0] == x and board[1][0] == x and board[2][0] == x:
				return i	

			if board[1][2] == x and board[2][1] == x and board[0][3] == x:
				return i		


		if board[3][1] == t:

			if board[3][0] == x and board[3][2] == x and board[3][3] == x:
				return i

			if board[0][1] == x and board[1][1] == x and board[2][1] == x:
				return i			

		if board[3][2] == t:

			if board[3][1] == x and board[3][0] == x and board[3][3] == x:
				return i

			if board[0][2] == x and board[1][2] == x and board[2][2] == x:
				return i			

		if board[3][3] == t:

			if board[3][1] == x and board[3][2] == x and board[3][0] == x:
				return i

			if board[0][3] == x and board[1][3] == x and board[2][3] == x:
				return i	

			if board[1][1] == x and board[2][2] == x and board[0][0] == x:
				return i		


		x = "O"
	# Dot-Count
	for j in range(4):
		for k in range(4):
			if board[j][k] == '.':
				return 2

	return 3
main()
