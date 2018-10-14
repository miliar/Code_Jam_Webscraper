a = int(raw_input())
for i in range(a):
	r1 = int(raw_input())
	l1 = []
	for j in range(4):
		l1.append(raw_input())
	r2 = int(raw_input())
	l2 = []
	for j in range(4):
		l2.append(raw_input())
	l3 = l1[r1-1].split()
	l4 = l2[r2-1].split()
	l5 = list(set(l3).intersection(l4))
	if len(l5) == 1:
		print "Case #%d: %s" % (i+1, l5[0])
	elif len(l5) > 1:
		print "Case #%d: Bad magician!" % (i+1)
	else:
		print "Case #%d: Volunteer cheated!" % (i+1)