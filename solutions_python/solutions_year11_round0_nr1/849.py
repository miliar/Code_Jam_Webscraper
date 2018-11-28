import math



def nextLocation(buttonList, color, currentListLoc):
	loc = currentListLoc+1
	while loc < len(buttonList) and buttonList[loc]!=color:
		loc+=1
	
	if loc==len(buttonList):
		return [int(buttonList[currentListLoc]), currentListLoc]
	else:
		return [int(buttonList[loc+1]), loc+1]
	
def getDirection(currentLoc, targetLoc):
	direction = [0,0]
	for i in range (0,2):
		if currentLoc[i]<targetLoc[i]:
			direction[i]=1
		elif currentLoc[i]>targetLoc[i]:
			direction[i]=-1
		
	return direction


directory = "/Users/se/Downloads/"

inFile=directory+"A-large.in"
outfile = directory+"test.out"

input = open(inFile)
output = open(outfile, "w")

line = input.readline().strip()
cases = int(line)

for case in range (0, cases):
	lineElements = input.readline().strip().split(' ')
	noButtons = int(lineElements[0])

	currentButton = 0
	targetButton = [lineElements[2*currentButton+1], int(lineElements[2*currentButton+2])]
	noMoves = 0
	colorMap = ['O','B']
	listLoc=[-1,-1]
	targetLoc=[0,0]
	for i in range (0,2):
		[targetLoc[i], listLoc[i]] = nextLocation(lineElements, colorMap[i], listLoc[i])
		
	currentLoc = [1,1]
	
	
	while (currentButton < noButtons):
		buttonPushed = False	
		direction = getDirection(currentLoc, targetLoc)
		for i in range (0,2):
			if [colorMap[i], currentLoc[i]] == targetButton and buttonPushed ==False:
				buttonPushed=True
				currentButton+=1
				if currentButton < noButtons:
					targetButton = [lineElements[2*currentButton+1], int(lineElements[2*currentButton+2])]
				[targetLoc[i], listLoc[i]] = nextLocation(lineElements, colorMap[i], listLoc[i])
			else: 
				currentLoc[i]+=direction[i]
				
		noMoves+=1

	print >> output, "Case #%d: %d" % (case+1, noMoves)
	print "Case #%d: %d" % (case+1, noMoves)



