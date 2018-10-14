t = int(raw_input())

def isTidy(x):
	ref1 = list(str(x))
	ref2 = sorted(ref1)
	if ref1 == ref2:
		return True
	else:
		return False

def findTidy(x):
	i = 1
	while not isTidy(x):
		x -= x % (10**i) + 1
		i += 1
	return x

for i in xrange(1, t + 1):
	n = int(raw_input())
	print "Case #{}: {}".format(i, findTidy(n))