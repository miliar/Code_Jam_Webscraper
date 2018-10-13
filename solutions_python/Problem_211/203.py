
def product(probs):
	p = 1
	for pr in probs:
		p *= pr
	return p

def share(N, U, probs):

	probs_sorted = sorted(probs)

	while U > 0:

		i = 1
		while i < N and probs_sorted[0] == probs_sorted[i]:
			i += 1

		if i < N:
			needed = (probs_sorted[i] - probs_sorted[0]) * i

		if i < N and needed < U:
			U -= needed
			for j in xrange(i):
				probs_sorted[j] = probs_sorted[i]
		else:
			for j in xrange(i):
				probs_sorted[j] += U/i
			U = 0
			

	return product(probs_sorted)


def main():
	T = int(raw_input())

	for t in xrange(T):

		line = raw_input().split()
		N, K = int(line[0]), int(line[1])
		U = float(raw_input())
		probs = map(float, raw_input().split()[:N])

		print 'Case #'+str(t+1)+': '+str(share(N, U, probs))

main()