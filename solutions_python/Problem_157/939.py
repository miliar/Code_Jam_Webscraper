number_cases = int(raw_input())

cache = {('-i', 'i'): '1',
('-k', '-j'): '-i',
('-i', '1'): '-i',
('j', 'j'): '-1',
('-j', '-1'): 'j',
('-1', '-1'): '1',
('-k', 'k'): '1',
('-j', 'i'): 'k',
('-i', 'j'): '-k',
('-1', 'i'): '-i',
('k', 'j'): '-i',
('-j', '-k'): 'i',
('j', '-i'): 'k',
('-1', '-k'): 'k',
('1', '-i'): '-i',
('k', 'i'): 'j',
('j', 'k'): 'i',
('1', 'k'): 'k',
('i', '-i'): '1',
('k', '1'): 'k',
('i', 'k'): '-j',
('i', '-1'): '-i',
('-j', 'j'): '1',
('k', '-k'): '1',
('j', '-j'): '1',
('-1', '-j'): 'j',
('-j', '1'): '-j',
('-1', '1'): '-1',
('j', '1'): 'j',
('-k', 'j'): 'i',
('1', 'j'): 'j',
('1', '1'): '1',
('-i', '-k'): '-j',
('i', 'j'): 'k',
('-k', '-k'): '-1',
('-i', '-i'): '-1',
('-j', 'k'): '-i',
('k', '-j'): 'i',
('-1', 'k'): '-k',
('-i', '-1'): 'i',
('j', '-k'): '-i',
('1', '-k'): '-k',
('-k', '-i'): 'j',
('-k', '1'): '-k',
('-j', '-i'): '-k',
('i', '-k'): 'j',
('-i', '-j'): 'k',
('-1', '-i'): 'i',
('k', 'k'): '-1',
('j', 'i'): '-k',
('1', 'i'): 'i',
('k', '-i'): '-j',
('-1', 'j'): '-j',
('-k', 'i'): '-j',
('-k', '-1'): 'k',
('i', 'i'): '-1',
('j', '-1'): '-j',
('k', '-1'): '-k',
('1', '-j'): '-j',
('1', '-1'): '-1',
('-i', 'k'): 'j',
('i', '1'): 'i',
('-j', '-j'): '-1',
('i', '-j'): '-k'}

def exp(letter, n):
	m = n % 4
	if m == 1:
		return letter
	return cache[(letter, exp(letter, m - 1))]

def cumulate(string):
	if not string:
		return ''
	cumulative = [None] * len(string)
	cumulative[0] = string[0]
	for i in xrange(1, len(string)):
		cumulative[i] = cache[cumulative[i - 1], string[i]]
	return cumulative

def solve(string, x):
	first_stop = None
	second_stop = None
	cumulative = cumulate(string)
	assert len(cumulative) == len(string)
	if exp(cumulative[-1], x) != '-1':
		return False
	for i in xrange(x):
		for n, letter in enumerate(cumulative):
			l = cache[(exp(cumulative[-1], i), letter)]
			if l == 'i' and first_stop == None:
				first_stop = n + i * len(cumulative)
			if l == 'k':
				second_stop = n + i * len(cumulative)
				if first_stop is not None and second_stop > first_stop:
					return (first_stop, second_stop)
	return False

for n_case in xrange(number_cases):
	l, x = [int(x) for x in raw_input().split()]
	string = raw_input()
	assert len(string) == l
	if l * x < 3:
		print "Case #{}: NO".format(n_case+1)
	else:
		a = solve(string, x)
		if a == False:
			print "Case #{}: NO".format(n_case+1)
		else:
			p1, p2 = a
			s = string * x
			s1, s2, s3 = s[:p1 + 1], s[p1 + 1: p2 + 1], s[p2 + 1:]
			c1, c2, c3 = [cumulate(x)[-1] for x in (s1, s2, s3)]
			if (c1, c2, c3) != ('i', 'j', 'k'):
				raise Exception("HHHHHHHHHH")
			c = cumulate(s)
			for i in xrange(p1):
				if c[i] == 'i':
					raise Exception("GGGGGGGGGGG")
			if c[p1] != 'i' or c[p2] != 'k' or c[-1] != '-1':
				raise Exception("FFFFFFFF")
			print "Case #{}: YES".format(n_case+1)
