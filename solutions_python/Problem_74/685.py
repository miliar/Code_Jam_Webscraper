#!/usr/bin/env python

import sys, math

sys.stdin.readline()
case = 1
for line in sys.stdin:
	ans = 0
	line = line.strip().split()[1:]
	pos = {'O': (1, 0), 'B': (1, 0)}
	prev = '-'
	for word in line:
		if prev in 'OB':
			cur = prev
			other = 'O' if cur == 'B' else 'B'
			button_pos = int(word)
			prev_pos = pos[cur][0]
			prev_time = pos[cur][1]
			new_time = prev_time + abs(button_pos - prev_pos)
			if new_time < pos[other][1]:
				new_time = pos[other][1]
			new_time += 1
			pos[prev] = (button_pos, new_time)
			ans = new_time
		prev = word
	print "Case #%d: %d" % (case, ans)
	case += 1

