fin = open("ex.in")

cases = []

def listNums():
	return map(int, fin.readline().split(' '))

def parseFile():
	numCases = int(fin.readline())
	for i in range(0,numCases):
		cases.append({"row1":[], "row2":[]})

		#arrangement 1
		row = int(fin.readline())
		#Skip rows maybe
		for j in range(1,row):
			fin.readline()
		cases[i]["row1"] = listNums()
		#skip more rows maybe, get to second arrangement
		for j in range(0,4-row):
			fin.readline()

		#arrangement 2
		row = int(fin.readline())
		#Skip rows maybe
		for j in range(1,row):
			fin.readline()
		cases[i]["row2"] = listNums()
		#skip more rows maybe, get to second arrangement
		for j in range(0,4-row):
			fin.readline()

def output():
	fout = open("ex.out","w")
	caseNum = 0
	for case in cases:
		caseNum += 1
		#any numbers the same in the different rows
		count = 0
		lastNum = 0
		for num in case["row1"]:
			if num in case['row2']:
				count += 1
				lastNum = num
		if count > 1:
			fout.write("Case #"+str(caseNum)+": Bad magician!\n")
		elif count == 0:
			fout.write("Case #"+str(caseNum)+": Volunteer cheated!\n")
		else:
			fout.write("Case #"+str(caseNum)+": "+str(lastNum)+"\n")

def main():
	parseFile()
	output()


main()