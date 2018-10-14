# coding: shift-jis

import sys

f = file(sys.argv[1])

test_cnt = int(f.readline())


for number in range(test_cnt):
	count = int(f.readline())
	elems = map(int, f.readline().split())
	
	ret = count
	for i, e in enumerate(elems):
		if i+1 == e: ret -= 1
	
	
	print 'Case #%d:'%(number+1), '%0.6lf'%float(ret)