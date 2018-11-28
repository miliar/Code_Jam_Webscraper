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

tokenize = lambda: raw_input().split()
tokenize_int = lambda: [int(v) for v in tokenize()]

def ntokenize():
	t = tokenize()
	n = int(t.pop(0))
	assert len(t) == n
	return t

def ntokenize_int():
	t = tokenize_int()
	n = t.pop(0)
	assert len(t) == n
	return t



def testCase():
	N = int(raw_input())
	vines = []
	for i in xrange(N):
		d, l = tokenize_int()
		vines.append((d, l, i))
	vines.sort()
	D = int(raw_input())
	reachability = [0] * N
	ds = []
	ls = []
	todo = []
	for n, (d, l, i) in enumerate(vines):
		ds.append(d)
		ls.append(l)
		if i == 0:
			reachability[n] = min(d, l)
			todo.append(n)
	while todo:
		j = todo.pop()
		d_min = ds[j] - reachability[j]
		d_max = ds[j] + reachability[j]
		assert reachability[j]
		if d_min <= D <= d_max:
			return "YES"
		i = j - 1
		while i >= 0 and ds[i] >= d_min:
			r = min(ds[j] - ds[i], ls[i])
			if reachability[i] < r:
				reachability[i] = r
				todo.append(i)
			i -= 1
		k = j + 1
		while k < N and vines[k][0] <= d_max:
			r = min(ds[k] - ds[j], ls[k])
			if reachability[k] < r:
				reachability[k] = r
				todo.append(k)
			k += 1
	return "NO"

if __name__ == '__main__':
	for i in xrange(int(raw_input())):
		print "Case #%d: %s" % (i + 1, testCase())
