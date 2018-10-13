

def count_pairs(n, b):
	pairs = []
	for i in xrange(len(n), 0, -1):
		m = (n[i:] + n[:i]).lstrip('0')
		if (len(n) == len(m)) and (m not in pairs) and (int(n) < int(m) <= b):
			pairs.append(m)
	return len(pairs)


def total_pairs(a, b):
	total = 0
	for n in xrange(a, b):
		total += count_pairs(str(n), b)
	return total


test_cases = int(raw_input())
for test in xrange(1, test_cases + 1):
	a, b = [int(e) for e in raw_input().split()]
	print 'Case #%d: %d' % (test, total_pairs(a, b))