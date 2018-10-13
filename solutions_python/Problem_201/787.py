import sys

def solve(N, K):

	Q = {N}

	d = dict()
	d[N] = 1

	c = max(Q)
	Q.remove(c)

	while c > 0:

		if c%2 == 1:
			if c/2 not in d:
				d[c/2] = 2*d[c]
			else:
				d[c/2] += 2*d[c]
			Q.add(c/2)

		else:
			if c/2 not in d:
				d[c/2] = d[c]
			else:
				d[c/2] += d[c]
			Q.add(c/2)

			if (c/2)-1 not in d:
				d[(c/2) - 1] = d[c]
			else:
				d[(c/2) - 1] += d[c]
			Q.add((c/2) - 1)

		c = max(Q)
		Q.remove(c)

	for k in sorted(d.keys(), reverse=True):
		K -= d[k]
		if K <= 0:
			return k/2, k/2 - 1 + (k%2)


lines = sys.stdin.readlines()

T = int(lines[0].strip())

for t in range(T):
	N, K = lines[t+1].strip().split()
	N = int(N)
	K = int(K)
	answer = solve(N, K)
	print "Case #{}: {} {}".format(t+1, answer[0], answer[1])
