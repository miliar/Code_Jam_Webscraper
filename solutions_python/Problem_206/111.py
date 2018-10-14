def process(D, K, S):
	N = len(K)
	arrive = [-1.0]*N
	arrive[-1] = (D-K[-1])*1.0/S[-1]

	for i in reversed(range(N-1)):
		arrive[i] = max(arrive[i+1], (D-K[i])*1.0/S[i])

	return D*1.0/arrive[0]


def run():
	T = int(raw_input().strip())
	for caseno in range(T):
		D, N = map(int, raw_input().strip().split())
		K = [-1]*N
		S = [-1]*N
		for i in range(N):
			K[i], S[i] = map(int, raw_input().strip().split())

		print "Case #" + str(caseno+1) + ": " + format(process(D,K,S), '.10f')


run()