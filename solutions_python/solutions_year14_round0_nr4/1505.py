t = int(raw_input())
for i in range(1,t+1):
	print "Case #%d:" %i,
	n =	int(raw_input())
	naomi = raw_input().split()
	ken = raw_input().split()
	naomi = sorted([float(x) for x in naomi])
	ken = sorted([float(x) for x in ken])
	l1,l2,r1,r2,legal,illegal = n-1,n-1,n-1,n-1,0,0
	for i in range(n):
		if ken[l1]<naomi[l2]:
			l2 -= 1
			illegal += 1
		if ken[r1]>naomi[r2]:
			r1 -= 1
		else:
			legal += 1
		l1 -= 1
		r2 -= 1
	print illegal,legal