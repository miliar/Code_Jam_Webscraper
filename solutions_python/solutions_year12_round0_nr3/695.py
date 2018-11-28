#!/usr/bin/env python
import re


def rotate(nr, small, big):
	cnt = 0
	done = {}

	for i in range(1, len(nr)):
		tmp = nr[i:] + nr[:i]
		if tmp[0] != '0':
			if (tmp > nr) and (tmp <= big) and tmp not in done:
				cnt = cnt + 1
				done[tmp] = 1
	return cnt


def check(small, big):
	cnt = 0

	for i in range(int(small), int(big)):
		nr = str(i)
		cnt = cnt + rotate(nr, small, big)

	return cnt


N = input()
for i in range(N):
	line = raw_input()
	line = re.split(' +', line)
	A = int(line[0])
	B = int(line[1])
	print "Case #%d: %s" % (i + 1, check(str(A), str(B)))
