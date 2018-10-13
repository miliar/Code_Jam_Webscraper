#!/usr/bin/python
import sys, math
def i(a):
	return a==a[::-1]
n = 0
with open(sys.argv[1]) as f:
	for line in f.read().splitlines()[1:]:
		n = n+1
		count = 0
		num = map(lambda x:int(x), line.split(' '))
		for x in range(num[0], num[1]+1):
			sq = int(math.sqrt(x))
			if sq**2 == x and i(str(x)) and i(str(sq)):
				count=count+1
		print "Case #%i: %i" % (n, count)
