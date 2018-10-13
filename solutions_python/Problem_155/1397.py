from sys import stdin

cases = int(stdin.readline())

for case in xrange(cases):
	line = stdin.readline().split(' ')
	shyest = line[0]
	shyarray = line[1]

	total = 0
	addedpeople = 0
	for shyness, people in enumerate(shyarray):
		if (not people.isdigit()):
			break
		if (total >= shyest):
			break
		if (total < shyness):
			addedpeople += shyness-total
			total += shyness-total
		total += int(people)
	print "Case #%d: %d" % (case+1, addedpeople)

