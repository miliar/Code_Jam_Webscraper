t = int(raw_input())
cas = 0
f = open("out.txt", "w")
while t:
	t -= 1
	s = raw_input()
	res = ""
	while True:
		get = -1
		for i in range(len(s) - 1):
			if s[i + 1] < s[i]:
				get = i
				break
		if get == -1:
			break
		r = s[:get] + chr(ord(s[get]) - 1) + '9' * (len(s) - get - 1)
		s = r
	cas += 1
	f.write('Case #%d: %s\n' % (cas, s.lstrip('0')))
