#normal: ti >= 3p-2
#suprising: ti >= 3p-4 (and <= 3p-2) (p > 1)

1121
1112

def testCase():
	A, B = [int(token) for token in raw_input().split()]
	result = 0
	d = 1
	nd = 1
	while 10*d <= A:
		d *= 10
		nd += 1
	rng = xrange(len(str(A))-1)
	for m in xrange(A+9, B+1):
		n = m
		dup = set()
		for i in rng:
			n, n1 = divmod(n, 10)
			n += n1 * d
			if A <= n < m:
				if n not in dup:
					dup.add(n)
					result += 1
	return result


if __name__ == '__main__':
	for i in xrange(int(raw_input())):
		print "Case #%d: %d" % (i+1, testCase())
