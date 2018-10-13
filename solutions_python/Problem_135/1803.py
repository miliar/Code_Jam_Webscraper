case_num = int(raw_input())
for i in xrange(1, case_num+1):
	print 'Case #%d:'%i,
	x1, x2, x3, x4, y1, y2, y3, y4 = (0,0,0,0,0,0,0,0)
	row1 = int(raw_input())
	for j in range(1,5):
		#print "row 1 round...", j
		if row1 == j:
			x1, x2, x3, x4 = raw_input().split()
		else:
			raw_input()
	row2 = int(raw_input())
	for j in range(1,5):
		#print "row 2 round...", j
		if row2 == j:
			y1, y2, y3, y4 = raw_input().split()
		else:
			raw_input()
	count = 0
	selected = 0
	if x1 in (y1, y2, y3, y4):
		selected = x1
		count += 1
	if x2 in (y1, y2, y3, y4):
		selected = x2
		count += 1
	if x3 in (y1, y2, y3, y4):
		selected = x3
		count += 1
	if x4 in (y1, y2, y3, y4):
		selected = x4
		count += 1
	if count == 0:
		print 'Volunteer cheated!'
	elif count > 1:
		print 'Bad magician!'
	else:
		print selected