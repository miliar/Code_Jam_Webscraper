f = open("a.in", "r")
d = f.read()
f.close()

def solve(p, a, q, b):
	for i in xrange(4):
		a[i] = a[i].split(" ")
		b[i] = b[i].split(" ")
		a[i] = [int(v) for v in a[i]]
		b[i] = [int(v) for v in b[i]]
	v = a[p-1]
	w = b[q-1]
	c = []
	for i in v:
		for j in w:
			if i == j: c.append(i)
	if len(c) == 1: return str(c[0])
	if len(c) > 0: return "Bad magician!"
	return "Volunteer cheated!"

d = d.split("\n")[:-1]
n = int(d[0])
d = d[1:]

f = open("a.out", "w")
for i in xrange(n):
	s = "Case #%d: %s" % (i+1, solve(int(d[i*10]), [d[i*10+1],d[i*10+2],d[i*10+3],d[i*10+4]], int(d[i*10+5]), [d[i*10+6],d[i*10+7],d[i*10+8],d[i*10+9]]))
	print s
	f.write(s+"\n")
f.close()

