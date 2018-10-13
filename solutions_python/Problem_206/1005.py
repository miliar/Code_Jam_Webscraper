
T = int(raw_input())

for i in xrange(T):
	pos_list = []
	speed_list = []
	slowest_eta = 0

	D, N = [int(s) for s in raw_input().split(" ")]
	for j in xrange(N):
		K, S = [int(s) for s in raw_input().split(" ")]

		pos_list.append(K)
		speed_list.append(S)

		eta = float(D-K) / S

		if eta > slowest_eta or slowest_eta == 0:
			slowest_eta = eta

	speed = 0
	if slowest_eta > 0:
		speed = float(D) / slowest_eta

	print "Case #%d: %f" % ((i + 1), speed)
