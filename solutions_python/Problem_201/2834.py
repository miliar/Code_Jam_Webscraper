import math
test1 = [
	1,0,1,0,0,0,0,1,1,0,
	0,1,1,0,0,0,0,1,1,1,
	0,0,0,1,1,1,0,0,0,0,
	0,0,0,0,0,0,0,1,1,0,
	1,0,1,0,1,0,1,0,1]
test = [1,0,0,0,0,0,1] 

def initStalls(n):
	arr = []
	a = 0
	while a < n+2:
		arr.append(0)
		a += 1
	arr[0] = 1
	arr[len(arr) - 1] = 1
	return arr

def insertIntoStalls(stalls,i):
	stalls[int(i)] = 1
	return stalls
	
def getOccupiedList(stalls):
	temp = []
	for i in range(0,len(stalls)):
		if stalls[i] == 1:
			temp.append(i)
	return temp
	
def getLargestGapAmount(stalls):
	occupied =getOccupiedList(stalls)
	localMax = 0 
	for i in range(0,len(occupied)):
		localMax = max(((occupied[i] - occupied[i-1]) -1),localMax)
	return localMax

def getLargestGapleftCoordinate(stalls):
	occupied =getOccupiedList(stalls)
	localMax = 0 
	leftCoord = 0
	for i in range(0,len(occupied)):
		if max(((occupied[i] - occupied[i-1]) -1),localMax) != localMax:
			leftCoord = occupied[i-1]
		localMax = max(((occupied[i] - occupied[i-1]) -1),localMax)
	return leftCoord
	
def getLs(stalls,pos):
	occupied =getOccupiedList(stalls)
	for i in range(0,len(occupied)):
		if occupied[i] == pos:
			return (occupied[i] - occupied[i-1]) -1
		elif occupied[i] > pos:
			return (pos - occupied[i-1]) -1
			
def getRs(stalls,pos):
	occupied =getOccupiedList(stalls)
	for i in range(0,len(occupied)):
		if occupied[i] == pos:
			return (occupied[i+1] - occupied[i] ) -1
		elif occupied[i] > pos:
			return (occupied[i] - pos) -1

def getPositionToGo(stalls):
	occupied = getOccupiedList(stalls)
	gap = getLargestGapAmount(stalls)
	gapLeft = getLargestGapleftCoordinate(stalls)
	
	if gap % 2 == 0:
		return gapLeft + (gap / 2)
	else:
		return gapLeft + math.ceil(gap / 2) + 1

def run(stalls,people):
	stalls = initStalls(stalls)
	for i in range(0,people):
		targetStall = getPositionToGo(stalls)
		if i == people - 1:
			return [int(max(getLs(stalls,targetStall), getRs(stalls,targetStall))),int(min(getLs(stalls,targetStall), getRs(stalls,targetStall)))]
		stalls = insertIntoStalls(stalls,targetStall)
   
#print getLargestGap(getOccupiedList(test))
#print getRs(test,8)
#print getPositionToGo(test)    
print run(1000,1)

lines = open('input.txt').readlines()
q = 1
for line in lines:
	lineArr = line.split()
	if len(lineArr)  == 2:
		out = run(int(lineArr[0]),int(lineArr[1]))
		print "case #" + str(q)  + ": " + str(out[0]) + " " + str(out[1])
		q += 1











	