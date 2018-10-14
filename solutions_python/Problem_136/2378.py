#!/usr/bin/python

fi = file("B-large.in", "r")
fo = file("a.out", "w")

n = int(fi.readline())
for i in range(n):
	l = fi.readline().split()
	c = float(l[0])
	f = float(l[1])
	x = float(l[2])
	p = 2.0
	t = x / p
	b = 0
	while 1:
		b += c / p
		if t < b + x / (p+f):
			break
		else:
			t = b + x / (p+f)
			p += f
	t = round(t, 8)
	fo.write("Case #"+str(i+1)+": "+str(t)+"\n")
