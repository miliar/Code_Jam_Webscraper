#encoding=utf-8
import re

if __name__ == '__main__':

	_, D, N = [int(v) for v in raw_input().split()]

	words = []
	for i in range(D):
		words.append(raw_input())

	patterns = []
	for i in range(N):
		patterns.append(re.compile(raw_input().replace('(', '[').replace(')', ']')))

	cache = {}
	for i in range(1, N+1):
		count = 0
		pattern = patterns[i-1]
		if not cache.has_key(pattern):
			for w in words:
				if pattern.match(w):
					count += 1
			cache[pattern] = count
		else:
			count = cache.get(pattern)
		print 'Case #%d: %d' % (i, count)
