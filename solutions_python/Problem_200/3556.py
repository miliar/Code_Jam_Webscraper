def is_tidy(n):
	n = str(n)
	for i in range(len(n) - 1):
		if n[i] > n[i+1]:
			return False
	return True


def solve(n):
	while not is_tidy(n):
		n -= 1
	return n

if __name__ == '__main__':
	T = int(raw_input())
	for t in range(1, T+1):
		num = int(raw_input())
		ans = solve(num)
		print "Case #%s: %s" % (t, ans)
