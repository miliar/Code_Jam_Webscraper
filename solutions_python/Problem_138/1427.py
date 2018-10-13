#Google Code Jam: Qualification Round - D. Deceitful War

inputfile = open('D-large.in')
outputfile = open('output.txt', 'w')
currentCase = []
warData = []
caseIndex = 0
caseNum = 1
numCases = int(inputfile.readline())

#Build the data list
for line in inputfile:
	currentLine = line.strip().split(' ')
	for num in currentLine:
		currentCase.append(float(num))
	warData.append(currentCase)
	currentCase = []

#Determine Solution
while caseIndex < 3*numCases:
	N_Blocks = warData[caseIndex+1]
	K_Blocks = warData[caseIndex+2]
	N_Blocks_D = N_Blocks[:]
	K_Blocks_D = K_Blocks[:]
	N_Blocks.sort()
	K_Blocks.sort()
	N_Blocks_D.sort()
	K_Blocks_D.sort()
	N_Score = 0
	N_Score_D = 0

	#Determine War Score
	while N_Blocks:
		N_Pick = N_Blocks[0]
		for block in K_Blocks:
			if block > N_Pick:
				K_Pick = block
				break
			else:
				K_Pick = K_Blocks[0]
		if N_Pick > K_Pick:
			N_Score += 1
		N_Blocks.remove(N_Pick)
		K_Blocks.remove(K_Pick)

	#Determine Deceitful War Score
	while N_Blocks_D:
		j = len(N_Blocks_D)
		for i in range(j):
			if N_Blocks_D[i] < K_Blocks_D[i]:
				N_Blocks_D.pop(i)
				K_Blocks_D.pop(-(i+1))
				j = len(N_Blocks_D)
				break
			else:
				N_Score_D += 1
				N_Blocks_D.pop(i)
				K_Blocks_D.pop(i)
				j = len(N_Blocks_D)
				break

	outputfile.write('Case #' + str(caseNum) + ': ' + str(N_Score_D) + ' ' + str(N_Score) + '\n')
	caseIndex += 3
	caseNum += 1