import sys

t = int(sys.stdin.readline())

for i in xrange(t):
	n = int(sys.stdin.readline())

	nums = [int(x) for x in sys.stdin.readline().split()]
	
	wrong = 0
	for j in xrange(1,n+1):
		if nums[j-1] != j:
			wrong += 1

	print "Case #%d: %.6f" % (i+1, wrong)
