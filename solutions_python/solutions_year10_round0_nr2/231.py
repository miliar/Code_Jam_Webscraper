import sys

def gcd(a, b):
	return gcd(b, a%b) if b else a

c = -1
for line in sys.stdin:
	c += 1
	if c == 0: continue
	numstr = line.split()
	num = [int(x) for x in numstr[1:]]
	num.sort()
	g = num[1] - num[0]
	for i in xrange(2,len(num)):
		g = gcd(g,num[i]-num[i-1])
	tmp = num[-1] / g * g
	ans = 0 if tmp == num[-1] else tmp+g-num[-1]
	print "Case #%d: %d" % (c, ans)
