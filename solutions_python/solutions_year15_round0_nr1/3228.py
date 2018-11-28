f = open('A-large.in', 'r')
fw = open('output.in', 'w')
N = int(f.readline())
for i in range(N):
	x = f.readline()
	n, s = x.split(" ")
	p = 0
	q = 0
	for j in range(int(n) + 1):
		p += int(s[j])
		if p <= j:
			q += (j+1 - p)
			p += (j+1 - p)
	fw.write("Case #%s: %s\n" % (i+1, q))

f.close()
fw.close()