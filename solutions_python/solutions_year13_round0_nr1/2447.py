#Algorith takes a List of four elements(each element is a row of the puzzle) as input and return the result of the game
def fun(matrix):
	#Counter of diagonal elements, both for X and O
	countX1=0
	countX2=0
	countO1=0
	countO2=0
	countEmpty=0
	for i in range(4):

		#Check one diagonal 		
		if L[i][i] == 'X' or L[i][i] == 'T':
			countX1=countX1+1
		if L[i][i] == 'O' or L[i][i] == 'T':
			countO1=countO1+1
		if countX1==4:
			return 'X won'
		if countO1==4:
			return 'O won'

		#Check other diagonal
		if L[i][3-i] == 'X' or L[i][3-i] == 'T':
			countX2=countX2+1
		if L[i][3-i] == 'O' or L[i][3-i] == 'T':
			countO2=countO2+1
		if countX2==4:
			return 'X won'
		if countO2==4:
			return 'O won'

		#Counter of row and column elements
		countXrow=0
		countOrow=0
		countXcol=0
		countOcol=0
		#Check rows and columns
		for j in range(4):
			if L[i][j] == 'X' or L[i][j] == 'T':
				countXrow=countXrow+1
			if L[i][j] == 'O' or L[i][j] == 'T':
				countOrow=countOrow+1
			if L[j][i] == 'X' or L[j][i] == 'T':
				countXcol=countXcol+1
			if L[j][i] == 'O' or L[j][i] == 'T':
				countOcol=countOcol+1
			if L[i][j] == '.':
				countEmpty=countEmpty+1
		if countXrow==4:
			return 'X won'
		if countOrow==4:
			return 'O won'
		if countXcol==4:
			return 'X won'
		if countOcol==4:
			return 'O won'

	if countEmpty>0:
		return 'Game has not completed'
	if countEmpty == 0:
		return 'Draw' 

#open file
f = open('./A-large.in', 'rw')

#count input puzzle
numberOfLines = f.readline()

#compute results 
for i in range(int(numberOfLines)):
	L=[]

	for j in range(4):
		l=f.readline()
		L.append(l[0:4])

	print 'Case #'+ str(i+1) + ': ' + fun(L)
	f.readline()


