cases = int(input())
counts = [0]*cases

for x in range(cases):
	temp = str(input())
	temp = temp.split()
	maxShyness = int(temp[0])
	tempVals = [[0 for m in range(2)] for m in range(maxShyness+1)]
	shyNessVals = list(temp[1])
	shyNessVals = [int(y) for y in shyNessVals]

	for n in range(len(shyNessVals)):
		tempVals[n] = [shyNessVals[n], n]
	claps = tempVals[0][0]
	peopleReq = 0
	#print(tempVals)
	for z in range(1, len(tempVals)):
		if(claps < tempVals[z][1] and tempVals[z][0] != 0):
			#print(claps)
			clapsThatWereRequired = tempVals[z][1]
			peopleReq += (clapsThatWereRequired - claps)
			claps += tempVals[z][0]
			claps += peopleReq

		elif(claps >= tempVals[z][1]):
			claps += tempVals[z][0]


	counts[x] = peopleReq

for l in range(len(counts)):
	print('Case #'+str(l+1)+': '+str(counts[l]))
