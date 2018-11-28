import psyco
psyco.full()

def r(s):
	if len(s) == 0: return 0
	if len(s) == 1: return 1
	if s[0] == s[1]:
		return r(s[1:])
	return 1 + r(s[1:])


def allperms(xs): # [int] - >[[int]]
		if len(xs) == 1:
			return [xs]
		else:
			return add(xs[0], allperms( xs[1:] ) )
			
def add(x,xss):# char -> [[char]] -> [[char]]
		result = []
		for xs in xss:
			result += [xs[:i]+[x]+xs[i:] for i in range(len(xs)+1)]
		return result

def perm(s,p):
	if len(s) == 0 :return []
	k = [s[i] for i in p]
	return k + perm(s[len(p):],p)
	

input  = file("d-small.in")
totalNumber = int(input.readline())
old = (0,0)
for case in range(1,totalNumber+1):
	k = int(input.readline())
	s = input.readline()[:-1]
	#print len(s),k
	x = len(s)
	for p in allperms(range(k)):
		assert len(p) == k
		x = min(r(perm(s,p)),x)

	print "Case #%i: %i" %(case,x)
		
	
