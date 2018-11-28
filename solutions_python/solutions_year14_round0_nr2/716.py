"""
Written for Google Code Jam 2014
Kolijn Wolfaardt
kolijn.wolfaardt@gmail.com
"""

f = open('cookie/B-large.in','r')

#Read the number of test cases
T = int(f.readline())

for t in range(T):
	line = f.readline().split()

	#This is me, not reading the specification beforehand
	C= 2
	farmCost = float(line[0])
	F = float(line[1])
	X = float(line[2])

	totalTime=0

	#First, check that the final score is larger than the farm cost
	winning=100 #Go away, Charlie Sheen
	production=C
	#We're at the minimum now, calc time 
	currentTime=0
	
	timeToWin = X/production

	while (winning>0):
		if (currentTime > timeToWin):
			winning=0
		else:
			#Uncomment to stop endless execution.
			#winning = winning-1

			#We've just started, of just bought a farm
			#calculate the new time to win
			newTimeToWin = currentTime+X/production


			#replace the old value, if it's bigger
			if newTimeToWin<timeToWin:
				timeToWin = newTimeToWin

			#Wait to buy a farm
			currentTime = currentTime + farmCost/production
			production = production+F
	print ("Case #{}: {:.7f}".format(t+1,timeToWin))


			

