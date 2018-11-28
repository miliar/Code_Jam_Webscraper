
fileIn = open('in.txt','r')
fileOut = open('out.txt','w')

#read number of tests
nCases = fileIn.readline().strip()

for i in range(int(nCases)):
	caseLine = fileIn.readline().strip().split(" ")
	housePrice = float(caseLine[0])
	cookiePerHouse = float(caseLine[1])
	goal = float(caseLine[2])
	cookies = float(0.0)
	houseCount = 0
	timeElapsed = float(0.0)

	if goal <= housePrice:
		timeElapsed = goal/2
	else:
		while  goal/(houseCount*cookiePerHouse+2) >  goal/((houseCount+1)*cookiePerHouse+2) + housePrice/((houseCount)*cookiePerHouse+2):
			#calculate time to buy next house
			t = housePrice/(houseCount*cookiePerHouse+2)
			timeElapsed += t
			houseCount +=1
			

		timeElapsed += goal/(houseCount*cookiePerHouse+2)

	result = "Case #" + str(i+1) + ": " + str(timeElapsed)
	print result
	fileOut.write(result + "\n")

fileOut.close()

