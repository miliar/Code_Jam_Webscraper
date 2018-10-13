import sys

F = open('A-small-attempt0.in')

cases = int(F.readline())

for case in xrange(cases):
	candidates = None
	
	lineno = int(F.readline())
	for i in range(4):
		line = F.readline()
		if i == lineno - 1:
			candidates = set(int(card) for card in line.split())
	
	lineno = int(F.readline())
	for i in range(4):
		line = F.readline()
		if i == lineno - 1:
			candidates.intersection_update(int(card) for card in line.split())

	if len(candidates) == 0:
		print "Case #%d: Volunteer cheated!" % (case + 1)
	elif len(candidates) == 1:
		print "Case #%d: %d" % (case + 1, candidates.pop())
	else:
		print "Case #%d: Bad magician!" % (case + 1)
	

	