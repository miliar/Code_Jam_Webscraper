#!/usr/bin/env python2

T = int(raw_input())
for aa in range(1,T+1):

	n, m = map(int, raw_input().split(" "))

	if n < 10 and m < 10:
		print "Case #"+str(aa)+": 0"
		continue

	ss = {}
	
	for i in range(n, m):
		_n = i
		_m = str(i)
		
		for j in range(len(_m)):
			_m = _m[-1]  + _m[0: - 1]
				
			if (int(_m) <= m and _n < int(_m) and n <= int(_m) ):
				ss[(_n, _m)] = 1
	print "Case #"+str(aa)+": "+str(len(ss))


