f = open('B-small-attempt1.in', 'r')
l = f.readlines()
f.close()
c = 0
for a in l:
	s = str(a)
	s = s.rstrip()
	i = 0
	if c == 0:
		c += 1
		continue
	if len(s) == 1:
		r = s
	elif int(s) < int(s[0] * len(s)):
		if int(s[0]) == 1:
			t = ''
		else:
			t = str(int(s[0]) - 1)
		t += '9' * (len(s) - 1)
		r = t
	else:
		res = None
		while i < (len(s) - 1):
			if int(s[i]) > int(s[i+1]):
				if res == None:
					res = str(int(s[i]) - 1)
				else:
					res += str(int(s[i]) - 1)
				t = '9' * (len(s) - i - 1)
				res += t
				r = res
				break
			else:
				if res == None:
					if i == len(s) - 2:
						res = s[i]
						res += s[i+1]
					else:
						res = s[i]
				else:
					if i == len(s) - 2:
						res += s[i]
						res += s[i+1]
					else:
						res += s[i]
			i += 1
		if res == None or int(res) == int(s):
			r = s
	result = 'Case #%d: %s' % (c, r)
	print result
	c += 1