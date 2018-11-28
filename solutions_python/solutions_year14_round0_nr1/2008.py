T = input()
for t in xrange(T):
	m = t+1
	n1 = input()
	board1 = [[int(_) for _ in raw_input().split()] for i in xrange(4)]
	n2 = input()
	board2 = [[int(_) for _ in raw_input().split()] for i in xrange(4)]
	row1 = board1[n1-1]
	row2 = board2[n2-1]
	set = None
	for i in row1:
		for j in row2:
			if i == j:
				if set is None:
					set = i
				else:
					set = False
	if set is None:
		print "Case #%d:" % m, "Volunteer cheated!"
	elif set is False:
		print "Case #%d:" % m, "Bad magician!"
	else:
		print "Case #%d:" % m, set
