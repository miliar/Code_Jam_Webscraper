L, D, N = [int(n) for n in raw_input().split()]
words = [set() for i in xrange(L)]

def calc(pattern):
	if not '(' in pattern:
		return 1 if pattern in words[L-1] else 0
	i, j = pattern.find('('), pattern.find(')')
	res = 0
	for c in pattern[i+1:j]:
		if not (pattern[:i] + c) in words[i]: continue
		res += calc(pattern[:i] + c + pattern[j+1:])
	return res

for i in xrange(D):
	word = raw_input()
	for j in xrange(L):
		words[j].add(word[:j+1])

for i in xrange(N):
	pattern = raw_input()
	print "Case #%i: %i" % (i+1, calc(pattern))

