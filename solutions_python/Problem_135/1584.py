N = int(raw_input())

for case in xrange(N):
	l1 = int(raw_input())
	
	cards1 = []
	for l in xrange(4):
		newrow = map(int, raw_input().strip().split())
		cards1.append(newrow)
	l2 = int(raw_input())
	
	gr1 = cards1[l1-1]
	
	cards2 = []
	for l in xrange(4):
		newrow = map(int, raw_input().strip().split())
		cards2.append(newrow)
	
	gr2 = cards2[l2-1]
	
	#print 'expect card here',gr1,gr2
	
	cardrep = {}
	
	for c in gr1:
		if c in gr2: cardrep[c] = 1
		
	#print cardrep
	if len(cardrep) == 1:
		print 'Case #'+str(case+1)+':',cardrep.keys()[0]
	elif len(cardrep) > 1:
		print 'Case #'+str(case+1)+': Bad magician!'
	else:
		print 'Case #'+str(case+1)+': Volunteer cheated!'
	