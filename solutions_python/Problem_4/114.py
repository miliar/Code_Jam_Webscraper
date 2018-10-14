# Minimum Scalar Product

for case in range(input()):
	n = int(raw_input())
	x = map(int,raw_input().split())
	y = map(int,raw_input().split())
	
	x.sort()
	y.sort()
	y.reverse()
	
	ans = 0
	
	for i in range(n):
		ans += x[i]*y[i]
	
	print "Case #%s: %s" % (case+1, ans)