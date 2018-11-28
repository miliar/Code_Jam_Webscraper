import sys
f = open(sys.argv[1])
N = int(f.readline())
for case in xrange(1, N+1):
	[A,B,K] = map(int, f.readline().rstrip().split(" "))
	count = 0
	for i in xrange(A):
		for j in xrange(B):
			if i&j < K:
				count += 1
	print "Case #%s: %s" %(case, count)

