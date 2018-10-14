#!/usr/bin/env python

import time

filename = 'data/A-small-attempt1'
#filename = 'data/A'

f = open(filename + '.in', 'r')

cases = int(f.readline())

raw = []

for case in range(cases):
	l = f.readline().rstrip().split(' ')
	raw.append([int(l[0]), l[1]])
f.close()

f = open(filename + '.out', 'w')

start = time.time()

case_row = 0
for case in raw:
	case_row += 1
	print case
	stand = 0
	need = 0
	for i in range(case[0] + 1):
		p = int(case[1][i])

		if p > 0 and stand < i:
			need += i-stand
			stand += need
		stand += p

		print stand, need

	res = "Case #" + str(case_row) + ": " + str(need)
	f.write(res + '\n')
	print res
	#print stand, need

end = time.time()

f.close()

print end - start

