f = open("/Users/sangypae/Desktop/gcj/A-large.in", 'r')
contents = f.read()
cases = int(contents.split("\n")[0])
contents = contents.split("\n")[1:]
for i in range(cases):
	m, s = contents[i].split(" ")
	m = int(m)
	l = len(s)
	t = 0
	c = 0
	for x in range(l):
		p = int(s[x])
		if t >= x or p == 0:
			t += p
		else:
			c += x-t
			t += p+x-t
	g = open("/Users/sangypae/Desktop/gcj/a-output.txt", 'a')
	g.write("Case #" + `i+1`+": " + `c` + "\n")
	g.close()