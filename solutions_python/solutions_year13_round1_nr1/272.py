import sys
import os
from math import sqrt
w = open("A-large.in","r")
ww = open("A-large.out","w")
T = w.readline()
T = int(T)
wlist = w.read().split()
i = 0
for csT in range(T):
	r,t = wlist[i],wlist[i+1]
	i = i + 2;
	r = int(r)
	t = int(t)
	st = 0
	ans = -1
	ed = int(2 * (sqrt(t) + 1))
	while st <= ed:
		mid = (st + ed)/2
		res = (2 * r + 2 * mid + 1) * (mid + 1)
		if res <= t:
			if ans < mid:
				ans = mid
			st = mid + 1
		else:
			ed = mid - 1
	ww.write("Case #%s: %s\n" % (csT + 1, ans + 1))
ww.close()
	
