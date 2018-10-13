
def speed(init, max_speeds, D, N):
	max_t = 1.0*(D-init[-1])/max_speeds[-1]
	for i in xrange(N-2, -1, -1):
		t_prime = 1.0*(D-init[i])/max_speeds[i]
		if t_prime > max_t:
			max_t = t_prime
	return str(D/max_t)


def main():
	T = int(raw_input())

	for t in xrange(T):

		line = raw_input().split()
		D, N = int(line[0]), int(line[1])
		max_speeds = []
		init = []
		for h in xrange(N):
			line = raw_input().split()
			init.append(int(line[0]))
			max_speeds.append(int(line[1]))

		print 'Case #'+str(t+1)+': '+speed(init, max_speeds, D, N)


main()