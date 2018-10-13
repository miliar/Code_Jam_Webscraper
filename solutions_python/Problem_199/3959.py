import heapq as hq

def solve(s, k):
	return search(s, k)

def flip_self(s, k, i):
	for j in range(i, i+k):
		s[j] = '-' if s[j] == '+' else '+'

def flip(s, k, i):
	s = list(s)
	flip_self(s, k, i)
	return tuple(s)

def possible_flips(s, k):
	'''
	if k = len(s), None
	range(0, len(s) - k + 1)
	- i when s[i..i+k] all +
	'''
	#if len(s) == k:
	#	return set()
	#else:
	p = set()
	for i in range(0, len(s) - k + 1):
		for j in range(i, i+k):
			if s[j] == '-':
				p.add(i)
				break
	return p

def search(s, k):
	s = tuple(s) # frozenset
	closed = set()
	fringe = []
	hq.heappush(fringe, (s, 0))

	while len(fringe) != 0:
		_s, steps = hq.heappop(fringe)
		if '-' not in _s:
			return steps
		if _s not in closed:
			closed.add(_s)
			for i in possible_flips(_s, k):
				hq.heappush(fringe, (flip(_s, k, i), steps+1))
	return 'IMPOSSIBLE'

t = int(input())
for i in range(1, t+1):
	s, k = input().split(' ')
	s = list(s)
	k = int(k)

	print('Case #{}: {}'.format(i, solve(s, k)))