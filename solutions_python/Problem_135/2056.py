t = int(raw_input())

for qq in xrange(1, t + 1):
	r = int(raw_input())
	for i in xrange(1, 5):
		row = raw_input().split()
		if i == r: row1 = set(row)
	r = int(raw_input())
	for i in xrange(1, 5):
		row = raw_input().split()
		if i == r: row2 = set(row)
	inter = list(set.intersection(row1, row2))
	if len(inter) == 1:
		print "Case #{0}: {1}".format(qq, inter[0])
	elif len(inter) > 1:
		print "Case #{0}: {1}".format(qq, "Bad magician!")
	else:
		print "Case #{0}: {1}".format(qq, "Volunteer cheated!")

