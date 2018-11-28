def main():
#	fileIn = "inputsample.txt"
#	fileIn = "inputsamplebig2.txt"
#	fileIn = "A-small-attempt0.in"
	fileIn = "A-large.in"
	fileOut = "output.txt"
	
	fin = open(fileIn, 'r')
	fout = open(fileOut, 'w')
	counter = 1
	isFirstLine = True
	
	cases = int(fin.readline())
	for case in range(cases):
		outputStr = "Case #" + str(counter) + ": "
		
		# Read in the inputs
		boardArr = []
		for a1 in range(4):
			boardArr.append(fin.readline().strip())
		fin.readline()	# Skip a line		
		
		boardArr = appendStrings(boardArr)
		if(checkForWin(boardArr,'X')):
			outputStr = outputStr + "X won"
		elif(checkForWin(boardArr,'O')):
			outputStr = outputStr + "O won"
		else:
			gameNotDone = False
			for row in boardArr:
				if(row.find(".") > -1):
					gameNotDone = True
			if(gameNotDone):
				outputStr = outputStr + "Game has not completed"
			else:
				outputStr = outputStr + "Draw"
		
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