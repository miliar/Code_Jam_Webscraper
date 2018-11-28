#ugh this system doesnt have python3 installed

def check(n):
	s = str(n)
	return list(s) == sorted(s)

def solve(n):
	s = map(int, list(str(n)))
	while True:
		i = 1
		fix = False
		while i < len(s):
			if fix:
				s[i] = 9
			elif s[i-1] > s[i]:
				#print s, i, s[i-1], s[i]
				s[i-1] -= 1
				s[i] = 9
				fix = True
			i += 1
		if not fix:
			break
	return int(''.join(map(str, s)))

if __name__ == "__main__":
	T = int(raw_input())
	for case in xrange(T):
		N = int(raw_input())
		soln = solve(N)
		assert check(soln), soln
		print "Case #%s: %s" % (case+1, soln)
