import sys
def mul(l):
	def m(a,b):
		return a*b
	return reduce(m,l,1.0)

f = open("a.in")
cases = int(f.readline())

for i in xrange(cases):
	line = f.readline()
	a = int(line.split()[0])
	b = int(line.split()[1])
	probs = [float(x) for x in f.readline().split()]
	allright = mul(probs)
	minexp = 1.0 + b + 1
	keepTyping = 0.0
	keepTyping += allright * (b-a+1)
	backspaceNth = [0] * a
	for n in xrange(a):#nth character is wrong  
		prob = mul(probs[0:n])*(1-probs[n])
		keepTyping += prob * (b-a+2+b)
		for c in xrange(1,a+1):#back space c times
			keys = 0
			if c+n >= a: # the wrong char is erased
				keys = prob * (c+b-(a-c)+1)
			else:	   # the wrong char is not erased
				keys = prob * (c+b-(a-c)+1+b+1)
			
			backspaceNth[c-1]+=keys
	for n in xrange(a):
		backspaceNth[n]+=allright * (n+1+b-(a-n-1)+1)
	minimum = min(backspaceNth)
	if minimum < minexp:
		minexp = minimum
	if keepTyping < minexp:
		minexp = keepTyping				
	print "Case #%d: %f"%(i+1,minexp)



