from sets import Set
file1 = open("q2Test.txt","r")
numOfTestCases = 0

numOfTestCases = int(file1.readline())
results = []
for i in xrange(numOfTestCases):
	rateOfGettingCookies = 2.0
	numofcookies = 0.0
	numoffarms = 0
	a = file1.readline()
	c = 0
	f = 0
	x = 0
	word = a.split()
	c = float(word[0].rstrip("\n "))
	f = float(word[1].rstrip("\n "))
	x = float(word[2].rstrip("\n "))

	timeSpent = 0.0
	while(numofcookies<x):
		currentTime = 0.0
		currentTimeWithFarm = 0.0
		currentTime = (x-numofcookies)/rateOfGettingCookies
		if numofcookies > c:
			currentTimeWithFarm = (x-numofcookies+c)/(rateOfGettingCookies+f)
		else:
			currentTimeWithFarm = (c-numofcookies)/rateOfGettingCookies + x/(rateOfGettingCookies+f)
		#print currentTime,currentTimeWithFarm,c,f,x
		if(currentTimeWithFarm<currentTime):
			if numofcookies>c:
				numofcookies-=c
			else:
				numofcookies = 0
				timeSpent += (c-numofcookies)/rateOfGettingCookies
			rateOfGettingCookies+=f
		else:
			numofcookies = x
			timeSpent = timeSpent+currentTime
	results.append(timeSpent)

for i in xrange(len(results)):
	print "Case #{0}: {1}".format(i+1,results[i])