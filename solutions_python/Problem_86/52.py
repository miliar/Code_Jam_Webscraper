def cached(f):
	not_cached = object()
	cache = {}
	def wrapper(*args):
		result = cache.get(args, not_cached)
		if result is not not_cached:
			return result
		cache[args] = result = f(*args)
		return result
	wrapper.cache = cache
	return wrapper

def testCase():
	N, L, H = [int(n) for n in raw_input().split()]
	frequencies = [int(n) for n in raw_input().split()]

	if L == 1:
		return 1

	for f in xrange(L, H + 1):
		if all((freq % f) == 0 or (f % freq) == 0 for freq in frequencies):
			return f

	return "NO"

if __name__ == '__main__':
	for i in xrange(int(raw_input())):
		print "Case #%d: %s" % (i + 1, testCase())
