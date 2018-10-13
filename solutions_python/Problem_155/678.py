def solve(s):
	a = flatten(map(lambda (n, m): [n for _ in range(m)], enumerate(s)))
	a = map(lambda (n, m): m - n, enumerate(a))
	return max(a)

def main():
	t = input()
	for i in range(1, t + 1):
		(n, s) = raw_input().split()
		s = map(lambda x: ord(x) - ord('0'), s)
		print "Case #%d: %d" % (i, solve(s))

def flatten(a):
	return [i for t in a for i in t]

if __name__ == "__main__":
	main()
