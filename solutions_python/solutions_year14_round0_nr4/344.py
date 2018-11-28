#!/usr/bin/env python

inFile = open("D-large.in.txt", 'r')
numbers = int(inFile.readline())
c = 1
results = ""
while c <= numbers:
	totalWood = int(inFile.readline())
	naomiStr = inFile.readline()
	if naomiStr[len(naomiStr)-1] == '\n':
		naomiStr = naomiStr[0:len(naomiStr)-1]
	kenStr = inFile.readline()
	if kenStr[len(kenStr)-1] == '\n':
		kenStr = kenStr[0:len(kenStr)-1]
	naomiStr = naomiStr.replace('0.', '')
	kenStr = kenStr.replace('0.', '')
	naomiWood = naomiStr.split(' ')
	kenWood = kenStr.split(' ')
	for i in range(totalWood):
		naomiWood[i] = int(naomiWood[i])
		kenWood[i] = int(kenWood[i])
	warScore = 0
	deceitfulScore = 0
	naomiWood.sort()
	kenWood.sort()
	naomiWood.reverse()
	kenWood.reverse()
	# get the war score
	kenTemp = kenWood[:]
	naomiTemp = naomiWood[:]
	while True:
		if len(naomiTemp) == 0 :
			break
		if naomiTemp[0] >= kenTemp[0]:
			warScore += 1
			naomiTemp.pop(0)
			kenTemp.pop()
		elif naomiTemp[0] < kenTemp[len(kenTemp)-1]:
			break
		else:
			popIndex = 0
			while naomiTemp[0] < kenTemp[popIndex+1]:
				popIndex += 1
			naomiTemp.pop(0)
			kenTemp.pop(0)
	# get the deceitful score
	kenTemp = kenWood[:]
	naomiTemp = naomiWood[:]
	while True:
		if len(naomiTemp) == 0:
			break
		if naomiTemp[len(naomiTemp) - 1] > kenTemp[len(kenTemp) - 1]:
			deceitfulScore += 1
			naomiTemp.pop()
			kenTemp.pop()
		elif naomiTemp[len(naomiTemp)-1]  > kenTemp[0]:
			deceitfulScore += len(naomiTemp)
		else:
			popIndex = 0
			while kenTemp[0] - popIndex + 1 in kenTemp:
				popIndex += 1
			naomiTemp.pop()
			kenTemp.pop(popIndex)
	results += "Case #" + str(c) + ": " + str(deceitfulScore) + ' ' + str(warScore) + '\n'
	c += 1
outFile = open("D-large.out.txt", 'w')
outFile.write(results[0:len(results)-1])