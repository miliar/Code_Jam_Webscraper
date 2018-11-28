def tidy(s):
	for i, c in enumerate(zip(s, s[1:])):
		if c[1] < c[0]:
			return False, i

	return True, -1

def printSol(i, n):
	print("Case #{:d}: {:d}".format(i+1, n))

t = int(input())
for case_no in range(t):
	n = int(input())
	n_orig = n

	s = str(n)
	is_tidy, idx = tidy(s)

	while not is_tidy:
		l = list(s)
		l[idx] = str(int(l[idx]) - 1)
		l[idx+1:] = ['9' for _ in range(len(l)-1 - idx)]

		s = "".join(l)
		is_tidy, idx = tidy(s)

	printSol(case_no, int(s))