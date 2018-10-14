caseCount = int(raw_input())

for case in xrange(caseCount):
	firstAnswer = int(raw_input())
	options = []
	for l in xrange(1,5):
		line = raw_input()
		if l == firstAnswer:
			options = map(int, line.split(" "))
	secondAnswer = int(raw_input())
	matches = 0
	match = 0
	for l in xrange(1,5):
		line = raw_input()
		if l == secondAnswer:
			second = map(int, line.split(" "))
			for x in options:
				if x in second:
					matches += 1
					match = x
	if matches == 0:
		print "Case #%d: Volunteer cheated!" % (case+1)
	elif matches == 1:
		print "Case #%d: %d" % (case+1, match)
	else:
		print "Case #%d: Bad magician!" % (case+1)
