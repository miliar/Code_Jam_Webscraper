#!/usr/bin/env python

for T in range(int(raw_input())):
	S_max, S = raw_input().split()

	S_max = int(S_max)
	S = map(int, list(S))

	stand = S[0]
	invite = 0

	for i in range(1, S_max + 1):
		diff = (i - stand if i > stand else 0)
		stand += diff + S[i]
		invite += diff

	print 'Case #{0}: {1}'.format(T + 1, invite)
