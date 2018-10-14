T = int(raw_input())

for test in xrange(1,T+1):
	N, K = map(int, raw_input().split())
	U = float(raw_input()) 
	a = map(float, raw_input().split())
	a.sort()
	ans = 1. 
	for i in xrange(N-1,-1,-1):
		tmp = (sum(a[:i+1])+U)/(i+1)
		if a[i]>= tmp :
			ans*= a[i]
		else :
			ans*= tmp 
			U-= tmp - a[i]
	print "Case #%d: %.7f"%(test, ans) 
