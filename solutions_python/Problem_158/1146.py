#!/usr/bin/env python

import time

filename = 'data/D-small-attempt1'
#filename = 'data/D'

G = 'GABRIEL'
R = 'RICHARD'

def calc(x, r, c):
	l = min(r, c)
	h = max(r, c)

	print l,h

	if x == 1:
		return G
	if (x == 3 or x == 4) and l == 1:
		return R
	if h < x:
		return R
	if x == 2:
		if (l * h) % 2 == 0:
			return G
		else:
			return R
	if x == 3:
		if (l * h) % 3 == 0:
			return G
		else:
			return R
	if x == 4:
		if l * h == 16 or l * h == 12:
			return G
		else:
			return R	
		
	return '!'	


f = open(filename + '.in', 'r')

cases = int(f.readline())

raw = []

for case in range(cases):
	l = f.readline().rstrip().split(' ')
	raw.append([int(l[0]), int(l[1]), int(l[2])])
f.close()

f = open(filename + '.out', 'w')

start = time.time()

case_row = 0
for case in raw:
	case_row += 1
	print case

	x = case[0]
	r = case[1]
	c = case[2]

	res = "Case #" + str(case_row) + ": " + calc(x, r, c)
	f.write(res + '\n')
	print res

end = time.time()

f.close()

print end - start


