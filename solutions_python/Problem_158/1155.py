from sys import argv

T = int(input())
for t in xrange(T):
	line = raw_input().split(' ')
	X = int(line[0])
	R = int(line[1])
	C = int(line[2])

	if R*C < X:
		who = 'RICHARD'
	else:
		if X==1:
			who = 'GABRIEL'
		elif X==2:
			if (R,C) in [(1,2),(2,1),(1,4),(4,1),(2,2),(2,3),(3,2),(2,4),(4,2),(3,4),(4,3),(4,4)]:
				who = 'GABRIEL'
			else:
				who = 'RICHARD'
	 	elif X==3:
			if (R,C) in [(2,3),(3,2),(3,3),(3,4),(4,3)]:
				who = 'GABRIEL'
			else:
				who = 'RICHARD'
	 	elif X==4:
			if (R,C) in [(3,4),(4,3),(4,4)]:
				who = 'GABRIEL'
			else:
				who = 'RICHARD'
	print 'Case #'+str(t+1)+': '+str(who)