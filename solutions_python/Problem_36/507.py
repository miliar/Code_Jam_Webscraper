#! /usr/bin/python

baseString = "welcome to code jam"

def recurse(baseStringIndex, haystackString):
	if baseStringIndex == len(baseString):
		return 1
	if len(haystackString) == 0:
		return 0
	localCount = 0
	localIndex = -1
	while True:
		localIndex = haystackString.find(baseString[baseStringIndex],localIndex+1)
		if len(haystackString) <= 1:
			return 0
		if localIndex < 0:
			break
		else:
			localCount += recurse(baseStringIndex+1,haystackString[localIndex+1:])
	return localCount


filename = raw_input("Enter the file name: ")
inputFile = open(filename)

count = int(inputFile.next())
for lineNumber in range(1,count+1):
	try:
		line = inputFile.next()
	except StopIteration:
		print "File ended abrubtly..."
		inputFile.close()
		exit(1)
	numba = "%04d" % (recurse(0,line))
	print "Case #%s: %s" % (lineNumber, numba[-4:])


inputFile.close()
exit(0)