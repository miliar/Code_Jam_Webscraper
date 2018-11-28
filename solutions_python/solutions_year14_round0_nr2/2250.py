file_in = open('C:\\Users\\ichung\\Downloads\\code\\B-large.in','r')
numSets = int(file_in.readline())
# print numSets
for i in xrange(1,numSets+1) :
	firstRow = file_in.readline()
	firstRow = firstRow[:-1]
	firstRowSeparated = firstRow.split()
	c = float(firstRowSeparated[0])
	f = float(firstRowSeparated[1])
	x = float(firstRowSeparated[2])
	# print str(c) + " " + str(f) + " " + str(x)
	contLoop = 1
	counter = 0
	totalSum = 0.0
	while(contLoop == 1) :
		nextCount = counter+1
		# print x/(2+(counter*f))
		# print (c/(2+(counter*f)) + x/(2+(nextCount*f)))
		if(x/(2+(counter*f)) < (c/(2+(counter*f)) + x/(2+(nextCount*f)))) :
			totalSum = totalSum + x/(2+(counter*f))
			contLoop = 0
		else :
			totalSum = totalSum + c/(2+(counter*f))
		counter = counter + 1

		# if counter > 100000 :
		# 	contLoop = 0

	print "Case #" + str(i) + ": " + str(totalSum)
