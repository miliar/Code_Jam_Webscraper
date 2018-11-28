f = open("B.in")
g = open("Bw.txt",'w')
T = int(f.readline())
for t in range(T):
	N = int(f.readline())
	a = 0
	o = len(str(N))
	p = 0
	while o > 0 and p < 9:
		b = int("1" * o)
		if N >= a + b:
			a = a + b
			p = p + 1
		else:
			o = o - 1
	g.write("Case #" + str(t + 1)+": " + str(a)+"\n")


