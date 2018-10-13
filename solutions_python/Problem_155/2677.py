fin = open("A-Large.in", 'r')
fout = open("outputFileLarge.txt", 'w')
totalTestCases = int(fin.readline())
caseNo = 1
while caseNo <= totalTestCases:
	sMax, audience = fin.readline().split()
	sMaxInt = int(sMax)
	indexes = list()
	friendsRequired = 0
	# Using this while I have calculated list of indexes of 0
	while (sMaxInt >= 0):
		if (audience[sMaxInt] == '0'):
			indexes.append(sMaxInt)
		sMaxInt -= 1
	indexes.sort()
	if len(indexes) != 0:
		for audienceRequired in indexes:
			actualAudience = 0
			loop = audienceRequired - 1
			while loop >= 0:
				actualAudience += int(audience[loop])
				loop -= 1
			actualAudience += friendsRequired
			if (actualAudience < (audienceRequired + 1)):
				friendsRequired += 1
		fout.write("Case #{0}: {1}\n".format(caseNo, friendsRequired))
	else:
		fout.write("Case #{}: 0\n".format(caseNo))
	caseNo += 1
