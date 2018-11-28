import sys

index = 0
for line in open(sys.argv[1]).readlines()[1:]:
	index += 1
	res = {}
	start, end = map(int, line.split())
	for i in xrange(start, end+1):
		n = i
		for j in xrange(1,len(str(i))):
			tmp = n % 10**j
			m = n / 10**j
			m += tmp * 10**(len(str(n))-j)
			if n < m and m <= end:
				res[(n,m)] = 1
				#print n, " ", m
	print "Case #%i: %i" % (index, len(res))
