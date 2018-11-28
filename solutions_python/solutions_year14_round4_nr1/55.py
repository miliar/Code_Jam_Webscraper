
def f():
	n, c = map(int, raw_input().split())
	sizes = map(int, raw_input().split())
	sizes.sort()
	sizes = sizes[::-1]
	used = [False] * n
	ans = 0
	for i in xrange(n):
		if used[i]:
			continue
		used[i] = True
		for j in xrange(n):
			if used[j] or sizes[j] + sizes[i] > c:
				continue
			else:
				used[j] = True
				break
		ans += 1
	return ans

T = input()
for i in xrange(1, T+1):
	print "Case #%s: %s" % (i, f())