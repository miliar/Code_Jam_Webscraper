fo = open("A-small-attempt1.in","r+")
fw = open("output.txt","w")
def ToInt(str):
	return int(str.strip())


count = ToInt(fo.readline())

for i in range(1,count+1):
	answerList = []
	firstAnswer = ToInt(fo.readline())
	for j in range(1,5):
		
		if firstAnswer == j:
			firstArrange = [int(l) for l in fo.readline().strip().split()]
		else:
			fo.readline()

	secondAnswer = ToInt(fo.readline())
	secondArrange = []
	for j in range(1,5):
		if secondAnswer == j:
			secondArrange = [int(l) for l in fo.readline().strip().split()]
		else:
			fo.readline()

	for k in range(0,4):
		try:
			if secondArrange.index(firstArrange[k]) != -1 :
				answerList.append(firstArrange[k])
		except ValueError:
			pass

	if len(answerList) == 1 :
		fw.write("Case #{0}: {1}\n".format(i, answerList[0])) 
	elif len(answerList) == 0:
		fw.write("Case #{0}: Volunteer cheated!\n".format(i))
	elif len(answerList) > 1:
		fw.write("Case #{0}: Bad magician!\n".format(i))