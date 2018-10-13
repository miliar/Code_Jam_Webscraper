def getBit(n,i):
	return (n>>i)&1;
def probDist(p):
	dist = []
	for x in xrange(0,(2<<len(p)-1)):
		prob=1
		for i in xrange(len(p)):
			if getBit(x,i):
				prob*=1-p[i]
			else:
				prob*=p[i]
		dist.append(prob)
	return dist

def getMask(n):
	return (2<<(n-1))-1

def keepTyping(t, l, p):
	#print t,l,p
	return (l-t+1)*p[0]+(l-t+l+2)*(1-p[0])

def backspace(t, l, x, p):
	#print t,l,x,p
	if t==x: return x+l+1;
	return x+keepTyping(t-x,l,probDist(p[:-x]))

def enter(t,l):
	return l+2

def solve(p,t,l):
	best = keepTyping(t,l,probDist(p))
	for x in xrange(t):
		score = backspace(t,l,x+1,p)
		if score<best:
			best = score
	score = enter(t,l)
	if score<best:
		best = score
	return best

f = open("A-small-attempt0.in","r")

lines = f.readlines()

l = 0
n = int(lines[0])
for case in xrange(n):
	typed = [int(num) for num in lines[case*2+1].split()]
	prob = [float(num) for num in lines[case*2+2].split()]
	print 'Case #'+str(case+1)+': '+str(solve(prob,typed[0],typed[1]))
