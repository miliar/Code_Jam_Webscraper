def solution(case, sol):
	print "Case #%d: %s" % (case, sol)

def gen_case2(length, a, b):
	s = ""
	for i in xrange(length):
		if i%2 == 0:
			s += a
		else:
			s += b
	return s

def generate_partial(first, second, l_first, l_second):
	if first > second:#first ha de ser el petit
		first, second = second, first
		l_first, l_second = l_second, l_first
	s = ''
	for i in xrange(first):
		s += l_first + l_second

	s += (second - first) * l_second
	return s#nice

def interleave_third(partial, third, l_third):
	s = partial
	added = 0
	for i in xrange(1, third + 1):
		s = s[:-i-added] + l_third + s[-i-added:]
		added += 1
	#s = partial[:-1] + l_third + partial[-1:]
	return s

def	correct(string):
	for i in xrange(1, len(string)):
		if string[i] == string[i-1]:
			return False
	return string[0] != string[-1]

T = input()
for t in xrange(1, T+1):
	inpt = raw_input().split()

	N, R, O, Y, G, B, V = int(inpt[0]), int(inpt[1]), int(inpt[2]), \
							int(inpt[3]), int(inpt[4]), int(inpt[5]), int(inpt[6])

	everything = [R, O, Y, G, B, V]
	#used = [i for i in everything if i != 0]
	names = []
	used = {}
	if R > 0:
		names.append('R')
		used['R'] = R
	if O > 0:
		names.append('O')
		used['O'] = O
	if Y > 0:
		names.append('Y')
		used['Y'] = Y
	if G > 0:
		names.append('G')
		used['G'] = G
	if B > 0:
		names.append('B')
		used['B'] = B
	if V > 0:
		names.append('V')
		used['V'] = V
	colors = len(used)


	if colors == 1:
		if N > 1:
			solution(t, "IMPOSSIBLE")
		else:
			solution(t, names[0])
	elif colors == 2:
		if used[names[0]] == used[names[1]]:
			solution(t, gen_case2(N, names[0], names[1]))
		else:
			solution(t, "IMPOSSIBLE")
	elif colors == 3:
		if R >= Y >= B:
			first = R
			l_first = 'R'
			second = Y
			l_second = 'Y'
			third = B
			l_third = 'B'
		elif Y >= R >= B:
			first = Y
			l_first = 'Y'
			second = R
			l_second = 'R'
			third = B
			l_third = 'B'
		elif R >= B >= Y:
			first = R
			l_first = 'R'
			second = B
			l_second = 'B'
			third = Y
			l_third = 'Y'
		elif B >= R >= Y:
			first = B
			l_first = 'B'
			second = R
			l_second = 'R'
			third = Y
			l_third = 'Y'
		elif B >= Y >= R:
			first = B
			l_first = 'B'
			second = Y
			l_second = 'Y'
			third = R
			l_third = 'R'
		elif Y >= B >= R:
			first = Y
			l_first = 'Y'
			second = B
			l_second = 'B'
			third = R
			l_third = 'R'

		partial = generate_partial(first, second, l_first, l_second)

		final = interleave_third(partial, third, l_third)

		if (correct(final)):
			solution(t, final)
		else:
			solution(t, 'IMPOSSIBLE')

