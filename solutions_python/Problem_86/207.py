import sys, os
from math import sqrt

inf = open(sys.argv[1] , 'r')
outf = open('C-out', 'w')

cast_cnt = int(inf.readline())

for i in range(cast_cnt):
	ele = inf.readline().split()
	low = int(ele[1])
	high = int(ele[2])
	ele = inf.readline().split()
	others = []
	for e in ele:
		others.append(int(e))
	
	ok = False
	for j in range(low, high + 1):
		cnt = 0
		for o in others:
			if o >= j:
				if o % j == 0:
					cnt += 1
			else:
				if j % o == 0:
					cnt += 1
		if cnt == len(others):
			ok = True
			outf.write('Case #%d: %d\n' % (i + 1, j))
			break
	
	if not ok:
		outf.write('Case #%d: NO\n' % (i+1,))
