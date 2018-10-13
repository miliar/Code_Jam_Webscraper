import sys

N = int(sys.stdin.readline())

for i in range(N):
	size = int(sys.stdin.readline())
	x = sys.stdin.readline().split()
	y = sys.stdin.readline().split()
	a = []
	b = []
	for j in range(size):
		a.append(int(x[j]))
		b.append(int(y[j]))
	a.sort(reverse=True)
	b.sort()
	total = 0
	for j in range(size):
		v = a.pop()
		w = b.pop()
		total = total + v * w
	print "Case #%d:" % (i + 1), total

