import math

def main():
#	fileIn = "inputsample.txt"
	fileIn = "C-small-attempt0.in"
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
		A = long(tempLineArr[0])
		B = long(tempLineArr[1])
			
		# Process the scenario now
		fairSquareCounter = long(0)
		pos = A	
		while(pos < (B+1)):
			if(isFair(pos) and isSquare(pos)):
#				print "Found a match: " + str(pos)
				fairSquareCounter = fairSquareCounter + 1
			pos = pos + 1
		
		outputStr = outputStr + str(fairSquareCounter)
		
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

def isFair(number):
	numStrf = str(number)
	numStrb = numStrf[::-1]
	return (numStrf == numStrb)
	
def isSquare(number):
	# First, see if the number has an integer/long square root
	root = long(math.sqrt(number))
	if((root * root) != number):
		return False
	else:
		# We know it's a square. Now, is that square root a palindrome?
		return isFair(root) 
			
if __name__ == '__main__':
	main()