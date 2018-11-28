tc = int(input())
c = 1
while c <= tc:
	s = input()
	s = s.split()
	l = int(s[0])
	s = s[1]
	count = 0
	shy = 0
	inv = 0
	for i in s:
		n = int(s[shy])
		if count >= shy:
			count += n
		else:
			if n > 0:
				inv += (shy - count)
				count = shy + n
		shy += 1
	p = 'Case #' + str(c) + ':'
	print(p, inv)
	c += 1