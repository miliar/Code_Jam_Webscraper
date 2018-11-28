#!/usr/bin/python2.6

def testCase():
	raw_input()
	values = [int(v) for v in raw_input().split()]
	if reduce(lambda x, y: x ^ y, values, 0):
		return "NO"
	values.sort()
	return sum(values[1:])

if __name__ == '__main__':
	for i in xrange(int(raw_input())):
		print "Case #%d: %s" % (i + 1, testCase())
