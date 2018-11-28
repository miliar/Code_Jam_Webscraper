











for case in xrange(input()):
	row = input()
	for r in xrange(4):
		if r+1 == row:
			first_row = set(raw_input().split(" "))
		else:
			raw_input()

	row = input()
	for r in xrange(4):
		if r+1 == row:
			second_row = set(raw_input().split(" "))
		else:
			raw_input()

	intersect = first_row & second_row
	if len(intersect) == 0:
		print "Case #%d: Volunteer cheated!" % (case+1)
	elif len(intersect) == 1:
		print "Case #%d: %s" % (case+1, intersect.pop())
	else:
		print "Case #%d: Bad magician!" % (case+1)
