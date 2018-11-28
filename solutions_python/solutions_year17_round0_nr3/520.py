import sys

def solve():
	n, k = (int(x) for x in sys.stdin.readline().split())
	s = {}
	s[n] = 1
	a = []
	a.append(n)
	while True:
		x = a[0]
		a = a[1:]
		#~ print("{}: {}".format(x, s[x]), file=sys.stderr)
		mx, mn = x // 2, (x-1) // 2
		if k <= s[x]:
			print("{} {}".format(mx, mn))
			return
		k -= s[x]
		if mx not in s:
			a.append(mx)
			s[mx] = 0
		s[mx] += s[x]
		if mn not in s:
			a.append(mn)
			s[mn] = 0
		s[mn] += s[x]

def main():
	t = int(sys.stdin.readline())
	for i in range(t):
		print("Case #{}: ".format(i+1), end='')
		solve()

if __name__ == "__main__":
	main()
