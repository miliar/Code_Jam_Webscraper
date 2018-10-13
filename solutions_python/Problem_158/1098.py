import math
f = open('d.in', 'r')
nTestCase = int(f.readline()[0:-1])
for numCase in range(0,nTestCase):
	l = f.readline()[0:-1].split(' ')
	X = int(l[0])
	R = int(l[1])
	C = int(l[2])
	if X==1:
		win = False
	elif X==2:
		win = R%2==1 and C%2==1
	elif X==3:
		win = not (R%2==0 and C%3==0 or R%3==0 and C%2==0 or R==3 and C==3)
	else:
		win = not (R==4 and C==4 or R==4 and C==3 or R==3 and C==4)
	if win:
		print "Case #"+str(numCase+1)+": RICHARD"
	else:
		print "Case #"+str(numCase+1)+": GABRIEL"
