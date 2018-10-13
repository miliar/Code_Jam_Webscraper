T = input()
fOut = open('codejam2.out','w')

for case in xrange(T):
	fOut.write('Case #' + str(case+1) + ': ')

	c,f,x = map(float, raw_input().split())
	print c,f,x
	time = 0.0
	rate = 2.0

	while(True):
		if(x/rate > (x/(rate+f) + c/rate)):
			time = time + c/rate
			rate = rate + f
			continue
		else:
			time = time + x/rate
			break

	fOut.write('%.7f'%time)
	if(case < (T-1)):
		fOut.write('\n')

fOut.close()