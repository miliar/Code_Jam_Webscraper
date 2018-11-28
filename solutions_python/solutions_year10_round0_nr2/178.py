import sys

def gcd(a, b):
	if a < b:
		a, b = b, a
	while b > 0:
		a %= b
		a, b = b, a
	return a

f = sys.stdin;

C = int(f.readline())
for i in range(1, C+1):
	p = f.readline().split()
	N = int(p[0])
	t = []
	for j in range(1, N + 1):
		t.append(int(p[j]))
	ans = 0
	for j in range(N):
		for k in range(N):
			if t[j] < t[k]:
				ans = gcd(ans, t[k] - t[j])
	ans = (ans - t[0] % ans) % ans
	
	print("Case #%d: %d" % (i, ans))

