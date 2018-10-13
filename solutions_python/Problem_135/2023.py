testCases = int(raw_input())

for t in range(1, testCases + 1):

	row1 = int(raw_input())
	# print "row1", row1,
	for i in xrange(1, 5):
		# print "i" , i
		if i == row1:
			set1 = set(map(int, raw_input().split(" ")))
			# print set1
		else:
			raw_input()

	row2 = int(raw_input())
	# print "row2", row2,
	for i in xrange(1, 5):
		if i == row2:
			set2 = set(map(int, raw_input().split(" ")))
			# print set2
		else:
			raw_input()

	ans = set1.intersection(set2)
	# print "ans", ans
	print "Case #%d: " % t,

	if len(ans) == 1:
		print ans.pop()
	elif len(ans) == 0:
		print "Volunteer cheated!"
	else:
		print "Bad magician!"

	# print 