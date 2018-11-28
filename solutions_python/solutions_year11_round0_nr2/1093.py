if __name__ == '__main__':
	fin = open("B-small-attempt0.in", 'r')
	fout = open("out.txt", 'w')
	numCases = int(fin.readline())
	for item in range(numCases):
		inpLine = fin.readline().split()
		i = 0
		numC = int(inpLine[i])
		i += 1
		combine = {}
		for numC in range(numC):
			itemC = inpLine[i]
			combine[itemC[0] + itemC[1]] = itemC[2]
			i += 1

		numOpp = int(inpLine[i])
		i += 1
		oppose = {}
		for numOpp in range(numOpp):
			itemOpp = inpLine[i]
			oppose[itemOpp[0]] = itemOpp[1]
			oppose[itemOpp[1]] = itemOpp[0]
			i += 1	

		numInsert = int(inpLine[i])
		i += 1
		initialList = inpLine[i]
		finalList = []
		finalList.append(initialList[0])
		for index in range(1, numInsert):
			currItem = initialList[index]

			if not len(finalList):
				finalList.append(currItem)
				continue
			possibleComb = currItem +  finalList[-1]
			possibleComb1 = finalList[-1] + currItem
			if possibleComb in combine.keys():
				finalList[-1] = combine[possibleComb]
				continue
			elif possibleComb1 in combine.keys():
				finalList[-1] = combine[possibleComb1]
				continue

			if (currItem in oppose.keys()) and (oppose[currItem] in finalList):
				finalList = []
				continue
			finalList.append(currItem)
		fout.write('Case #%d: %s\n'%(item+1, '[' + ', '.join(finalList) + ']'))
