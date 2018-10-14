for t in range(input()):
	X,R,C = map(int,raw_input().split(' '))
	if X==1:
		print "Case #%d: GABRIEL" % (t+1)
	elif X==2:
		if (R*C)%2==0:
			print "Case #%d: GABRIEL" % (t+1)
		else:
			print "Case #%d: RICHARD" % (t+1)
	elif X==3:
		if (R==3 and C==2) or (R==2 and C==3) or (R==3 and C==3) or (R==3 and C==4) or (R==4 and C==3):
			print "Case #%d: GABRIEL" % (t+1)
		else:
			print "Case #%d: RICHARD" % (t+1)
	elif X==4:
		if (R==4 and C==4) or (R==4 and C==3) or (R==3 and C==4):
			print "Case #%d: GABRIEL" % (t+1)
		else:
			print "Case #%d: RICHARD" % (t+1)
