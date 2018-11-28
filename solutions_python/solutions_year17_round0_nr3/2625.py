t = int(raw_input())
for i in range(1,t+1):
	nBathroomStalls,nOccupants = raw_input().split(" ")
	nBathroomStalls = int(nBathroomStalls)
	anOccupied = [0,nBathroomStalls+1]
	lastOccupiedStall = []
	for j in range(0,int(nOccupants)):
		nIndex = 1
		nMinSoFar = -1
		aLR = []
		for k in range(1,nBathroomStalls+1):
			if anOccupied[nIndex] > k:
				LR = [k,k - anOccupied[nIndex-1] - 1, anOccupied[nIndex] - k - 1]
				nCurrentMin = min(LR[1],LR[2])
				if nMinSoFar < nCurrentMin:
					nMinSoFar = nCurrentMin
					aLR = [[LR[0],LR[1],LR[2]]]
				else:
					if nMinSoFar == nCurrentMin:
						aLR += [[LR[0],LR[1],LR[2]]]
			else:
				nIndex += 1
		if len(aLR) == 1:
			count = 0
			while anOccupied[count] < aLR[0][0]:
				count += 1
			anOccupied.insert(count,aLR[0][0])
			lastOccupiedStall = aLR[0]
		else:
			nMaxSoFar = -1
			aLRMax = []
			for l in range(0,len(aLR)):
				nCurrentMax = max(aLR[l][1],aLR[l][2])
				if nMaxSoFar < nCurrentMax:
					nMaxSoFar = nCurrentMax
					aLRMax = [[aLR[l][0],aLR[l][1],aLR[l][2]]]
				elif nMaxSoFar == nCurrentMax:
					aLRMax += [[aLR[l][0],aLR[l][1],aLR[l][2]]]
			count = 0
			while anOccupied[count] < aLRMax[0][0]:
				count += 1
			anOccupied.insert(count,aLRMax[0][0])
			lastOccupiedStall = aLRMax[0]
	print "Case #%d: %d %d" % (i,lastOccupiedStall[2],lastOccupiedStall[1])




