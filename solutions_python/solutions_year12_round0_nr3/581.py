import sys

nolead = lambda tup: tup[0] != '0'

def check_value(A, B, x):
	return A <= x <= B

def rotate(l, n):
	return l[n:] + l[:n]

t = input()

for i in xrange(t):
	A, B = map(int, sys.stdin.readline().split())

	count = 0
	tupA, tupB = str(A), str(B)

	ch = set()
	size = len(tupA)

	for val in range(A, B+1):
		if str(val) not in ch:
			s = str(val)
			l = set([])
			for j in xrange(size):
				l.add(rotate(s, j))

			l = filter(nolead, l)
			l = filter(lambda x: tupA <= x <= tupB, l)

			t = len(l)
			if t > 1:
				count += (t * (t - 1) / 2)
			
			for k in l:
				ch.add(k)

	print "Case #{0}: {1}".format(i+1, count)