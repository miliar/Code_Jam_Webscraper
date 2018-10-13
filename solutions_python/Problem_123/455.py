# -*- coding:utf-8 -*-

f = open("input.txt","r")
lines  = int(f.readline())
i = 1
Y = 0

def Decision(d,a,y):
	global Y
	c = a
	if len(d)==0:
		if y < Y:
			Y = y
		return
	if y > Y:
		return
	while 1:
		if len(d)==0:
			if y < Y:
				Y = y
			return
		t = d.pop()
		if c > t:
			c = c+t
		else:
			d.append(t)
			break
	# remove all
	if Y > (len(d)+y):
		Y = y + len(d)
	# try add
	t = d.pop()
	b = 0
	while 1:
		if c == 1:
			d.append(t)
			b = 101
			break
		if c <= t:
			b=b+1
			c=c+c-1
		else:
			d.append(t)
			break
	Decision(d,c,y+b)

	return




while i<=lines:
	#Problem Start
	l = f.readline()
	s = l.split()
	A = int(s[0])
	N = int(s[1])
	l = f.readline()
	Ni= l.split()

	D = []
	for d in Ni:
		D.append(int(d))

	# use .pop()
	D.sort()
	D.reverse()
	Y = 101
	Decision(D,A,0)

	print "Case #%d: %d" % (i, Y)
	#End
	i=i+1

f.close
