t = int (raw_input())
for ti in xrange(t):
	d, n = (map(int,raw_input().split()))
	max_val = 0.0
	for i in xrange(n):
		ki , si = map(int, raw_input().split())
		time = (d-ki)*1.0/si
		if (time>max_val):
			max_val = time
	print "Case #"+str(ti+1)+": "+str(d*1.0/max_val)