t = int(raw_input())

def solve():
	s = list(raw_input())

	for i in xrange(len(s)-2, -1, -1):
		if ord(s[i]) > ord(s[i+1]):
			s[i] = chr(ord(s[i])-1)
			for j in range(i+1, len(s)):
				s[j] = '9'

	while s[0] == '0':
		s = s[1:]

	return "".join(s)

def report(t, s):
	print "Case #{}: {}".format(t, s)

for i in xrange(t):
	report(i+1, solve())