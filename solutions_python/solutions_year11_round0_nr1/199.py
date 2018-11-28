#! /usr/bin/env python3
T = int(input())
for i in range(T):
	N, *RP = input().split()
	last_time = {'O': 0, 'B': 0}
	last_pos = {'O': 1, 'B': 1}
	time = 0
	for j in range(int(N)):
		R, P = RP[j*2:j*2+2]
		dist = abs(int(P) - last_pos[R])
		time = max(time, last_time[R] + dist) + 1
		last_time[R] = time
		last_pos[R] = int(P)
	print('Case #%d: %d' % (i+1, time))