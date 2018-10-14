from collections import deque, defaultdict
from queue import PriorityQueue

def f(n):
	n1 = n-1
	if n % 2 == 0:
		return ((n1//2), (n//2))
	else:
		return ((n//2), (n//2))

T = int(input())
for t in range(1, T+1):
	N, K = map(int, input().split())
	"""
	c = 1
	p = 0
	while True:
		n1 = N-1
		if N % 2 == 1 and K - p <= c:
			print('Case #%s: %s %s' % (t, n1//2, n1//2))
			break
		elif N % 2 == 0:
			if K - p <= c:
				print('Case #%s: %s %s' % (t, n1//2, n//2))
			elif K - p - c <= c:
				print('Case #%s: %s %s' % (t,

		p += c
		c *= 2
	"""

	D = defaultdict(int)
	D[N] = 1
	while True:
		n = list(sorted(D.keys()))[-1]
		p = D.pop(n)

		if K <= p:
			mi, ma = f(n)
			print('Case #%s: %s %s' % (t, ma, mi))
			break

		K -= p

		if n % 2 == 0:
			D[n // 2] += p
			D[(n-1) // 2] += p
		else:
			D[n // 2] += 2*p

	continue


	Q = PriorityQueue()
	Q.put(f(N) + (N,))

	for j in range(K):
		mi, ma, n = Q.get()

		Q.put(f(n//2) + (n//2,))
		if n % 2 == 0:
			n1 = (n-1) // 2
			Q.put(f(n1) + (n1,))
		else:
			Q.put(f(n//2) + (n//2,))

		if j == K-1:
			print('Case #%s: %s %s' % (t, -ma, -mi))


