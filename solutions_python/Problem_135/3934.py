T = int(input())

for t in xrange(1,T+1): 
	r1 = int(input())
	store1 = None
	for i in xrange(1,5):
		if i == r1:
			store1 = map(int,raw_input().split(' '))
		else:
			raw_input()

	r2 = int(input())
	store2 = None
	for i in xrange(1,5):
		if i == r2:
			store2 = map(int,raw_input().split(' '))
		else:
			raw_input()

	match = list()

	for e in store1:
		if e in store2:
			match.append(e)

	if len(match) == 1:
		print "Case #%d: %d" % (t,match[0])
	elif len(match) > 1:
		print "Case #%d: %s" % (t,"Bad magician!")
	elif len(match) == 0:
		print "Case #%d: %s" % (t,"Volunteer cheated!")
