
N = int(raw_input())

def pgcd(a, b):
    if a % b == 0:
        return b
    return pgcd(b, a % b)

for k in range(1, N+1):
	l = map(lambda x : int(x), raw_input().split())[1:]
	l.sort()
	
	base = l[0]
	rem = l[1:]
	
	pgcd_rem = rem[0] - base
	for i in rem[1:]:
		if i - base:
			pgcd_rem = pgcd(pgcd_rem, i - base)
	ret = pgcd_rem - base 
	if ret < 0:
		ret += (abs(ret) / pgcd_rem)*pgcd_rem
		if ret:
			ret += pgcd_rem
		
	print 'Case #%d: %d' % (k, ret)
	