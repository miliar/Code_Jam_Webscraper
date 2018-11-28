fi = open("input.txt", "r+")
fo = open("output.txt", "r+")

t = fi.readline().strip()

case = 1
for l in fi:
	l = l.strip()
	c = l.split()
	c[0] = int(c[0])
	a = []
	for s in c[1]:
		a.append(int(s.strip()))
	c[1] = a
	inv = 0
	appl = 0
	for i, n in enumerate(c[1]):
		if appl + inv >= i:
			appl += n
		else:
			inv += 1
			appl += n
	fo.write("Case #" + str(case) + ": " + str(inv) + "\n")
	case += 1