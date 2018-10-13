din = open('large.in','r')
dout = open('large.out','w')

T = int(din.readline())

for K in range(1,T+1):
	line = list(din.readline().split())
	D = int(line[0])
	N = int(line[1])

	hdict = []
	for i in range(N):
		line = list(din.readline().split())
		hdict.append((D - int(line[0]))/float(line[1]))
	minS = max(hdict)
	res = D / minS
	dout.write('Case #%d: %s\n' % (K, str(res)))

	
din.close()
dout.close()
