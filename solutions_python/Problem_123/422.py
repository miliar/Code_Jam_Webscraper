import sys,logging

#logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

inputFile = open(sys.argv[1])
outFile   = open("outFile.txt", "w")
for i in range(int(inputFile.readline())):
	moteSize = int(inputFile.readline().strip().split()[0])
	motes    = sorted(map(int, inputFile.readline().split()))



	counter = 0
	done    = False

	costToDelete = 0
	while not done:
		if len(motes) == 0:
			if costToDelete < counter and costToDelete != 0:
				counter = costToDelete
			done = True
			continue

		if moteSize == 1:
			counter = len(motes)
			done = True
			continue
		
		if moteSize > motes[0]:
			moteSize += motes[0]
			motes.pop(0)
			continue

		elif (moteSize + moteSize - 1) <= motes[0]:
			if costToDelete == 0:
				costToDelete = len(motes) + counter
		
		motes.append(moteSize - 1)
		motes = sorted(motes)
		counter += 1


	outFile.write("Case #" + str(i+1) + ": " + str(counter) + "\n")
	print("Case #" + str(i+1) + ": " + str(counter))

