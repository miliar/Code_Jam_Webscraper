import sys
import logging

def cookieIO(inName, outName): #this reads the guesses and cards
	#open file
	fin = open(inName)
	T = int(fin.readline())
	fout = open(outName,'w')

	#looping cases
	for testcase in range(0,T):
		logging.debug("Case #" + str(testcase+1) + ":")
		
		#reading file and run cases
		thisline = map(float, fin.readline().split())
		result= "Case #" + str(testcase+1) + ": " + str("%.7f" % cookieClicker(thisline[0],thisline[1],thisline[2]))
		
		logging.info(result)
		fout.write(result+"\n")

	#done and closing
	fout.close()
	fin.close()




def cookieClicker(C, F, X):
	logging.debug("C:" + str(C) + " F:" + str(F) + " X:" + str(X))
	InitialSpeed = 2 #cookies per second
	timeSpent = 0;
	newTime = 0
	farmCost = C
	farmSpeed = F
	cookieTarget = X
	curSpeed = InitialSpeed

	while True:
		if cookieTarget < farmCost:
			timeSpent = cookieTarget / curSpeed
			break
		else: 
			newTime = farmCost / curSpeed
			if makeFarm(curSpeed, farmSpeed, farmCost, cookieTarget):
				timeSpent += newTime
				curSpeed += farmSpeed
			else:
				timeSpent += cookieTarget / curSpeed
				break


	return timeSpent
	#return cookieCalc(C, F, X, InitialSpeed)


def makeFarm(oldSpeed, farmSpeed, cost, target):
	#calculate Math here
	if (target-cost) / oldSpeed < target / (oldSpeed + farmSpeed):
		return False
	else:
		return True



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
	cookieIO(inName, outName)
