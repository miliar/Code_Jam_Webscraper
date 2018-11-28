import sys

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

def solve():
	line = sys.stdin.readline().split(' ')
	n = int(line[0])
	t = {};
	for j in range(1, n + 1):
		t[j - 1] = int(line[j])
	g = abs(t[1] - t[0])
	for j in range(1, n):
		g = gcd(g, abs(t[j] - t[0]))
	x = (t[0] - 1) % g + 1
	print g - x

n = int(sys.stdin.readline())
for i in range(1, n + 1):
	sys.stdout.write("Case #" + str(i) + ": ")
	solve()
