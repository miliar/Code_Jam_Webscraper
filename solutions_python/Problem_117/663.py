#Lawnmower
#We dealing with 2d arrays. Too complicated to do in C++ :P
#If there is a group of lower level things surrounded by higher level, not possible.

fin = open('lawnmower.in','r')
fout = open('lawnmower.out','w')

T = int(fin.readline())

def mowable(brd):
	'''for i in range(len(brd)):
		for j in range(len(brd[i])):
			print(str(brd[i][j]), end = " ")
		print()
	print()'''
	for i in range(len(brd)):
		mowhoriz(i, brd)
	for i in range(len(brd[i])):
		mowvert(i, brd)
		
	'''for i in range(len(brd)):
		for j in range(len(brd[i])):
			fout.write(str(brd[i][j]) + " ")
		fout.write("\n")
	fout.write("\n")
	'''

	for i in range(len(brd)):
		for j in range(len(brd[i])):
			if brd[i][j] == 1:
				return "NO"
					
	return "YES"

def mowhoriz(i, brd):
	for j in range(len(brd[i])):
		if not (brd[i][j] == 1 or brd[i][j] == 0):
			return
	for j in range(len(brd[i])):
		brd[i][j] = 0
		
def mowvert(i, brd):
	for j in range(len(brd)):
		if not (brd[j][i] == 1 or brd[j][i] == 0):
			return
	for j in range(len(brd)):
		brd[j][i] = 0

def floodfill(x, y, brd):
	if x < 0 or y < 0 or x >= len(brd) or y >= len(brd[i]) or brd[x][y] == 2:
		#print("2 spotted")
		return brd
	elif brd[x][y] == 1:
		brd[x][y] = 2
		brd = floodfill(x + 1, y, brd)
		brd = floodfill(x - 1, y, brd)
		brd = floodfill(x, y + 1, brd)
		brd = floodfill(x, y - 1, brd)
		return brd
	else:
		return brd

for count in range(T):
	N, M = fin.readline().split()
	N = int(N)
	M = int(M)
	
	board = []
	for i in range(N):
		board.append([])
		line = fin.readline().split()
		for j in range(M):
			board[i].append(int(line[j]))
	
	fout.write("Case #" + str(count + 1) + ": " + str(mowable(board)) + "\n")
	
fin.close()
fout.close()
