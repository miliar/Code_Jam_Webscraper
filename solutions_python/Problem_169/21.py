from fractions import Fraction

nT = int(raw_input())

def initP(p):
    return (Fraction(p[0]), Fraction(p[0]) * Fraction(p[1]))

def cross(a, o, b):
	return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def cmpAngle(a, b):
	c = cross(a, (0, 0), b)
	if c > 0:
		return -1
	elif c < 0:
		return 1
	else:
		return 0

def check(n, rpo, stdP, mi):
	po = []
	for i in range(n):
		po.append((rpo[i][0] * mi, rpo[i][1] * mi))
	for i in range(n):
		po.append((-po[i][0], -po[i][1]))
	
	for i in range(1, n * 2):
		po[i] = (po[i][0] + po[i - 1][0], po[i][1] + po[i - 1][1])
	po.append(po[0])
	
	maxX = Fraction(0)
	maxY = Fraction(0)
	for i in range(n * 2):
		if cross(po[i + 1], po[i], stdP) < 0:
			return False
		maxX = max(maxX, po[i][0])
		maxY = max(maxY, po[i][1])
	return stdP[0] <= maxX and stdP[1] <= maxY

for t in range(1, nT + 1):
    n, stdP0, stdP1 = raw_input().split()
    
    n = int(n)
    stdP = initP((stdP0, stdP1))
    
    rpo = []
    for i in range(n):
    	rpo.append(initP(raw_input().split()))
    rpo.sort(cmpAngle)
    print "Case #" + str(t) + ":",
    
    if not check(n, rpo, stdP, 100000000):
    	print "IMPOSSIBLE"
    else:
    	rL = Fraction(0)
    	rR = Fraction(100000000)
    	for times in range(60):
    		rM = (rL + rR) / 2
    		if not check(n, rpo, stdP, rM):
    			rL = rM
    		else:
    			rR = rM
    	print "%.9f" % float(rL)
