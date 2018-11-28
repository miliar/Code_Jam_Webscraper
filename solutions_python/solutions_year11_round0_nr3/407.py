import sys
ccN = int(sys.stdin.readline())
for cc in range(ccN):
	n = sys.stdin.readline()
	candy = sorted(map(int, sys.stdin.readline().split()))
	if reduce(lambda x, y : x ^ y, candy) == 0:
		print "Case #%d: %d" % (cc + 1, sum(candy) - candy[0])
	else:
		print "Case #%d: NO" % (cc + 1)

