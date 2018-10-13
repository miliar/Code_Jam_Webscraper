f = open("2.in")
d = f.read()
f.close()

d = d.split("\n")

N = int(d[0])

def gcd(a, b):
	if b == 0: return a
	return gcd(b, a % b)

def getVector(v):
	v = v.split(" ")
	return [int(v[i]) for i in xrange(1,len(v))]

def gcd2(v):
	g = v[0]
	for n in v:
		g = gcd(g, n)
	return g

f = open("2.out", "wa")

for icase in xrange(N):
	v = getVector(d[icase+1])
	nums = []
	for a in v:
		for b in v:
			if a > b: nums += [a - b]
	g = gcd2(nums)
	
	if g == 1: sol = 0
	else: sol = g - v[0] % g
	
	if v[0] % g == 0:
		sol = 0
	else:
		sol = ((v[0] / g) + 1) * g - v[0]
	
	LINE = "Case #%d: %d" % (icase+1, sol)
	print LINE
	f.write(LINE + "\n")

f.close()
