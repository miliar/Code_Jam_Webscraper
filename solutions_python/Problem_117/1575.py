def possibleCheck(row, col, item):
	#search a specifc row and column to see if item is not largest in both
	if (max(row) > item) and (max(col) > item):
		return False
	else:
		return True

def checkBoard(board, N, M):
	#iterate through board, searching for impossible case
	for n in range(N):
		for m in range(M):
			row = board[n]
			col = []
			for x in range(N):
				col.append(board[x][m])
			print "Row:", row
			print "Col:", col
			isPossible = possibleCheck(row, col, board[n][m])
			print isPossible
			if not isPossible:
				return False
	return True


i = open("B-small-attempt0.in", "r")
o = open("B-small-attempt0-output.txt", "w")

T = int(i.readline())
print "Test Cases (T): " + str(T)

for t in range(T):
	isPossible = True

	#find dimensions of board: N rows, M columns
	NandM = i.readline().split()
	N = int(NandM[0])
	M = int(NandM[1])
	print "N: " + str(N)
	print "M: " + str(M)
	
	#make board into 2D array
	board = []
	for row in range(N):
		board.append(i.readline().split())
	print board

	isPossible = checkBoard(board, N, M)

	if isPossible:
		case = "YES"
	else:
		case = "NO"

	print "Case #" + str(t+1) + ": " + case
	o.write("Case #" + str(t+1) + ": " + case + "\n")

i.close()
o.close()