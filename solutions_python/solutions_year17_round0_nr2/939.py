def tidy(v):
	last_s = '0'
	s = str(v)
	for c in s:
		if last_s > c: return False
		last_s = c

	return True

def solve():
	V = int(raw_input())

	while not tidy(V):
		# print "V:", V
		last_s = '0'
		s = str(V)

		for n in xrange(1,len(s)):
			if s[n-1] > s[n]:

				s = s[:n-1] + str(int(s[n-1])-1) + '9'*(len(s)-n)
				break

		V = int(s)

	return V

##########################################

T = int(raw_input())

for t in xrange(T):
	ans = solve()
	print "Case #%d:"%(t+1), ans
