def resolve_flip(state, pan_size):
	bool_state = [True if i=="+" else False for i in list(state)]
	cakes = len(state)
	count = 0
	for i in xrange(cakes):
		if not bool_state[i]:
			if i > cakes-pan_size:
				return "IMPOSSIBLE"
			bool_state[i:i+pan_size] = [not j for j in bool_state[i:i+pan_size]]
			count += 1
	return count


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n, m = raw_input().split(" ")  # read a list of integers, 2 in this case
	m = int(m)
	print "Case #{}: {}".format(i, resolve_flip(n,m))
