import os

def parser(filename):
	cases=[]
	with open(filename) as inFile:
		numIterations = int(inFile.readline())
		for i in range(0,numIterations):
			firstAnswer=int(inFile.readline())
			firstCards=[]
			for j in range(0,4):
				row=inFile.readline().strip().split(" ")
				firstCards.append(row)
			secondAnswer=int(inFile.readline())
			secondCards=[]
			for j in range(0,4):
				row=inFile.readline().strip().split(" ")
				secondCards.append(row)
			cases.append([firstAnswer,firstCards,secondAnswer,secondCards])
	return cases,numIterations

def answer(parsedData,testcases):
	for i in range(0,testcases):
		firstAnswer=parsedData[i][0]
		firstRow=set(parsedData[i][1][firstAnswer-1])
		secondAnswer=parsedData[i][2]
		secondRow=set(parsedData[i][3][secondAnswer-1])
		answer = firstRow.intersection(secondRow)
		res="Case #"+str(i+1)+": "
		if len(answer)==1:
			res+=str(answer.pop())
		elif len(answer)==0:
			res+="Volunteer cheated!"
		else:
			res+="Bad magician!"
		print(res)
		
data,numTestcases = parser(os.sys.argv[1])
answer(data,numTestcases)