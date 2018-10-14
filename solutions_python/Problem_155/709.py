import sys	

T = int(sys.stdin.readline())
for i in xrange(T):
	(SM,S),clapping,extra = sys.stdin.readline().split(),0,0
	for j,num in enumerate(map(int,S)):
		if num > 0 and (clapping + extra) < j:
			extra += j - clapping - extra
		clapping += num
	print "Case #%s: %s"%(i+1,extra)