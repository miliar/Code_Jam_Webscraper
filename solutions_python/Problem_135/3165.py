test_cases = int(raw_input())
for test in xrange(test_cases):
	row1 = int(raw_input()) - 1
	grid1 = [raw_input().split() for x in xrange(4)]
	row2 = int(raw_input()) - 1
	grid2 = [raw_input().split() for x in xrange(4)]
	evidence = len(set(grid1[row1] + grid2[row2]))
	if evidence == 7:
		x = [x for x in grid1[row1] if x in grid2[row2]]
		print 'Case #%d: %s' %((test+1),x[0])
	elif evidence < 7:
		print 'Case #%d: Bad magician!' %(test+1)
	else:
		print 'Case #%d: Volunteer cheated!' %(test+1)

