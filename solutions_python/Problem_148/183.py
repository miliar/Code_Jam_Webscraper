from sys import argv

def solve(n, x, s):
	s.sort()
	i = 0
	j = n-1
	r = 0
	while i <= j:
		if s[i] + s[j] <= x:
			i += 1
		j -= 1
		r += 1
	return r

f = open(argv[1])
t = int(f.readline())
for i in range(t):
	n, x = map(int, f.readline().strip().split(' '))
	s = map(int, f.readline().strip().split(' '))
	print 'Case #{0}: {1}'.format(i+1, solve(n, x, s))