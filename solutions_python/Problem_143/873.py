t = int(raw_input())
for q in xrange(t):
	a,b,k = [int(i) for i in raw_input().split()]
	co = 0
	for i in xrange(a):
		for j in xrange(b):
			if i&j < k:
				co += 1
	print "Case #%s: %s"%(q+1,co)
	