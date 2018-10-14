inf = open('c-small.in', 'r')
outf = open('RollerAns.txt', 'w')

T = int (inf.readline())
for i in xrange(T):
	c = inf.readline()
	c = map(int, c.split())
	R = c[0]
	k = c[1]
	N = c[2]
	c = inf.readline()
	c = map(int, c.split())
	l = 0
	money = 0
	NumbPass = k
	for j in xrange(R):
		for m in xrange(N):
			if NumbPass < c[l%N]:
				break
			else:
				NumbPass -= c[l%N]
				l += 1
		money += k-NumbPass
		NumbPass = k
		if l%N == 0:
			cycle = R/(j+1)
			money = money*cycle
			l = 0
			for s in xrange(R%(j+1)):
				for m in xrange(N):
					if NumbPass < c[l%N]:
						break
					else:
						NumbPass -= c[l%N]
						l += 1
				money += k-NumbPass
				NumbPass = k
			break
		
	
	outf.write ('Case #' + str(i+1) + ': ' + str(money) + '\n')

inf.close()
outf.close()