from __future__ import division

import fileinput

count = int(raw_input())
case = 0

while True:
	case += 1
	if count < case:
		break

	D, N = map(int, raw_input().split())
	longest_time = 0
	for i in range(N):
		K, S = map(int, raw_input().split())
		hours = (D - K) / S
		longest_time = max(longest_time, hours)
	speed = D / longest_time
	print "Case #%s: %s" % (case, speed)
