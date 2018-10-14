from math import sqrt
fin = open("C-small-attempt0.in", 'r')
fout = open("fairOut.txt", 'w')

t = int(fin.readline())
case = 0
for i in xrange(t):
	if case != 0:
		fout.write("\n")
	case += 1
	count = 0
	x, y = map(int, fin.readline().split())
	p = x
	while p <= y:
		a = str(p)
		if a == a[::-1]:
			if sqrt(p) == int(sqrt(p)):
				s = str(int(sqrt(p)))
				if s == s[::-1]:
					count += 1
		p += 1
	fout.write("Case #" + str(case) + ": " + str(count))

fin.close()
fout.close()