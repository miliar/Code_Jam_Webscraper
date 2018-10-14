def process(E,S,D):
	time = 0.0
	N = len(E)
	horses = [(E[0], S[0], D[0][1], 0.0)]

	for i in range(1,N-1):
		newhorses = []
		d = D[i][i+1]
		arrive = -1
		for e,s,dd,t in horses:
			if e >= dd+d:
				newhorses.append((e, s, dd+d, t))
			if arrive < 0 or arrive > dd*1.0/s + t:
				arrive = dd*1.0/s + t
		if E[i] >= d and arrive >= 0:
			newhorses.append((E[i],S[i],d,arrive))

		horses = newhorses

	arrive = [dd*1.0/s+t for e,s,dd,t in  horses]
	return min(arrive)

def run():
	T = int(raw_input().strip())
	for caseno in range(T):
		N, Q = map(int, raw_input().strip().split())
		E, S = zip(*[map(int, raw_input().strip().split()) for _ in range(N)])
		D = [map(int, raw_input().strip().split()) for _ in range(N)]
		U, V = zip(*[map(int, raw_input().strip().split()) for _ in range(Q)])
		print "Case #" + str(caseno+1) + ": " + format(process(E,S,D), '.10f')

run()
