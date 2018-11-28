T = int(raw_input())


def check(zz):
	for i in range(1, len(zz)):
		if zz[i-1] < i: return False
	return True
	

for i in range(T):
	Smax, ss = raw_input().split()
	n = int(Smax)+1
	z = [int(c) for c in ss]
	zz = [sum(z[:j]) for j in range(1, n+1)]

	f = 0
	while not check(zz):
		f += 1
		z[0] += 1
		zz = [sum(z[:j]) for j in range(1, n+1)]
		
	print "Case #%d: %d" %(i+1,f)
	
