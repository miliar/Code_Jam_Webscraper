import sys



def do_stuff(pairs, A, B):
	s = str(A)
	n = int(s)
	i = 0
	s_new = s
	c = 0
	while i < len(s):
		if s_new[0] == '0 ': continue

		s_new = s_new[1:] + s_new[0]
		m = int(s_new)
		if A <= n < m <= B:
			pairs[str(n)+str(m)] = 1
			c += 1
		i += 1

	return c
	

x = sys.stdin.readline()
x = int(x)
i = 1
while i <= x:
	input = sys.stdin.readline()
	input = input.split()
	A = int(input[0])
	B = int(input[1])
	pairs = {}

	total = 0
	while A <= B:
		total += do_stuff(pairs, A, B)
		A += 1
	out = len(pairs)
	print("Case #%d: %s" % (i, out)) 
	#print pairs
	#print total
	i += 1