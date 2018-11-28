inFile = "B-large.in"

openFile = open(inFile)
openFile.readline()

testCases = []
baseElements = ["Q", "W", "E", "R", "A", "S", "D", "F"]
results = []

for line in openFile:
	print
	values = line.split()
	print "RAW VALUES: ",
	print values

	counter = 0
	combos = {}

	C = int(values[counter])
	counter += 1

	for i in range(0,C):
		combos[values[counter][0]+values[counter][1]] = values[counter][2]
		combos[values[counter][1]+values[counter][0]] = values[counter][2]
		counter += 1

	print str(C) + " COMBO(S): ",
	print combos

	D = int(values[counter])
	counter += 1

	opposition = {}
	
	for i in range(0,D):
		try:
			opposition[values[counter][0]]
		except:
			opposition[values[counter][0]] = []
		try:
			opposition[values[counter][1]]
		except:
			opposition[values[counter][1]] = []

		opposition[values[counter][0]].append(values[counter][1])
		opposition[values[counter][1]].append(values[counter][0])
		counter += 1

	testString = values[counter+1]

	print str(D) + " OPPOSITION(S): ",
	print opposition
	print "TEST STRING: " + testString

	testCases.append({"combos":combos, "opposition":opposition,"testString":testString})

openFile.close()

for case in testCases:

	print

	elementList = []
	print case["testString"]
	print case["combos"]
	print case["opposition"]

	for element in case["testString"]:
		print "NEXT ELEMENT: " + element

		append = True

		if len(elementList) == 0:
			elementList.append(element)

		else:
			try:
				print element+elementList[-1] + " is a combo producing " + case["combos"][element+elementList[-1]]
				element = case["combos"][element+elementList[-1]]
				del elementList[-1]
			except KeyError:
				print element+elementList[-1] + " is not a combo."

			for opElement in elementList:

				try:
					if opElement in case["opposition"][element]:
						print element+" and " +elementList[-1] + " are opposed"
						elementList = []
						element=""
						append = False
				except:
					try:
						print element+" and " +elementList[-1] + " are not opposed"
					except:
						None

			if append:
				elementList.append(element)
			append = True

	print elementList
	result = "["

	for e in elementList:
		result = result + e+", "
	result = result.rstrip(", ")+"]"
	print "RESULT: " + result
	results.append(result)

outPath = "output.txt"

outFile = open(outPath, "w")
for i in range(0,len(results)):
	outFile.write("Case #"+str(i+1)+": "+results[i]+"\n")

outFile.close()



		
		

	

		
	
