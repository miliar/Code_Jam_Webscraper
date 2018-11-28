t = int(raw_input())
case = 0
while t > 0:
	t-=1
	case+=1
	ans = 'RICHARD'
	x, r, c = map(int, raw_input().split())
	if (r*c)%x==0:
		if (r%x==0 or c%x==0) and not(c<x-1 or r<x-1):
			ans = 'GABRIEL'
	print "Case #%s: %s" %(case, ans)
