import sys,operator

t = int(sys.stdin.readline())

for i in xrange(t):
	sys.stdin.readline()
	nums = [int(x) for x in sys.stdin.readline().split()]
	if reduce(operator.xor,nums) != 0:
		print "Case #%d: NO" % (i+1)
	else:
		print "Case #%d: %d" % (i+1,sum(nums) - min(nums))
	
