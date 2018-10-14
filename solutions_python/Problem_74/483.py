inf = open('A-large.in', 'r')
outf = open('robotsAns.txt', 'w')

T = int(inf.readline())
for j in xrange(T):
	pos = {}
	mas = []
	pos['O'] = 1
	pos['B'] = 1
	c = inf.readline()
	c = c.split()
	prevcol = c[1]
	time = int(c[2])
	pos[prevcol] = time
	alltimes = [[time]]
	i = 3
	while(i<len(c)):
		curcol = c[i]
		i += 1
		num = int(c[i])
		i += 1
		if curcol!=prevcol:
			prevcol = curcol
			time = abs(num - pos[curcol]) + 1
			alltimes.append([time])
			pos[curcol] = num
		else:
			time = abs(num - pos[curcol]) + 1
			pos[curcol] = num
			alltimes[-1].append(time)
	ans = 0
	for i in xrange(1, len(alltimes)):
		for k in alltimes[i-1]:
			ans += k
			alltimes[i][0] -= k
			if alltimes[i][0] <= 0:
				alltimes[i][0] = 1
	for k in alltimes[-1]:
		ans += k	
	outf.write('Case #' + str(j+1) + ': ' + str(ans) + '\n')

inf.close()
outf.close()
		
