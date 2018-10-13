
def solve(D, KS):
	KS.sort()
	slowest = 0
	for i in KS:
		t = float(D - i[0]) / i[1]
		if t > slowest:
			slowest = t
	return D / slowest


t = int(raw_input())

for i in range(1, t + 1):
	D, N = map(int, raw_input().strip().split())
	KS = [None] * N
	for j in range(N):
		KS[j] = map(int, raw_input().strip().split())

	print("Case #%d: %s" % (i, solve(D, KS)))
