import sys, math
f = open("r02", "rb")
t = int(f.readline())
for i in range(t):
	l = f.readline().split()
	n = int(l.pop(0))
	ll = list()
	for j in range(n):
		ll.append((l[0], int(l[1])))
		l = l [2:]
	result = 0
	o = 1; b = 1
	oo = 0; bb = 0
	for j in ll:
		if j[0] == 'O':
			s = max (0, abs(j[1] - o) - oo)
			result += s + 1
			bb += s + 1
			oo = 0
			o = j[1]

		else:	
			s = max (0, abs(j[1] - b) - bb)
			result += s + 1
			oo += s + 1
			bb = 0
			b = j[1]

	print "Case #" + str(i) + ":",result
