# coding: shift-jis
# 空([])の時どうする

import sys

f = file(sys.argv[1])

test_cnt = int(f.readline())


for number in range(test_cnt):
	count   = int(f.readline())
	candies = map(int, f.readline().split())
	
	ret = reduce(lambda a,b: a^b, candies)
	if ret == 0:
		candies.sort()
		total = sum(candies[1:])
		print 'Case #%d:'%(number+1), total
	else:
		print 'Case #%d: NO'%(number+1)
	
