import sys
import os

T = int(sys.stdin.readline())

for t in xrange(T):
	l, num = sys.stdin.readline().split()

	count = 0
	added = 0
	for i, n in enumerate(num):
		n = int(n)
		count += n

		if i + 1 > count:
			added += i+1-count
			count = i + 1

	sys.stdout.write('Case #{0}: {1}\n'.format(t+1, added))

