tests = input()
answers = []
for a in range(tests):
	firstAnswer = input()
	firstRowS = raw_input().split()
	secondRowS = raw_input().split()
	thirdRowS = raw_input().split()
	fourthRowS = raw_input().split()
	countableRow= []
	for c in range(len(firstRowS)):
		if firstAnswer == 1:
			countableRow.append(int(firstRowS[c]))
		if firstAnswer == 2:
			countableRow.append(int(secondRowS[c]))
		if firstAnswer == 3:
			countableRow.append(int(thirdRowS[c]))
		if firstAnswer == 4:
			countableRow.append(int(fourthRowS[c]))
	secondAnswer = input()
	firstRowS = raw_input().split()
	secondRowS = raw_input().split()
	thirdRowS = raw_input().split()
	fourthRowS = raw_input().split()
	countableRow2= []
	for b in range(len(firstRowS)):
		if secondAnswer == 1:
			countableRow2.append(int(firstRowS[b]))
		if secondAnswer == 2:
			countableRow2.append(int(secondRowS[b]))
		if secondAnswer == 3:
			countableRow2.append(int(thirdRowS[b]))
		if secondAnswer == 4:
			countableRow2.append(int(fourthRowS[b]))
	results = []
	for c in countableRow:
		if c in countableRow2:
			results.append(c)
	if len(results) == 0:
		answers.append("Case #"+str(a+1)+": "+"Volunteer cheated!") 
	elif len(results) == 1:
		answers.append("Case #"+str(a+1)+": "+str(results[0]))
	else:
		answers.append("Case #"+str(a+1)+": "+"Bad magician!")

for d in answers:
	print d
