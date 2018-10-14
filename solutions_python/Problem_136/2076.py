import math
def solve(C, F, X):
	n = int(math.ceil(X/C - (1 + 2/ F)))
	n = max(0, n)
	ans = 0
	for i in range(n):
		ans += C/(2.0 + i*F)
	ans += X/(2.0 + n*F)
	return str(ans)

if __name__ == "__main__":
	import sys
	f = open(sys.argv[1], "r")
	T = int(f.readline())
	for case in range(1, T+1):
		C, F, X = tuple(map(float, f.readline().split()))
		print "Case #"+str(case)+": "+solve(C, F, X)
