import sys

def are_recycled(n, m):
	n_str = str(n)
	m_str = str(m)
	n_str[0:]
	for l in xrange(1 ,len(n_str) ):
		if n_str[l:] + n_str[:l] == m_str: return True
	return False

t = int(sys.stdin.readline())

for i in xrange(t):
	data = sys.stdin.readline().split()
	a = int(data[0])
	b = int(data[1])
	count = 0
	for n in xrange(a, b + 1):
		for m in xrange(n + 1, b + 1):
			if are_recycled(n, m): count += 1
	print 'Case #%d: %d' % ( i + 1, count )