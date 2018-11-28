import sys

[T] = [int(x) for x in sys.stdin.readline().split()]

for K in range(1, T + 1):
	[n, p] = [int(x) for x in sys.stdin.readline().split()]
	inp = [int(x) for x in sys.stdin.readline().split()]

	if p == 2:
		even = len([x for x in inp if x % 2 == 0])

		print "Case #%d: %d" % (K, even + (n - even + 1) / 2)
	elif p == 3:
		trip = len([x for x in inp if x % 3 == 0])
		one = len([x for x in inp if x % 3 == 1])
		two = len([x for x in inp if x % 3 == 2])

		print "Case #%d: %d" % (K, trip + min(one, two) + (abs(one - two) + 2) / 3)
	elif p == 4:
		quad = len([x for x in inp if x % 4 == 0])
		one = len([x for x in inp if x % 4 == 1])
		two = len([x for x in inp if x % 4 == 2])
		thr = len([x for x in inp if x % 4 == 3])

		gr1 = min(one, thr)
		one -= gr1
		thr -= gr1

		gr2 = min(two, (one + thr) / 2)
		two -= gr2

		if one != 0:
			one -= gr2 * 2
		else:
			thr -= gr2 * 2

		gr3 = two / 2
		two -= gr3 * 2

		gr4 = (one + thr) / 4

		if one != 0:
			one -= gr4 * 4
		else:
			thr -= gr4 * 4

		if one + two + thr != 0:
			add = 1
		else:
			add = 0

		print "Case #%d: %d" % (K, quad + gr1 + gr2 + gr3 + gr4 + add)
		# print gr1, gr2, gr3, gr4

'''
===
5
4 3
4 5 6 4
4 2
4 5 6 4
3 3
1 1 1
4 4
4 2 5 3
4 4
3 3 2 2
---
Case #1: 3
Case #2: 4
Case #3: 1
Case #4: 4
Case #5: 4
===
'''