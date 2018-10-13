f = open('test.txt', 'r')

f.readline()
caseN=1
for line in f:
	total = int(line)
	cakes = f.next()
	cakes = cakes.split()
	cakes = [int(x) for x in cakes]
	bestans = max(cakes)
	mins = 2
	while mins < bestans:
		switch = sum([(x - 1) // mins for x in cakes]) + mins 
		bestans = min(bestans, switch)
		mins += 1
	print "Case #%d: %d" % (caseN, bestans)
	caseN += 1

		

