with open('p1.in') as f:
	lines = [line.strip() for line in f.readlines()]

testcases = int(lines.pop(0))


for testcase in xrange(1, testcases + 1):

	sug1 = int(lines.pop(0))

	for i in xrange(sug1 - 1):
		lines.pop(0)

	chosen1 = lines.pop(0)

	for i in xrange(4 - sug1):
		lines.pop(0)

	sug2 = int(lines.pop(0))

	for i in xrange(sug2 - 1):
		lines.pop(0)

	chosen2 = lines.pop(0)

	for i in xrange(4 - sug2):
		lines.pop(0)

	#print sug1, "k", chosen1, "k", sug2, "k", chosen2 

	set1 = set(chosen1.split())
	set2 = set(chosen2.split())

	inte = set1 & set2

	if len(inte) == 1:
		print "Case #%d: %s" % (testcase, inte.pop())
	elif len(inte):
		print "Case #%d: Bad magician!" % (testcase)
	else:
		print "Case #%d: Volunteer cheated!" % (testcase)