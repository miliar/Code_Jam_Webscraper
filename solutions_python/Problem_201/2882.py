
def main():
	testcases = int(input())
	for i in range(testcases):
		line = input().split()
		k = int(line[1])
		stallAmount = int(line[0])
		stall = [stallAmount]
		terminal = False
		u = 0
		while u < k:
			if u == k-1:
				terminal = True
			stall = addPerson(stall, terminal)
			u+= 1

		print("Case #", i+1,": ", stall[0], " ", stall[1], sep ="")

def addPerson(stall,term):
	if len(stall) == 1:
		if term:
			if stall[0]%2 == 0:
				return [int(stall[0]/2),int(stall[0]/2)-1]
			else:
				return [int(stall[0]/2),int(stall[0]/2)]
		return [int(((stall[0]-1)/2)), int(stall[0]/2)]

	maxSpace = 0
	bestSpot = 0
	for i in range(len(stall)):
		freeStalls = stall[i]
		if freeStalls > maxSpace:
			maxSpace = freeStalls
			bestSpot = i

	splitResult = addPerson([maxSpace],term)
	if term:
		return splitResult
	stall[bestSpot] = splitResult[0]
	stall.insert(bestSpot+1,splitResult[1])
	#print(stall)
	return stall


main()


