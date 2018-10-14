tc = int(raw_input())
cou = 0

while (tc>0):

	l1 = []
	l2 = []
	
	tc = tc - 1
	cou = cou + 1
	
	ans1 = int(raw_input())
	for i in xrange(4):
		a = map(int, raw_input().split())
		l1.append(a)
	
	ans2 = int(raw_input())
	for i in xrange(4):
		b = map(int, raw_input().split())
		l2.append(b)

	ti, ans = 0, 0
	for i in l1[ans1-1]:
		for j in l2[ans2-1]:
#			print i, j, "......"
			if (i==j):
#				print i, j, "#########"
				ans = i
				ti = ti + 1
	
#	print ti

	if (ti==0):
		print 'Case #%d: Volunteer cheated!' % (cou)
	elif (ti>1):
		print 'Case #%d: Bad magician!' % (cou)
	else:
		print "Case #%d: %d" % (cou, ans)




