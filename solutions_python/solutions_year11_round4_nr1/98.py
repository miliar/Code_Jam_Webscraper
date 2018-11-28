#!/usr/bin/env python

import sys

cases = int(sys.stdin.readline())

for case in xrange(1, cases + 1):
	print "Case #%d:" % case,
	X, S, R, t, N = [int(val) for val in sys.stdin.readline().strip().split()]
	walkways = []
	for i in xrange(N):
		B, E, w = [int (val) for val in sys.stdin.readline().strip().split()]
		walkways.append((B, E, w))
	walkways.sort()
	summary = []
	cur = 0
	while cur < X:
		speed = S
		if len(walkways) == 0:
			next_pos = X
			summary.append((float(speed), float(next_pos - cur)))
			cur = next_pos
		else:
			next_pos = walkways[0][0]
			if cur == next_pos:
				speed += walkways[0][2]
				next_pos = walkways[0][1]
				summary.append((float(speed), float(next_pos - cur)))
				cur = next_pos
				walkways.pop(0)
			else:
				summary.append((float(speed), float(next_pos - cur)))
				cur = next_pos
	summary.sort()
	time = 0.0
	used_fast = 0.0
	for part in summary:
		if used_fast < t:
			speed = float(part[0] + R - S)
			dist = float(part[1])
			if used_fast + (dist / speed) > t:
				d = speed * (t - used_fast)
				time += (t - used_fast)
				used_fast = t + 1
				speed = part[0]
				dist = part[1] - d
				time += dist / speed
			else:
				used_fast += (dist / speed)
				time += dist / speed
		else:
			speed = part[0]
			dist = part[1]
			time += dist / speed
	print time
