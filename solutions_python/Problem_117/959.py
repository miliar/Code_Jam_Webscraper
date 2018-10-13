def main():
#	fileIn = "inputsample.txt"
#	fileIn = "B-small-attempt0.in"
	fileIn = "B-large.in"
#	fileIn = "inputsamplebig.txt"
	fileOut = "output.txt"
	
	fin = open(fileIn, 'r')
	fout = open(fileOut, 'w')
	counter = 1
	isFirstLine = True
	
	cases = int(fin.readline())
	for case in range(cases):
		outputStr = "Case #" + str(counter) + ": "
		
		# Read in the inputs
		tempLineArr = fin.readline().split(' ')
		N = int(tempLineArr[0])		# Rectangle's dimensions are NxM
		M = int(tempLineArr[1])
		y = N	# of rows
		x = M	# of cols
		lawnArr = []
		isValid = True
		az = 1
		for a1 in range(N):
			tempLineArr = fin.readline().strip().split(' ')
#			print "Case " + str(counter) + ", tempLineArr " + str(az) + ":"
#			print tempLineArr
			az = az + 1
			tempIntMap = map(int,tempLineArr)
			lawnArr.append(tempIntMap)
			
		# Process the scenario now
		for row in lawnArr:
#			print "Row (Max " + str(maxVal)
#			print row
			posX = 0
			while((posX < x) and (isValid == True)):
				if(row[posX] < max(row)):
					# Horizontal cut won't work - try vertical
					posY = 0
					while((posY < y) and (isValid == True)):
						if(row[posX] < lawnArr[posY][posX]):
							isValid = False
						posY = posY + 1
				posX = posX + 1
		
		
		if(isValid == True):
			outputStr = outputStr + "YES"
		else:
			outputStr = outputStr + "NO"		
		# Write to the output file
		if(isFirstLine):
			fout.write(outputStr)
			isFirstLine = False
		else:
			fout.write("\n" + outputStr)
		
		# Increment the case counter
		counter = counter + 1	
	
	# Close the files
	fin.close()
	fout.close()
	
def	appendStrings(boardArr):
	# The row strings already exist in the array.
	# Now, add the column ones
	for column in range(4):
		tempStr = ""
		for row in range(4):
			tempStr = tempStr + boardArr[row][column]
		boardArr.append(tempStr)
	
	# Now add the diagonals
	tempStr = boardArr[0][0] + boardArr[1][1] + boardArr[2][2] + boardArr[3][3]
	boardArr.append(tempStr)
	tempStr = boardArr[3][0] + boardArr[2][1] + boardArr[1][2] + boardArr[0][3]
	boardArr.append(tempStr)
	
	return boardArr

def checkForWin(boardArr, player):
	for row in boardArr:
		if(row.count(player) == 4):
			return True
		elif((row.count(player) == 3) and (row.count('T') == 1)):
			return True
	return False
	
if __name__ == '__main__':
	main()