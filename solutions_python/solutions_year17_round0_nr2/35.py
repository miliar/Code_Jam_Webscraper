gets = lambda: input().split()
get = lambda: map(int, gets())

def memo(f):
	cache = dict()
	def wrap(*args):
		if args not in cache: cache[args] = f(*args)
		return cache[args]
	return wrap



def decrement(d):
	x = list(reversed(d))
	for i in range(len(x)):
		x[i] -= 1
		if i+1 == len(x) or x[i] >= x[i+1]:
			break
		x[i] = 9
	while x and x[-1] <= 0: x.pop()
	return ''.join(map(str, reversed(x)))

def solve(n):
	d = list(map(int, n))

	pos = None
	for i in range(len(d) - 1):
		if d[i] > d[i+1]:
			pos = i
			break

	if pos is None:
		# No problems
		return n

	return decrement(d[:pos+1]) + '9' * (len(d) - pos - 1)





testCases, = get()
for testCase in range(1, testCases+1):
	
	n, = gets()
	result = solve(n)

	print('Case #{}: {}'.format(testCase, result))
