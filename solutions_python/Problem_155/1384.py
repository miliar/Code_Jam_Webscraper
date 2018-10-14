f = open('A-large.in', 'r')

T = int(f.readline())
for i in range(T):
	[n, l] = f.readline().split(' ')
	nLevel = int(n)
	claque = 0
	nApplause = 0
	for shyness in range(nLevel+1):
		nSpect = int(l[shyness])-int('0')
		if nApplause < shyness:
			nApplause = nApplause + 1
			claque = claque + 1
		nApplause = nApplause + nSpect
	print 'Case #' + str(i + 1) + ': ' + str(claque)