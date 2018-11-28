f = open('1.in', 'r')
o = open('1.out', 'w')

T = int(f.readline().strip())


for t in xrange(T):
    (C, F, X) = map(float, f.readline().strip().split(' '))
    P = 2
    i = 0
    allt = 0.0000000
    while(1):
	t1 = X / P
        t2 = (X / (P + F)) + (C / P)
	if (t1 > t2):
		allt = allt + (C / P)
		P = P + F
	else:
		allt = allt + t1
		break

    
    res = str('%.*f' % (7, allt))
    s = "Case #%d: %s\n" % (t+1, res)
    o.write(s)
