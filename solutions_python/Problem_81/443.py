import sys


def read(N,inIter):
	instance=[]
	for lineNo in range(N):
		line = next(inIter)
		instance.append(line.strip())
	return instance
PREC = 10**13
def solve(N, m):
	OOWP = [None] * N
	OWP = [None] * N
	WP = {}
	def wp(i, hide=None):
		x = (i,hide)
		if x in WP:
			return WP[x]
		count = 0
		val = 0
		for (idx, v) in enumerate(m[i]):
			if v != '.' and idx != hide:
				count += 1
				val += int(v)
				
		WP[x] = (val*PREC)/count
		return WP[x]
	
	def owp(i):
		if OWP[i] is not None:
			return OWP[i]
		count = 0
		val = 0
		for (idx, v) in enumerate(m[i]):
			if v != '.':
				count += 1
				val += wp(idx, i)
				
		OWP[i] = val/count
		return OWP[i]

	def oowp(i):
		if OOWP[i] is not None:
			return OOWP[i]
		count = 0
		val = 0
		for (idx, v) in enumerate(m[i]):
			if v != '.':
				count += 1
				val += owp(idx)
		OOWP[i] = val/count
		return OOWP[i]
	
	RPI=[]
	for i in range(N):
		rpi = (wp(i)+2*owp(i)+oowp(i))/4.0/PREC
		RPI.append(rpi)
	return RPI
	
fname = sys.argv[1]
inF = open(fname, 'r')
outF = open(fname+'.out', 'w')

inIter = iter(inF)
T = int(next(inIter))
for case in range(1,T+1):
	N = int(next(inIter))
	instance = read(N,inIter)
	solution = solve(N,instance)
	print >>outF, "Case #%i:" % case
	print >>outF, "\n".join(map(str,solution))

outF.close()