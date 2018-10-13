
def PrintRes(Res,num):
	fdOut.write("Case #"+str(num+1)+": %d\r\n" % Res)



fdIn = open("/home/aviv/Desktop/Code/CodeJam/2015/standingOvation/A-large.in","rb")
fdOut = open("/home/aviv/Desktop/Code/CodeJam/2015/standingOvation/A-large.out","w")

LinesNum=int(fdIn.readline().strip())
for num in xrange(LinesNum):
	testCase = fdIn.readline().strip().split()
	maxShy = int(testCase[0])
	currStanding = 0
	minPeople = 0
	for currShy in xrange(maxShy+1): 
		currShyPeople = int(testCase[1][currShy])
		if currShy <= currStanding:
			currStanding += currShyPeople
		else:
			addedPeople = currShy - currStanding		
			minPeople += addedPeople
			currStanding += currShyPeople + addedPeople
	PrintRes(minPeople,num)

fdIn.close()
fdOut.close()		
		

	
	
	
