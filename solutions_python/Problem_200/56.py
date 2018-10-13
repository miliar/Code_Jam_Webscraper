def tidy(n):
	s = list(n)
	ind = len(s)
	lst = range(len(s)-1)
	lst.reverse()
	for i in lst:
		if s[i] > s[i+1]:
			ind = i+1
			s[i] = chr(ord(s[i])-1)

	for i in range(ind,len(s)):
		s[i] = '9'
	while s[0] == '0':
		s.pop(0)
	return "".join(s)

t = int(raw_input())
for q in range(t):
	n = raw_input()
	print "Case #" + str(q+1) + ": " + tidy(n)