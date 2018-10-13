gets = lambda: input().split()
get = lambda: map(int, gets())

def memo(f):
	cache = dict()
	def wrap(*args):
		if args not in cache: cache[args] = f(*args)
		return cache[args]
	return wrap


def solve(p, k):
	b = [c == '+' for c in p]
	count = 0

	for i in range(len(b) - k + 1):
		if not b[i]:
			count += 1
			for j in range(i, min(i + k, len(b))):
				b[j] = not b[j]

	return str(count) if all(b) else 'IMPOSSIBLE'



testCases, = get()
for testCase in range(1, testCases+1):

	p, k = gets()
	result = solve(p, int(k))

	print('Case #{}: {}'.format(testCase, result))
