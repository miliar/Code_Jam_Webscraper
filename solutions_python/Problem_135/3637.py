test_num = int(raw_input().strip())
for i in xrange(test_num):
	cards1 = []
	cards2 = []
	row_chosen1 = int(raw_input().strip())
	for j in xrange(4):
		cards1.append([int(elem)  for elem in raw_input().strip().split()])
	row_chosen2 = int(raw_input().strip())
	for j in xrange(4):
		cards2.append([int(elem)  for elem in raw_input().strip().split()])
	#print row_chosen1, row_chosen2
	#print cards1
	#print cards2
	cards = set(cards1[row_chosen1-1]) & set(cards2[row_chosen2-1])
	common_no = len(cards)
	if (common_no == 0):
		print 'Case #%d: Volunteer cheated!' % (i+1)	 
	elif (common_no == 1):
		print 'Case #%d: %d' % (i+1,cards.pop())
	elif (common_no > 1):
		print 'Case #%d: Bad magician!' % (i+1)	