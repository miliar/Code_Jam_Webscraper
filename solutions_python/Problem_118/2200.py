R=5000
fas=set()
for i in xrange(R):
	if str(i)==(str(i)[::-1]):
		sq = i**2
		if sq < 10000001 and str(sq)==(str(sq)[::-1]):
			fas.add(sq)
			sq1 = sq**2
			if sq1 < 1000001 and str(sq1)==(str(sq1)[::-1]):
				fas.add(sq1)
				sq2 = sq1**2
				if sq2 < 1000001 and str(sq2)==(str(sq2)[::-1]):
					fas.add(sq2)
					sq3 = sq2**2
					if sq3 < 1000001 and str(sq3)==(str(sq3)[::-1]):
						fas.add(sq3)
T=int(raw_input())
for i in xrange(T):
	l=raw_input().split()
	a=int(l[0])
	b=int(l[1])
	count = 0
	for j in fas:
		if a <= j and j <= b:
			count=count+1
	print "Case #"+str(i+1)+": "+str(count)


