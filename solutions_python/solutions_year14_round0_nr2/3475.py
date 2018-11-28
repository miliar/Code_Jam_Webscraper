def calculateTimeForFarms(c,f,n):
	cookiesPerSecond=2.0
	currentTime=0.0
	if(n==0):
		return currentTime
	for i in range(n):
		currentTime=currentTime+(c/cookiesPerSecond) # time until next farm
		cookiesPerSecond=cookiesPerSecond+f #cookie production increases
	return currentTime

def calculateTimeForWaiting(f,x,n):
	cookiesPerSecond=2.0
	if(n>0):
		cookiesPerSecond=cookiesPerSecond+(n*f)
	currentTime=x/cookiesPerSecond
	return currentTime

row={}
fIn = open( "small.in", "r" )
fOut=open("result.out","w")
testCaseNumber=int(fIn.readline())

for i in range(testCaseNumber):
	row=fIn.readline().split()
	c=float(row[0])
	f=float(row[1])
	x=float(row[2])

	numberOfFarms=0
	timeForFarms=0
	previousTime=-1
	totalTime=0.0
	solved=False
	while(solved==False):
		timeForFarms=calculateTimeForFarms(c,f,numberOfFarms)
		timeForWaiting=calculateTimeForWaiting(f,x,numberOfFarms)
		totalTime=timeForFarms+timeForWaiting
		if(totalTime>previousTime and previousTime!=-1):
			solved=True
		else:
			numberOfFarms=numberOfFarms+1
			previousTime=totalTime
	fOut.write("Case #"+str(i+1)+": %.7f" % previousTime)

	if(i!=testCaseNumber-1):
		fOut.write("\n")

fIn.close()
fOut.close()