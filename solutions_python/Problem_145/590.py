from math import log,ceil

cc = int(raw_input().strip())

def gcd(x,y):
	if(x > y):
		return gcd(y,x)
	if(y%x == 0):
		return x
	return gcd(y%x,x)

for ccc in range(1,cc+1):
	print 'Case #' + str(ccc) + ':',
	P,Q = raw_input().strip().split('/')
	P = int(P)
	Q = int(Q)
	g = gcd(P,Q)
	if(g != 1):
		P /= g
		Q /= g
	base = log(Q,2)
	if(base != int(base)):
		print 'impossible'
	else:
		ans = log(float(Q)/float(P),2)
		print int(ceil(ans))
