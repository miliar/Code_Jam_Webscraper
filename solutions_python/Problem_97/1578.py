#!/usr/bin/python

f = open('C-small-attempt0.in', 'r')
n = int(f.readline())
for i in range(1, n+1):
	line = f.readline().split()
	a = int(line[0])
	b = int(line[1])
	y = 0
	done = []
	for x in range(a, b+1):
		x = str(x)
		done.append(x)
		tempdone = []
		for idx in range(len(x)-1, 0, -1):
			z = x[idx:len(x)] + x[0:idx]
				
			xi = int(x)
			zi = int(z)

			if zi >= a and zi <= b and xi < zi and zi not in done and len(str(xi)) == len(str(zi)) and zi not in tempdone:
				y += 1
				tempdone.append(zi)

	print "Case #" + str(i) + ": " + str(y)
