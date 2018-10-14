
inFile = open('./A-small-attempt2.in', 'r')
outFile = open('./output.out', 'w')
caseNum = int(inFile.readline())
for num in range(1, caseNum + 1) :
	
	vecList1 = [[0 for col in range(4)] for row in range(4)]
	vecList2 = [[0 for col in range(4)] for row in range(4)]
	
	cnt = 0

	row1 = int(inFile.readline())-1	
	
	for i in range(0,4) :
		vecStr = inFile.readline().split(' ')
		for j in range(0,4) :
			vecList1[i][j] = int(vecStr[j])
			
	row2 = int(inFile.readline())-1	
	
	for i in range(0,4) :
		vecStr = inFile.readline().split(' ')
		for j in range(0,4) :
			vecList2[i][j] = int(vecStr[j])

		
	for i in range(0,4) :
		for j in range(0,4) :
			if vecList1[row1][i] == vecList2[row2][j] :
				cnt += 1
				card = vecList1[row1][i]	
			
	if cnt > 1 :
		print('Case #%d: Bad magician!' %num, file = outFile)
	elif cnt == 0 :
		print('Case #%d: Volunteer cheated!' %num, file = outFile)
	else :
		print('Case #%d: %d' %(num,card), file = outFile)
