
T = int(raw_input())

def ans(n, k):
	if k==1 : return n/2, (n-1)/2
	
	if n%2 : return ans(n/2, k/2)
	else : return ans( (n- (k%2))/2, k/2 )
		
for test in xrange(1, T+1):
	n, k = map(int, raw_input().split())
	a, b = ans(n, k)
	print "Case #%d: %d %d"%(test, a, b) 


