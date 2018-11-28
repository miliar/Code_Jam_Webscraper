#!/usr/bin/python
def calculateWar(nList, kList):
	nPoint = 0
	# Modify a copy of the list since we need it intact for deceit war
	nListCopy = list(nList)
	kListCopy = list(kList)

	# Ken will follow this strategy in War
	# Pick the smallest block heavier than what naomi said. If not
	# available, pick the least weighing block and lose a point.
	# Assume Naomi picks one block after another, starting with smallest
	for nVal in nListCopy :
		if (kListCopy[len(kListCopy) -1] < nVal) :
			#Ken burns his lowest block and loses 1 point
			kListCopy.pop(0)
			nPoint = nPoint + 1
		else :
			for j in range (0, len(kListCopy)) :
				if kListCopy[j] > nVal:
					#point goes to Ken
					kListCopy.pop(j)
					break
	return nPoint

def calculateDWar(nList, kList) :
	#In this case, Naomi tries to win as many points as possible by following this strategy.
	#For every block of hers, if she finds Ken having a smaller block, she declares the weight to be
	# larger than Ken's largest block. This way, he puts his lowest block and loses points.
	# If she cannot find a smaller block in Ken's list, she gives out a number slightly less than his
	#largest block,  making Ken lose his biggest blocks, but gaining a point.
	nPoint = 0
	for nVal in nList:
		if (kList[0] < nVal) :
			nPoint = nPoint + 1
			kList.pop(0)
		else:
			kList.pop()
	return nPoint	

def getList(data) :
	weightList = []
	for n in data:
		weightList.append(float(n))

	weightList.sort()
	return weightList

def main() :
	fobj = open("war-input")
	writeobj = open("war-output.txt", 'w')
	caseNum = int(fobj.readline())
	print("No of cases is %d" %caseNum)
	for i in range (0, caseNum) :
		numBlocks = int(fobj.readline())
		nData = fobj.readline().split(' ')		
		kData = fobj.readline().split(' ')
		nList = getList(nData)
		kList = getList(kData)
		warScore = calculateWar(nList, kList)
		dwarScore = calculateDWar(nList, kList)
		writeobj.write("Case #%d: %d %d\n" %(i + 1, dwarScore, warScore)) 

	writeobj.close()
	fobj.close()

main()
