import sys

def line():
	return [int(s) for s in sys.stdin.readline().split()]

def state(n, k):
	return 0 == (k + 1) % (2 ** n)

labels = {True: 'ON', False: 'OFF'}

t = input()
for i in range(1, t + 1):
	(n, k) = line()
	s = labels[state(n, k)]
	print('Case #%d: %s' % (i, s))
