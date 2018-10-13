file = file("ovation.in", "r")
nCases = int(file.readline())

for i in xrange(0, nCases):
	data = []
	current = 0
	added = 0
	case = file.readline().split()
	for j in xrange(0, int(case[0])+1):
		if (case[1][j] != 0 and current < j):
				added = added + (j - current)
				current = j
		current = current + int(case[1][j])
		# print "at", j, "with", current, "people"
	print "Case #"+str(i+1)+": "+str(added)

