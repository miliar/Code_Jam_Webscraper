t = int(raw_input())

for i in xrange(t):
	a,b,k = map(int,raw_input().split())
	count = 0
	for j in xrange(a):
		for l in xrange(b):
			if j & l < k:
				count += 1
	
	print "Case #" + str(i+1) + ": " + str(count)

