t = int(raw_input())
case = 0
while t>0:
	t-=1
	ans = 0
	r,c,w = map(int, raw_input().split())
	case += 1
	if c==w or w==1:
		ans = c
	else :
		if c%w == 0:
			ans = c/w + w - 1
		else:
			ans = c/w + w
	print "Case #%s: %s" %(case,ans)