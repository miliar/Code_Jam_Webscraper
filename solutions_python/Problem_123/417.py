import sys

t = int(sys.stdin.readline().strip())

def foo(a, b, x):
	if x >= len(b):
		return 0
	if a == 1:
		return foo(a, b, x+1) + 1
	elif b[x] < a:
		return foo(a+b[x], b, x+1)
	else:
		foo1 = foo(a, b, x+1) + 1
		o = 0
		while a <= b[x]:
			a += a-1
			o += 1
		foo2 = foo(a+b[x], b, x+1) + o
		return min(foo1, foo2)

def foo2(a, b):
	foo1 = 0
	foo2 = 0
	for bb in b:
		foo2 = min(foo1, foo2) + 1
		if a == 1:
			foo1 = sys.maxint
		elif bb < a:
			a += bb
		else:
			while a <= bb:
				a += a-1
				foo1 += 1
			a += bb
	return min(foo1, foo2)

for i in range(1, t+1):
	a, n = [int(x) for x in sys.stdin.readline().strip().split()]
	b = [int(x) for x in sys.stdin.readline().strip().split()]
	b.sort()
	print 'Case #%d: %d' % (i, foo2(a,b))
		