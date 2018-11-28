from heapq import heappush, heappop, heapify

class PQ(list):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		heapify(self)

	def push(self, item):
		heappush(self, item)

	def pop(self):
		return heappop(self)

gets = lambda: input().split()
get = lambda: map(int, gets())

def memo(f):
	cache = dict()
	def wrap(*args):
		if args not in cache: cache[args] = f(*args)
		return cache[args]
	return wrap



def solve(n, k):
	sc = {n: 1}
	pq = PQ([-n])

	left = k

	while True:
		n = -pq.pop()
		c = sc[n]

		left -= c
		if left <= 0:
			return (n // 2, n // 2) if n & 1 else (n // 2, n // 2 - 1)

		if n & 1:
			child = n // 2
			if child not in sc:
				sc[child] = 0
				pq.push(-child)
			sc[child] += 2 * c
		else:
			child1 = n // 2 - 1
			child2 = n // 2
			if child1 not in sc:
				sc[child1] = 0
				pq.push(-child1)
			if child2 not in sc:
				sc[child2] = 0
				pq.push(-child2)
			sc[child1] += c
			sc[child2] += c

@memo
def count(n):
	if n == 0:
		return 0
	if n & 1:
		return 1 + 2 * count((n - 1) // 2)
	else:
		return 1 + count(n // 2 - 1) + count(n // 2)


testCases, = get()
for testCase in range(1, testCases+1):
	
	n, k = get()
	x, y = solve(n, k)

	print('Case #{}: {} {}'.format(testCase, x, y))
