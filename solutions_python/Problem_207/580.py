from itertools import *		

inf = open("b.in", 'r')
outf = open("b.out", 'w')

t = int(inf.readline())

for tc in xrange(0, t):
	n, r, o, y, g, b, v = map(int, inf.readline().split())
	colors = [(r, "R"), (y, "Y"), (b, "B")]
	colors.sort()
	colors.reverse()
	#print colors
	
	myr = colors[0]
	myy = colors[1]
	myb = colors[2]
	
	
	myrn = myr[0]
	myyn = myy[0]
	mybn = myb[0]
	
	myrsym = myr[1]
	myysym = myy[1]
	mybsym = myb[1]
	
	s = ""
	x = myyn + mybn - myrn  #myb remains
	tr = myrn
	ty = myyn
	for i in xrange(0, x / 2):
		s += myrsym + mybsym + myysym + mybsym
		tr -= 1
		ty -= 1	
	if (x % 2 == 1):
		s += myrsym + mybsym + myysym
		tr -= 1
		ty -= 1
	for i in xrange(0, ty):
		s += myrsym + myysym
		tr -= 1
	for i in xrange(0, tr):
		s += myrsym + mybsym
		
	outf.write("Case #" + str(tc + 1) + ": ")
	if myrn > n / 2:	
		outf.write("IMPOSSIBLE\n")
	else:
		sl = len(s)
		for  i in xrange(0, sl - 1):
			if s[i]  == s[ i + 1]:
				print "Unicorns are sad! ", tc + 1
		if len(s) <> n:
				print "Unicorn lost or found! ", tc + 1, x, tr			
		outf.write(s + "\n")	
	
outf.close()
