t = input()

def solve_dumb(n, k):

	stalls = [1]
	for _ in xrange(n):
		stalls.append(0)
	stalls.append(1)

	for i in xrange(k):
		ls, rs = -1, -1
		posAns = -1
		for pos in xrange(1, len(stalls) -1):
			if stalls[pos] > 0:
				continue

			lcnt = 0
			if pos > 1:
				for x in xrange(pos-1, -1, -1):
					if stalls[x] > 0:
						break
					else:
						lcnt += 1

			rcnt = 0
			if pos < n:
				for x in xrange(pos+1, n+2):
					if stalls[x] > 0:
						break
					else:
						rcnt += 1
			# print 'pos : {0}, lcnt: {1}, rcnt: {2}, ls: {3}, rs: {4}'.format(pos, lcnt, rcnt, ls, rs)
			if min(lcnt, rcnt) > min(ls, rs):
				ls = lcnt
				rs = rcnt
				posAns = pos
			elif min(lcnt, rcnt) == min(ls, rs):
				if rcnt > rs:
					ls = lcnt
					rs = rcnt
					posAns = pos
			else: continue

		stalls[posAns] = 1
		# print stalls
		if i == k-1:
			return max(ls, rs), min(ls, rs)
	return "wrong!", "yo"

for idx in xrange(1, t+1):
	n, k = map(int, raw_input().split())
	a, b = solve_dumb(n, k)
	print 'Case #{0}: {1} {2}'.format(idx, a, b)