#!/usr/bin/env python

debug = False


def tidy(n):
	sn = [int(x) for x in list("%d" % n)]

	fixup = False
	for n in range(len(sn)):
		if n < (len(sn) - 1) and sn[n] > sn[n+1]:
			fixup = True
			break

	if fixup:
		sn[n] -= 1
		for m in range(n+1, len(sn)):
			sn[m] = 9

	ss = ''.join([str(x) for x in sn])

	if fixup:
		return tidy(int(ss))
	else:
		return int(ss)




num_tests = int(input())

for t in range(1, num_tests+1):
	n = int(input())
	res = tidy(n)
	if debug:
		print("Case #%d: %d -> %d" % (t, n, res))
	else:
		print("Case #%d: %d" % (t, res))
