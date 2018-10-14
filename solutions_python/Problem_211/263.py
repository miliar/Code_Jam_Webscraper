import math 

t = input()
for case in xrange(1,t+1):
	ac, aj = map(int, raw_input().split())
	c = [[]*ac];d = [[]* ac]
	for x in xrange(ac):
		c[x], d[x] = map(int, raw_input().split())
	j = [[]*aj] ; k = [[]*aj]
	for x in xrange(aj):
		j[x], k[x] = map(int, raw_input().split())
		
	print "Case #%d: %d %d"%(case, max(t1, t2), min(t1, t2))
























