
def token():
	return raw_input()
def tokens():
	return raw_input().strip().split()

for t in range(int(raw_input())):
	D, N = map(int, tokens())
	T = 0
	for i in range(N):
		K, S = map(int, tokens())
		T = max(T, float(D - K)/S)
	S_max = D / T
	print "Case #{}: {}".format(t+1, S_max)
