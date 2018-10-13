import sys


T = int(raw_input())

for tt in xrange(1, T + 1):
	s = raw_input().split()
	c = int(s[0])
	t = s[1:1 + c]
	a = {}
	for i in t:
		a[i[0:2]] = i[2]
	d = int(s[1 + c])
	t = s[2 + c:2 + c + d]
	b = {}
	for i in t:
		if not (i[0] in b):
			b[i[0]] = []
		b[i[0]].append(i[1])
		if not (i[1] in b):
			b[i[1]] = []
		b[i[1]].append(i[0])
	n = int(2 + c + d)
	s = s[3 + c + d]
	t = []
	for i in s:
		if t:
			x = t[-1] + i
			if x in a:
				t = t[0:-1]
				t.append(a[x])
				continue
			x = i + t[-1]
			if x in a:
				t = t[0:-1]
				t.append(a[x])
				continue
		if i in b:
			f = False
			for j in b[i]:
				if j in t:
					t = []
					f = True
					break
			if f:
				continue
		t.append(i)
	print "Case #%d:" % tt, str(t).replace("'", '')
