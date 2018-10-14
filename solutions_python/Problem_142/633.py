#MAM, Google Code Jam - Round 1B, Problem A

infile = open("A-small-attempt0.in", "r")
outfile = open("output.txt", "w")

numtests = int(infile.readline())

for T in range(numtests):

	outfile.write("Case #"+str(T+1)+": ")

	#Input

	N = int(infile.readline())
	strings=list()
	for x in xrange(N):
		strings.append(str(infile.readline().rstrip()))

	#Calculations

	stringdict=list()

	for x in xrange(N):

		stringdict.append(list())
		prevchar = ''
		repcount = 0

		for c in strings[x]:

			repcount+=1

			#if not same as before, input into dictionary, reset to 0
			if c != prevchar:
				if prevchar != '':
					stringdict[x].append((prevchar, repcount))
				repcount = 0
				prevchar=c

		stringdict[x].append((prevchar, repcount+1))


	#####find out if the characters are the same####

	SameChars = True

	#if lengths of any dictionaries different, break
	for everyotherstringdict in stringdict[1:]:
		if len(everyotherstringdict) != len(stringdict[0]):
			SameChars=False
			break

	#Harder test; if char order is different or different chars altogether, break
	for x in xrange(len(stringdict[0])):
		if SameChars==False: 
			break

		currchar = stringdict[0][x][0]
		#print currchar
		for everyotherstringdict in stringdict[1:]:

			#print everyotherstringdict[x][0]
			if everyotherstringdict[x][0] != stringdict[0][x][0]:
				SameChars=False
				break

	#####Now that we have established characters are the same, find the minimum difference;######
	#find stepsneeded by picking closest to the mean and subtracting

	if SameChars:
		stepsneeded = 0
		#naive solution for N=2; replace with mean as noted above
		for x in xrange(len(stringdict[0])):
			stepsneeded += abs(stringdict[0][x][1]-stringdict[1][x][1])

	#Output
		outfile.write(str(stepsneeded))

	else:
		outfile.write("Fegla Won")

	outfile.write("\n")