Blue = 2
Red = 1

def DiagnolTest(Grid,length,K):
	RedInARow = False
	BlueInARow = False
#	print 1
	for i in range(0,length-K+1):
		previous = Grid[0][i]
		rowCount = 1
		colCount = i+1
		inARowCounter = 1
		while colCount < length:
#			print colCount
			if previous!=0:
				if Grid[rowCount][colCount] == previous:
					inARowCounter+=1
				else:
					inARowCounter=1
				if inARowCounter == K:
					if previous == Blue:
						BlueInARow = True
					else:
						RedInARow = True
				previous = Grid[rowCount][colCount]
			rowCount+=1
			colCount+=1
#	print 2
	for i in range(1,length-K+1):
		previous = Grid[i][0]
		rowCount = i+1
		colCount = 1
		inARowCounter = 1
		while rowCount < length:
			if previous!=0:
				if Grid[rowCount][colCount] == previous:
					inARowCounter+=1
				else:
					inARowCounter=1
				if inARowCounter == K:
					if previous == Blue:
						BlueInARow = True
					else:
						RedInARow = True
				previous = Grid[rowCount][colCount]
			rowCount+=1
			colCount+=1 
#	print 3
	for i in range(K-1,length):
		previous = Grid[0][i]
		rowCount = 1
		colCount = i-1
		inARowCounter = 1
		while colCount >=0:
			if previous!=0:
				if Grid[rowCount][colCount] == previous:
					inARowCounter+=1
				else:
					inARowCounter=1
				if inARowCounter == K:
					if previous == Blue:
						BlueInARow = True
					else:
						RedInARow = True
				previous = Grid[rowCount][colCount]
			rowCount+=1
			colCount-=1
#	print 4
	for i in range(1,length-K+1):
		previous = Grid[i][length-1]
		rowCount = i+1
		colCount = length-2
		inARowCounter = 1
		while rowCount < length:
			if previous!=0:
				if Grid[rowCount][colCount] == previous:
					inARowCounter+=1
				else:
					inARowCounter=1
				if inARowCounter == K:
					if previous == Blue:
						BlueInARow = True
					else:
						RedInARow = True
				previous = Grid[rowCount][colCount]
			rowCount+=1
			colCount-=1 
	return [RedInARow,BlueInARow]
		

def RowTest(Grid,length,K):
	RedInARow = False
	BlueInARow = False
	for row in Grid:
		previous = row[0]
		colCount = 1
		inARowCounter=1
		while colCount<length:
			if previous!=0:
				if row[colCount] == previous:
					inARowCounter+=1
				else:
					inARowCounter=1
				if inARowCounter == K:
					if previous == Blue:
						BlueInARow = True
					else:
						RedInARow = True
					inARowCounter =1
			previous = row[colCount]
			colCount+=1
	return [RedInARow,BlueInARow]
						
def ColTest(Grid,length,K):	
	RedInARow = False
	BlueInARow = False
	colCount=0
	rowCount=0
	while colCount<length:
		previous = Grid[0][colCount]
		rowCount = 1
		inARowCounter = 1
		while rowCount<length:
			if previous!=0:
				if Grid[rowCount][colCount] == previous:
					inARowCounter+=1
				else:
					inARowCounter=1
				if inARowCounter == K:
					if previous == Blue:
						BlueInARow = True
					else:
						RedInARow = True
					inARowCounter =1
			previous = Grid[rowCount][colCount]
			rowCount+=1
		colCount+=1
	return [RedInARow,BlueInARow]	




def Rotate(oldGrid,length):
	row = length -1
	col = length -1
	newGrid = [[]]
	rowCounter = 0
	colCounter = 0
	while rowCounter<length-1:
		while colCounter<length:
			newGrid[rowCounter] += [0,]
			colCounter+=1
		rowCounter+=1
		newGrid+=[[],]
		colCounter = 0
	while colCounter<length:
		newGrid[rowCounter] += [0,]
		colCounter+=1
	newRow = 0
	newCol = 0
	while row>= 0:
		while col>=0:
#			print row
#			print col
			if oldGrid[row][col]!=0:
				newGrid[newRow][newCol] = oldGrid[row][col]
				newCol+=1
			else:
				newGrid[newRow][newCol] = 0
			col-=1
		while newCol<length:
			newGrid[newRow][newCol] = 0
			newCol +=1
			
		row-=1
		newRow+=1
		col =length-1
		newCol = 0
	return newGrid
	
def Test(number):
	a=input.readline().split()
	print a
	length=int(a[0])
	K = int(a[1])
	tempGrid=[]
	counter = 0
	for i in range(0,length):
		tempGrid+=[input.readline()[:-1],]
	newGrid = [[]]
	rowCounter = 0
	colCounter = 0
	while rowCounter<length-1:
		while colCounter<length:
			newGrid[rowCounter] += [0,]
			colCounter+=1
		rowCounter+=1
		newGrid+=[[],]
		colCounter = 0
	while colCounter<length:
		newGrid[rowCounter] += [0,]
		colCounter+=1
	row=0
	col=0
	print tempGrid
	for i in range(0,length):
		for j in tempGrid[i]:
			if j == "B":
				newGrid[row][col] = Blue
			elif j == "R":
				newGrid[row][col]=Red
			else:
				newGrid[row][col] = 0
			
			col+=1
		row+=1
		col = 0	
	newGrid = Rotate(newGrid,length)
	A = ColTest(newGrid,length,K)
	B = RowTest(newGrid,length,K)
	C = DiagnolTest(newGrid,length,K)
	red = A[0] or B[0] or C[0]
	blue = A[1] or B[1] or C[1]
	if red and blue:
		fout.write("Case #%d: Both\n" % number)	
	elif blue:
		fout.write("Case #%d: Blue\n" % number)	
	elif red:
		fout.write("Case #%d: Red\n" % number)
	else:
		fout.write("Case #%d: Neither\n" % number)
		

input = open('A-small-attempt1.in', 'r')
fout = open("output.txt","w")
total = int(input.readline())
for whatever in range(1,total+1):
	Test(whatever)

	