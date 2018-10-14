
def computeAmount(numRounds, capacity, groups, numGroups):
	rnd = 1
	numPeople = 0
	amount = 0
	grps = 0
	while rnd < numRounds+1:
	#	print numPeople, ':', groups
		if (numPeople + groups[0] > capacity) or (grps == numGroups):
			rnd += 1
			amount += numPeople
			numPeople = grps = 0
		else:
			numPeople += groups[0]
			groups.append(groups.pop(0))
			grps += 1
	return amount

if __name__ == '__main__':
	numTestcases = input()
	for testcase in range(numTestcases):
		numRounds, capacity, numGroups = map(int, raw_input().split())
		groups = map(int, raw_input().split())
		print 'Case #' + str(testcase+1) + ':', computeAmount(numRounds, capacity, groups, numGroups)
