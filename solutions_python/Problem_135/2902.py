for k in xrange(int(raw_input())):
	first = int(raw_input())
	first_possibilities = set([row for index, row in enumerate(([int(token) for token in raw_input().split()] for i in xrange(4))) if index == first - 1][0])
	second = int(raw_input())
	second_possibilities = set([row for index, row in enumerate(([int(token) for token in raw_input().split()] for i in xrange(4))) if index == second - 1][0])
	matches = first_possibilities.intersection(second_possibilities)
	if len(matches) == 1:
		print "Case #%d: %s" % (k + 1, matches.pop())
	elif len(matches) > 1:
		print "Case #%d: %s" % (k + 1, "Bad magician!")
	else:
		print "Case #%d: %s" % (k + 1, "Volunteer cheated!")