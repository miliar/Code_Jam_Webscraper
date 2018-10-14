#!/usr/bin/python2.6

def testCase():
	result = 0
	raw_input()
	result = sum(int(v)!=i+1 for i, v in enumerate(raw_input().split()))
	return str(result) + ".000000"

if __name__ == '__main__':
	for i in xrange(int(raw_input())):
		print "Case #%d: %s" % (i + 1, testCase())
