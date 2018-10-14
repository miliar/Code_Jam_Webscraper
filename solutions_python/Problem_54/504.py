def gcd2(a, b):
    while b != 0:
       t = b
       b = a % b
       a = t
    return a

gcd = lambda l: reduce(gcd2, l)

for i in xrange(int(raw_input())):
        l = map(int, raw_input().split(" "))
	assert len(l) == l[0] + 1
	l = l[1:]
	m = min(l)
	l2 = [x - m for x in l if x != m]
	g = gcd(l2)
	x = min(l)
	print "Case #%i: %i" %(i+1, ((x+g-1)//g)*g - min(l))
