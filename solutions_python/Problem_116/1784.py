#0 not ended
#1 draw
#2 x wins
#3 o wins

def GetResult(line):
	if 'X' in line and 'O' not in line and '.' not in line:
		return 2#2 x wins
	elif 'O' in line and 'X' not in line and '.' not in line:
		return 3#3 o wins
	elif '.' in line:
		return 0#0 not ended
	return 1 #1 draw

def LineWin(testCase):
	isDraw=0
	for line in testCase:
		result=GetResult(line)
		if result in [2,3]:
			return result
		else:
			isDraw+=result
		
	if isDraw==4:
		return 1
	else:
		return 0

def ColumnWin(testCase):
	isDraw=0
	for i in range(0,4):
		column=testCase[0][i]+testCase[1][i]+testCase[2][i]+testCase[3][i]
		result=GetResult(column)
		if result in [2,3]:
			return result
		else:
			isDraw+=result
		
	if isDraw==4:
		return 1
	else:
		return 0

def DiagonalWin(testCase):
	diagonal1=testCase[0][0]+testCase[1][1]+testCase[2][2]+testCase[3][3]
	diagonal2=testCase[0][3]+testCase[1][2]+testCase[2][1]+testCase[3][0]
	result=GetResult(diagonal1)
	if result in [2,3]:
		return result

	result=GetResult(diagonal2)
	if result in [2,3]:
		return result
	
	return 1


fileName=raw_input("Name of the input file or full path:")
fileHandle=open(fileName,'r')

allLines=fileHandle.readlines()
fileHandle.close()

results={0:'Game has not completed', 1:"Draw", 2:"X won", 3:'O won'}
testCases=[]
count=0

for line in allLines[1:]:
	if count==0:
		oneCase=[]

	if len(line)==5:
		oneCase.append(line[:-1])
		count+=1
	if count==4:
		count=0
		testCases.append(oneCase)

count=0
outputFile=open(fileName.split('.')[0]+'.out','a')
for aCase in testCases:
	count+=1
	if count>1:
		outputFile.write('\n')
	isDraw=0
	#Line verify
	result=LineWin(aCase)
	if result in [2,3]:
			outputFile.write('Case #'+str(count)+': '+results[result])
	else:
		isDraw+=result
		result=ColumnWin(aCase)
		if result in [2,3]:
			outputFile.write('Case #'+str(count)+': '+results[result])
		else:
			isDraw+=result
			result=DiagonalWin(aCase)
			if result in [2,3]:
				outputFile.write('Case #'+str(count)+': '+results[result])
			elif isDraw>0:
				outputFile.write('Case #'+str(count)+': '+results[1])
			else:
				outputFile.write('Case #'+str(count)+': '+results[0])
outputFile.close()