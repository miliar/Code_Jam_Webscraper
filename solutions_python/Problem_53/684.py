from sys import stdin

T = int(stdin.readline())

for _t in xrange(T):
	N, K = map(int, stdin.readline().split(" "))

	mask = ((1<<N)-1)
	res = K&mask==mask
	
	print "Case #%d: %s" % (_t+1, "ON" if res else "OFF")