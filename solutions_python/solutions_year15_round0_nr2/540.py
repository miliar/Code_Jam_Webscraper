def solve(d, p):
	mx = max(p)
	ans = mx
	for i in range(1, mx + 1):
		t = 0
		for j in p:
			t += (j - 1) / i
		ans = min(ans, t + i)
	return ans

def main():
	t = input()
	for i in range(1, t + 1):
		d = input()
		p = map(int, raw_input().split())
		print "Case #%d: %d" % (i, solve(d, p))

if __name__ == "__main__":
	main()
