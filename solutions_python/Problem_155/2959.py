def resolveCase(line):
	elements = line.split()
	n = int(elements[0])
	data = elements[1]

	i = 0
	nFriends = 0
	nAudience = 0
	for d in data:
		if (i > nAudience):
			friendsToAdd = (i - nAudience)
			nFriends += friendsToAdd
			nAudience += friendsToAdd

		nAudience += int(d)
		i = i+1

	return nFriends

f = open('A-large.in', 'r');
nCases = int(f.readline())
for x in xrange(0,nCases):
	line = f.readline()
	result = resolveCase(line)
	print "Case #{}: {}".format(x+1, result)