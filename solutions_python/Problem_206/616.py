T = int(input())

for t in range(T):

	D, N = list(map(int, input().split()))

	K = []
	S = []

	imin = -1
	tmin = -1
	for i in range(N):
		_K, _S = list(map(float, input().split()))
		K.append(_K)
		S.append(_S)

		t_temp = float(D - _K) / float(_S)

		if tmin == -1:
			tmin = t_temp
		else:
			if t_temp > tmin:
				tmin = t_temp

	res = float(D) / float(tmin)



	print("Case #{}: {}".format(t+1, res))
