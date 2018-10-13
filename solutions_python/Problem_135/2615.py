i = int(raw_input())

for z in xrange(i):
	a1 = int(raw_input()) - 1
	field1 = []
	for m in xrange(4):
		field1.append(set(map(int, raw_input().split(" "))))
	
	a2 = int(raw_input()) - 1
	field2 = []
	for m in xrange(4):
		field2.append(set(map(int, raw_input().split(" "))))
		
	f = field1[a1] & field2[a2]
	if len(f) > 1: print "Case #%d: Bad magician!" % (z+1,)
	elif len(f) == 0: print "Case #%d: Volunteer cheated!" % (z+1,)
	else: print "Case #%d: %d" % (z+1, f.pop())

