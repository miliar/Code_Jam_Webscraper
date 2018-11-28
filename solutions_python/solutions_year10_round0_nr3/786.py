import sys

if len(sys.argv) < 2:
	quit('More args')

# read the file
lines = [line.strip() for line in file(sys.argv[1])]
cases = int(lines[0])
for i in range(1, cases + 1):
	numRides, capacity, numGroups = lines[(i * 2) - 1].split()
	groups = lines[i * 2].split()

	# loop through the number of rides
	amount = 0
	groupIndex = 0
	for rides in range(0, int(numRides)):
		# add the number of people in each group
		numPeople = 0
		startIndex = groupIndex
		while numPeople + int(groups[groupIndex]) <= int(capacity):
			numPeople += int(groups[groupIndex])
			groupIndex += 1
			if groupIndex >= int(numGroups):
				groupIndex = 0
			if groupIndex == startIndex:
				break
				
		amount += numPeople
	print "Case #%s: %s" % (i, amount)
