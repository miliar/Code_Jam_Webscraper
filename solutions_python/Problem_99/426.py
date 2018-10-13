#!/usr/bin/env python

t = input()

for i in range(t):
	l = raw_input().split(' ')
	a = int(l[0])
	b = int(l[1])

	l = raw_input().split(' ')
	p = []
	for x in l:
		p.append(float(x))

	k = []
	if a == 1:
		k.append(2*b+1-p[0]*(b+1))
		k.append(2*b+3-p[0]*(b+1))
		k.append(b+2)
	elif a == 2:
		k.append(2*b-p[0]*p[1]*(b+1))
		k.append(2*b+2-p[0]*(b+1))
		k.append(b+3)
		k.append(b+2)
	elif a == 3:
		k.append(2*b-1-p[0]*p[1]*p[2]*(b+1))
		k.append(2*b+1-p[0]*p[1]*(b+1))
		k.append(2*b+3-p[0]*(b+1))
		k.append(b+4)
		k.append(b+2)

	print "Case #%d: %.6f"%(i+1,min(k))
