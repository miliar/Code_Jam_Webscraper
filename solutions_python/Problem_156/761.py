f = open("/Users/sangypae/Desktop/gcj/B-small-attempt4.in", 'r')
contents = f.read()
cases = int(contents.split("\n")[0])
c1s = []
c2s = []
contents = contents.split("\n")[1:]
for i in range(cases):
	n = int(contents[2*i])
	l = map(int, list(contents[2*i+1].split(" ")))
	ori = l[:]
	l.sort()
	c = 0
	cs = []
	while max(l) > 1:
		cs.append(c+max(l))
		if l[-1] == 9 and 5 not in l:
			l[-1] = 6
			ap = 3
		else:
			if l[-1] % 2 == 1:
				l[-1] = l[-1]/2 + 1
				ap = l[-1]
			else:
				l[-1] = l[-1]/2
				ap = l[-1]
		l.append(ap)
		l.sort()
		c += 1
	if len(cs) == 0:
		c = 1
	else:
		c = min(cs)
	c1s.append(c)
for i in range(cases):
	n = int(contents[2*i])
	l = map(int, list(contents[2*i+1].split(" ")))
	ori = l[:]
	l.sort()
	c = 0
	cs = []
	while max(l) > 1:
		cs.append(c+max(l))
		if l[-1] % 2 == 1:
			l[-1] = l[-1]/2 + 1
			ap = l[-1]
		else:
			l[-1] = l[-1]/2
			ap = l[-1]
		l.append(ap)
		l.sort()
		c += 1
	if len(cs) == 0:
		c = 1
	else:
		c = min(cs)
	c2s.append(c)
for i in range(len(c1s)):
	c = min(c1s[i], c2s[i])
	g = open("/Users/sangypae/Desktop/gcj/b-output.txt", 'a')
	g.write("Case #" + `i+1`+": " + `c` + "\n")
	g.close()