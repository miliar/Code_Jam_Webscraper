def checkMore(s):
	l = len(s)
	flag = 0
	for i in range(0,l-1):
		if s[i] > s[i+1]:
			flag = 1
	return flag

def tidy(s):
	l = len(s)
	for i in range(0,l-1):
		if s[i] > s[i+1]:
			s[i] = s[i]-1
			for j in range(i+1, l):
				s[j] = 9
			break
	return s

t = input()
for i in range(0, t):
	case = raw_input()
	s = list(case)
	s = map(int, s)
	while checkMore(s) != 0:
		s = tidy(s)
	
	num = 0
	for e in s:
		num = num*10 + e
	print "Case #"+`i+1`+": "+`num`
