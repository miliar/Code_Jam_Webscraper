#!/usr/bin/python2

def go(pos, time_move, time_wait, pos_move):
	dist = max(abs(pos - pos_move) - time_move, 0)
	return [dist + 1, 0, time_wait + dist + 1, pos]

T = int(raw_input())
for case_num in xrange(1, T + 1):
	a = raw_input().split()
	[n, res, time_o, time_b, pos_o, pos_b] = [int(a[0]), 0, 0, 0, 1, 1]
	for i in xrange(0, n):
		if a[i * 2 + 1] == 'O':
			status = go(int(a[i * 2 + 2]), time_o, time_b, pos_o)
			[time_o, time_b, pos_o] = status[1:]
		else:
			status = go(int(a[i * 2 + 2]), time_b, time_o, pos_b)
			[time_b, time_o, pos_b] = status[1:]
		res += status[0]
	print('Case #' + str(case_num) + ': ' + str(res))
