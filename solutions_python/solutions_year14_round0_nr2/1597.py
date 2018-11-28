outwr = ''
ckf = open('cookie.txt', 'r')
conts = ckf.read().split('\n')
ckf.close()

cases = int(conts[0])
for cn in range(cases):
	vals = [float(i) for i in conts[cn+1].split(' ')]
	cost = vals[0]
	fInc = vals[1]
	goal = vals[2]
	rate = 2
	inven = 0
	time = 0
	
	while inven != goal:
		if inven < cost:
			if (goal - inven)/rate < cost/rate:
				time += (goal-inven)/rate
				inven = goal
			else:
				time += cost/rate
				inven = cost
		else:
			if (goal - inven)/rate < goal/(rate + fInc):
				time += (goal-inven)/rate
				inven = goal
			else:
				rate += fInc
				inven = 0
	
	outwr += 'Case #' + str(cn+1) + ': ' + str(round(time,7)) + '\n'
	
outf = open('outB.txt', 'w')
outf.write(outwr)
outf.close()