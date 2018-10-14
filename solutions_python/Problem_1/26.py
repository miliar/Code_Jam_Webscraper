import sys
sys.stdin = file('qral.in')
n = int(raw_input())
for case_count in xrange(n):
	n = input()
	names = dict((raw_input().strip(),i) for i in xrange(n))
	vs = [0] * n
	m = input()
	for loop in xrange(m):
		query = raw_input().strip()
		idx = names[query]
		for i in xrange(n):
			vs[i] = min(vs[i], vs[idx] + 1)
		vs[idx] = m+1

	print "Case #%d: %d" % (case_count+1, min(vs))
