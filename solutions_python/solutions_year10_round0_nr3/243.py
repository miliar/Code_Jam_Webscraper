#!/usr/bin/python
import sys
testIn = open(sys.argv[1], "r")
testOut = open(sys.argv[2], "w")

nbTests = int(testIn.readline())

for nbTest in range(1, nbTests+1):
	line1 = testIn.readline().split(" ")
	nbTours = int(line1[0])
	nbPlaces = int(line1[1])
	nbGroupes = int(line1[2])

	groupes = testIn.readline().split(" ")

	for i in range(nbGroupes):
		groupes[i] = int(groupes[i])

	fric = 0
	for tour in range(nbTours):
		groupesPasses = []

		placesRestantes = nbPlaces
		while len(groupes) > 0 and groupes[0] <= placesRestantes:
			placesRestantes -= groupes[0]
			fric += groupes[0]
			groupesPasses.append(groupes[0])
			groupes = groupes[1:]
		groupes += groupesPasses

	outLine = "Case #"+str(nbTest)+": "+str(fric)
	
	testOut.write(outLine+"\n")
	print outLine

testIn.close()
testOut.close()
