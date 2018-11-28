doc = open("A-small-attempt1.in", "r")
a = doc.readline()
a = int(a[0:-1])
for case in range(a):
	#print "##############"
	result = "Case #" + str(case+1) + ": "
	firstNum = int(doc.readline()[0:-1])
	#print firstNum
	readthrough = 0
	for i in range(firstNum-1):
		doc.readline()
		readthrough+=1
	line = doc.readline()
	#print line
	options = []
	char = " "
	current = ""
	for j in range(len(line)):
		if line[j] == " ":
			options.append(int(current))
			current = ""
		else:
			current += line[j]
	options.append(int(current))
	#print options
	for x in range(4-readthrough-1):
			 doc.readline()
	secondNum = int(doc.readline()[0:-1])
	#print secondNum
	readthrough = 0
	for i in range(secondNum-1):
		doc.readline()
		readthrough+=1
	line = doc.readline()
	#print line
	options2 = []
	char = " "
	current = ""
	for j in range(len(line)):
		if line[j] == " ":
			options2.append(int(current))
			current = ""
		else:
			current += line[j]
	options2.append(int(current))
	#print options2
	numOfReppeats = 0
	for num in options:
		if num in options2:
			numOfReppeats+=1
			final = num
	if numOfReppeats == 0:
		result +="Volunteer cheated!"
	elif numOfReppeats > 1:
		result +="Bad magician!"
	else:
		result+=str(final)
	print result
	for x in range(4-readthrough-1):

			doc.readline()
		
		


