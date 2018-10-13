#!/usr/bin/env python

import time

# main

f = open('data/B-large.in', 'r')

cases = int(f.readline())

raw = []

for case in range(cases):
	raw.append(f.readline().rstrip().split(' '))

f.close()

start = time.time()

ff = open('data/B-large.out', 'w')

for casepos in range(cases):
	case = raw[casepos]
	
	c = float(case[0])
	f = float(case[1])
	x = float(case[2])
	
# 	print c, f, x
	
	tcum = 0
	fcum = 2
	
	while True:
		ta = x/fcum
		tb = c/fcum
		tc = tb + x/(fcum+f)
		
# 		print ta, tb, tc
				
		if(tc < ta):
			fcum = fcum + f
			tcum = tcum + tb
		else:
			tcum = tcum + ta
			s = 'Case #' + str(casepos + 1) + ': ' + str(tcum)
			print s
			ff.write(s + '\n')
			break;

ff.close()

end = time.time()
print end - start