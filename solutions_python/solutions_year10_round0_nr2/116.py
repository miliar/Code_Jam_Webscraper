import sys
def gcd(a,b) :
	while a != 0 :
		a,b = b%a , a
	return b ;
input = sys.stdin.read().split()
index = 0
def cin() : 
	global index
	r = int(input[index])
	index += 1
	return r
C = cin()
for c in range(C) :
	n = cin() 
	t = []
	for i in range(n) :
		t.append(cin())
	t.sort()
	step = t[1] - t[0] ;
	for i in range(n-1) :
		step = gcd(step,t[i+1]-t[i])
	ans = (step - (t[0] % step)) % step
	print "Case #%d: %d" % (c+1,ans)
