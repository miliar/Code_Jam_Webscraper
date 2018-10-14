import sys
import logging

def magicIO(inName, outName): #this reads the guesses and cards
	#open file
	fin = open(inName)
	T = int(fin.readline())
	fout = open(outName,'w')

	#looping cases
	for testcase in range(0,T):
		logging.debug("Case #" + str(testcase+1) + ":")
		
		#reading flie
		ans1 = int(fin.readline())
		for row in range(0,ans1-1):  #looping dump rows
			fin.readline()
		row1 = map(int, fin.readline().split()) #read row
		for row in range(0, 4-ans1): #looping dump rows
			fin.readline()
		logging.debug(">> Row" + str(ans1) + ": " + str(row1))

		ans2 = int(fin.readline())
		for row in range(0,ans2-1):  #looping dump rows
			fin.readline()
		row2 = map(int, fin.readline().split()) #read row
		for row in range(0, 4-ans2): #looping dump rows
			fin.readline()
		logging.debug(">> Row" + str(ans2) + ": " + str(row2))
		
		#guess cases and output
		guess = magicTrick(row1, row2)
		result= "Case #" + str(testcase+1) + ": "
		if len(guess) == 1:
			result = result + str(guess[0])
		elif len(guess) > 1:
			result = result + "Bad magician!"
		else:
			result = result + "Volunteer cheated!"
		logging.info(result)
		fout.write(result+"\n")

	#done and closing
	fout.close()
	fin.close()




def magicTrick(row1, row2):
	result = filter(lambda x: x in row1, row2)
	return result	



if __name__ == '__main__':
	logger = logging.getLogger()
	logger.setLevel(logging.DEBUG)

	inName = "example.in"
	outName = "output"
	if len(sys.argv) == 2:
		inName = sys.argv[1]
	elif len(sys.argv) > 2:
		logging.error(" Usage: solution.py filename")
		sys.exit(0)
	logging.info( "Running MagicTrick: " + inName + " > " + outName)
	magicIO(inName, outName)
