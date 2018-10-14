from Queue import PriorityQueue


def solve(n, k):
	space = PriorityQueue()
	space.put((-n, 0))
	for i in range(k - 1):
		free, position = space.get()
		free = -free
		new_people = position + (free - 1) / 2
		if new_people - position:
			t_1 = (- (new_people - position), position)
			space.put(t_1)
		if position + free - new_people - 1:
			t_2 = (- (position + free - new_people - 1), new_people + 1)
			space.put(t_2)
		# print sorted(people)
	free, position = space.get()
	free = -free
	if free % 2:
		return (free - 1) / 2, (free - 1) / 2
	else:
		return free / 2, free / 2 - 1


def allocate(s, c, stalls):
	stalls.pop(s)
	if s % 2 == 1:
		d = stalls.get((s - 1) / 2)
		if d is not None:
			stalls[(s - 1) / 2] = d + c * 2
		else:
			stalls[(s - 1) / 2] = c * 2
		return (s - 1) / 2, (s - 1) / 2
	else:
		d1 = stalls.get(s / 2)
		d2 = stalls.get(s / 2 - 1)
		if d1 is not None:
			stalls[s / 2] = d1 + c
		else:
			stalls[s / 2] = c
		if d2 is not None:
			stalls[s / 2 - 1] = d2 + c
		else:
			stalls[s / 2 - 1] = c
		return s / 2, s / 2 - 1


def solve2(n, k):
	count = 0
	stalls = {n: 1}
	while k > count:
		keys = sorted(stalls.keys(), reverse=True)
		for s in keys:
			c = stalls.get(s)
			if count + c >= k:
				return allocate(s, c, stalls)
			else:
				count += c
				allocate(s, c, stalls)
	return 0, 0


if __name__ == '__main__':
	T = int(raw_input())
	for t in range(1, T + 1):
		line = raw_input()
		N, K = [int(i) for i in line.split()]
		ans = solve2(N, K)
		print "Case #%s: %s %s" % (t, ans[0], ans[1])
