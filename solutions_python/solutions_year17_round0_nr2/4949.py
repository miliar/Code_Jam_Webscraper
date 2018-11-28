
def tidy(N):
	e = N % 10
	N = N / 10
	while N > 0:
		if e < N % 10:
			return False
		e = N % 10
		N = N / 10
	return True

def solve(N):
	while not tidy(N):
		N -= 1
	return N

T = int(raw_input())
for t in xrange(1, T + 1):
	arr = raw_input().split(' ')
	print "Case #{}: {}".format(t, solve(int(arr[0])))
