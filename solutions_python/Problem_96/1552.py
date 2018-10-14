#!/usr/bin/env python

import sys



cases = int(sys.stdin.readline())

for i in range(1,cases+1):
	data = sys.stdin.readline().split();
	N = int(data[0])
	S = int(data[1])
	p = int(data[2])
	t_i = data[3:]

	count = 0

	for t in t_i:
		tt = int(t)
		tmp = int(tt/3)
		mod = tt%3

		if(tt >= p):
			if(tmp >= p):
				# no surprise needed
				count += 1
			elif(tmp == p-1 and (mod == 2 or mod == 1)):
				# no surprise needed
				count += 1
			elif(S > 0 and tmp == p-1 and mod == 0):
				count += 1
				S -= 1
			elif(S > 0 and tmp >= p-2 and mod == 2):
				count += 1
				S -= 1

	print('Case #{}: {}'.format(i, count))