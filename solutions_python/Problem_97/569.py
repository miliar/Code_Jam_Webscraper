import sys

T = int(raw_input())

print >> sys.stderr, "Caching..."
cache = {}
for n in xrange(1, 2000001):
	n_str = str(n)
	ms = set()
	for i in xrange(1, len(n_str)):
		if n_str[i] == '0': continue
		m_str = n_str[i:] + n_str[:i]
		m = int(m_str)
		if m > n:
			ms.add(m)
	cache[n] = ms
print >> sys.stderr, "cache done."

for case_num in xrange(1, T+1):
	A,B = [int(x) for x in raw_input().split()]

	count = 0
	for n in xrange(A, B+1):
		for m in cache[n]:
			if A <= m <= B: count+=1
	print "Case #%d: %d" % (case_num, count)