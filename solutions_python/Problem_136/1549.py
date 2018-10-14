N = int(raw_input())

for case in xrange(N):
	C,F,X = map(float,raw_input().strip().split())
	#print C,F,X
	
	besttime = X/2.0
	parsum = 0
	fact = 0

	while True:
		parsum += C/(2.0+fact*F)
		newtime = parsum + X/(2.0+(fact+1)*F)
		fact+=1
		#print newtime
		if besttime < newtime: break
		if besttime > newtime:
			besttime = newtime
		

	print 'Case #'+str(case+1)+':',besttime
	