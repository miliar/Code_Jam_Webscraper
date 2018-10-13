def recyclings(n):
	s = str(n)
	S = set()
	for i in xrange(1, len(s)):
		S.add(int(s[i:] + s[:i]))
	return S

def recycled_pairs(A, B):
	nb = 0
	for n in xrange(A, B):
		for m in recyclings(n):
			if n < m and m <= B:
				nb += 1
	return nb

T = int(raw_input())
for x in xrange(T):
	[A, B] = map(int, raw_input().split(' '))
	y = recycled_pairs(A, B)
	print("Case #%d: %d" % (x + 1, y))
