dump = open('B.in', 'r').readlines()

test_cases = int(dump[0][:-1])
print test_cases
for t in xrange(test_cases):
	print 'Case #{}:'.format(t+1),
	c = 0
	a, b, k = map(int, dump[1:][t][:-1].split(' '))
	for x in xrange(a):
		for y in xrange(b):
			if x & y < k:
				c += 1
	print c
