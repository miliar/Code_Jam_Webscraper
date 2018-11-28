#!/usr/bin/python

# snapper chain

# input:
# T    - number of test cases
# N K  - N - number of snappers, K - number of times snapped

# T = 1 .. 10,000
#
# N = 1 .. 10       N = 1 .. 30
# K = 0 .. 100      N = 1 .. 100,000,000

# output
# Case #n: ON/OFF

import sys

rl = sys.stdin.readline

for t in xrange(1, int(rl()) + 1):
	n, k = map(int, rl().split())
	onoff = 'OFF'

	if (k > 0) and (k >= n) and not ((k + 1) % (2 ** n)):
		onoff = 'ON'

	print 'Case #%d: %s' % (t, onoff)
