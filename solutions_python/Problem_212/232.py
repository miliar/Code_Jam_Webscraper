from math import *
from fractions import Fraction as F
import sys
import os

si = sys.stdin
so = sys.stdout
se = sys.stderr

readline = raw_input
readargs = lambda : readline().split()
readints = lambda : map(int, readargs())

T = readints()[0]
for t in range(1, T + 1):
	n, p = readints()
	groups = map(lambda x : x % p, readints())
	cnt = [0] * p
	for i in groups:
		cnt[i] += 1
	if p == 2:
		ans = cnt[0] + (cnt[1] + 1) / 2
	elif p == 3:
		ans1 = cnt[0]
		ans2 = min(cnt[1], cnt[2])
		ans3 = (abs(cnt[1] - cnt[2]) + 2) / 3
		ans = ans1 + ans2 + ans3
	elif p == 4:
		ans1 = cnt[0]
		ans2 = (cnt[2] + 1) / 2 + min(cnt[1], cnt[3])
		cnt[2] &= 1
		lft = abs(cnt[1] - cnt[3])
		ans3 = 0
		if cnt[2] > 0 and lft >= 2:
			ans3 = 1
			cnt[2] = 0
			lft -= 2
		ans4 += (lft + 3) / 4
		ans = ans1 + ans2 + ans3 + ans4

	print ('Case #%d:' % t), ans
