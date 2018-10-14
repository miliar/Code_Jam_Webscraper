for i in xrange(int(raw_input())):
	x,r,c = map(int, raw_input().split())
	if x == 1:
		print 'Case #' + str(i+1) + ': GABRIEL'
	elif x == 2:
		if (r*c)%2 == 0:
			print 'Case #' + str(i+1) + ': GABRIEL'
		else:
			print 'Case #' + str(i+1) + ': RICHARD'
	elif x == 3:
		if (r == 2 and c == 3) or (r == 3 and c == 2) or (r == 3 and c == 3) or (r == 4 and c == 3) or (r == 3 and c == 4):
			print 'Case #' + str(i+1) + ': GABRIEL'
		else:
			print 'Case #' + str(i+1) + ': RICHARD'
	else:
		if (r == 3 and c == 4) or (r == 4 and c == 3) or (r == 4 and c == 4):
			print 'Case #' + str(i+1) + ': GABRIEL'
		else:
			print 'Case #' + str(i+1) + ': RICHARD'				

