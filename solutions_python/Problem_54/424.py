from sys import stdin

def gcd(a, b):
	if a < b:
		return gcd(b, a)
	if b == 0:
		return a
	return gcd(b, a%b)

C = int(stdin.readline())
for c in xrange(1,C+1):
	aa = stdin.readline().split()
	N = int(aa[0])
	aa = aa[1:]
	for i in xrange(len(aa)):
		aa[i] = int(aa[i])
	aa.sort()
	#print aa
	mx = 0		
	for i in xrange(len(aa)):
		for j in xrange(len(aa)):
			if i != j:
				mx = gcd(mx, abs(aa[j]-aa[i]))
	#print mx
	ret = aa[0]
	ret = ret % mx;
	while (ret > 0):
		ret -= mx
	print "Case #" + str(c) + ": " + str(-ret)
