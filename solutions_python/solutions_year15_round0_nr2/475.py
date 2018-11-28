T = int(raw_input())


def best(p):
	if p[0] <= 3: return p[0]
	
	low = p[0]
	up = 4 if p[0] >= 8 else 3
	for spl in range(2, up):
		
		m = p[0] / spl
		ex = p[0] % spl
		pp = p[1:] + [m+1]*ex + [m]*(spl-ex)
		
		pp.sort(reverse=True)
		
		check = best(pp) + 1
		low = min(best(pp)+spl-1, low)
		
	return low


for i in range(T):
	D = int(raw_input())
	p = [int(n) for n in raw_input().split()]
	p.sort(reverse=True)

	print "Case #%d: %d" % (i+1,best(p))
