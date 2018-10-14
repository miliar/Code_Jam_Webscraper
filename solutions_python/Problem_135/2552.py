import sys

fileRead = open(sys.argv[1]).readlines()
cardPack1 = []
cardPack2 = []
count = 0
output = 0
flag = 0

numberOfTestCases = int(fileRead[0].replace("\n",""))

for i in range(1,len(fileRead),5):
	flag += 1
	rowNumber = int(fileRead[i].replace("\n",""))
	if flag%2 == 0:
		cardPack2.append([int(x) for x in fileRead[i+rowNumber].replace("\n","").split(" ")])
	else:
		cardPack1.append([int(x) for x in fileRead[i+rowNumber].replace("\n","").split(" ")])

for i in range(numberOfTestCases):
	count = 0
	for j in cardPack1[i]:
		if j in cardPack2[i]:
			count += 1
			output = j
	
	if count == 1:
		print "Case #" + str(i+1) + ": " + str(output)
	elif count == 0:
		print "Case #" + str(i+1) + ": Volunteer cheated!"
	else:
		print "Case #" + str(i+1) + ": Bad magician!"



	
