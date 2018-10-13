f = open("A-small-attempt0.in","r")
numberOfCases = f.readline()

fw = open("data1-output.txt","w")
for i in range(int(numberOfCases)):
	choice = int(f.readline())
	for k in range(4):
		if int(choice)==k+1:
			set1 = set(f.readline()[:-1].split(' '))
		else:
			f.readline().split(' ')

	choice = int(f.readline())
	for k in range(4):
		if int(choice)==k+1:
			set2 = set(f.readline()[:-1].split(' '))
		else:
			f.readline().split(' ')

	result = list(set1.intersection(set2))
	if result:
		if len(result) == 1:
			fw.write("Case #"+str(i+1)+": "+result[0]+"\n")
		else :
			fw.write("Case #"+str(i+1)+": Bad magician!"+"\n")
	else:
		fw.write("Case #"+str(i+1)+": Volunteer cheated!"+"\n")
fw.close()