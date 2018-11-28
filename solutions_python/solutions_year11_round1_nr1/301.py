inf = open('A-small-attempt2.in', 'r')
outf = open('aAns.txt', 'w')

T = int(inf.readline())
for j in xrange(T):
	print j
	c = inf.readline()
	c = map(long, c.split())
	N, Pd, Pg = c
	print N, Pd, Pg
	if N>=99:
		answer = 'Possible'
	else:
		answer = 'Broken'
		for i in xrange(1, N+1):
			if Pd == 0:
				answer = 'Possible'
				break
			if (Pd*i)%100 == 0:
				answer = 'Possible'
				break
	if Pg == 100:
		answer = 'Broken'
	if Pg == 0 and Pd != 0:
		answer = 'Broken'
	if Pg == 100 and Pd == 100:
		answer = 'Possible'


	outf.write('Case #' + str(j+1) + ': ' + answer + '\n')
	print answer
inf.close()
outf.close()		