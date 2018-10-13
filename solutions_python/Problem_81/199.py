import sys



def calcWP(wp):
	for y in dlist:
		nwin = 0.0
		nsum = 0.0
		for x in y:
			if x == "1":
				nsum += 1.0
				nwin += 1.0
			elif x == "0":
				nsum += 1.0
		wp += [ nwin / nsum ]
		
def calcNWP(b,a):
	nwin = 0.0
	nsum = 0.0
	for x in range(len(dlist[a])):
		if x == b:
			continue
		if dlist[a][x] == "1":
			nsum += 1.0
			nwin += 1.0
		elif dlist[a][x] == "0":
			nsum += 1.0
	return nwin/nsum
	

def calcOWP(owp):
	nCt = 0
	for y in dlist:
		nwp = 0.0
		nsum = 0.0
		for x in range(len(y)):
			if y[x] != ".":
				nsum += 1.0
				nwp += calcNWP(nCt,x)
		owp += [ nwp / nsum ]
		nCt += 1

def calcOOWP(oowp,owp):
	for y in dlist:
		nowp = 0.0
		nsum = 0.0
		for x in range(len(y)):
			if y[x] != ".":
				nsum += 1.0
				nowp += owp[x]
		oowp += [ nowp / nsum ]

def calcRPI(rpi):
	for y in range(len(dlist)):
		rpi += [0.25 * wp[y] + 0.50 * owp[y] + 0.25 * oowp[y]]
		


dlist = []
wp = []
owp = []
oowp = []
rpi = []

n = 0
l = 0
for line in sys.stdin:
	if n == 0:
		n = 1
		continue

	if l == 0:
		N = int(line[:-1])
		l = 1
		dlist = []
		wp = []
		owp = []
		oowp = []
		rpi = []
		continue
	
	if l < (N):
		dlist += [line[:-1]]
		l += 1
		continue
	else:
		dlist += [line[:-1]]
		calcWP(wp)
		calcOWP(owp)
		calcOOWP(oowp,owp)
		calcRPI(rpi)
		
		print "Case #" + str(n) + ":"
		for x in range(len(dlist)):
			print str(rpi[x])
		l = 0
		n += 1
		
