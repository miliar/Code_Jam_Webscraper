t = int(raw_input())
case = 0
while t > 0:
	t-=1
	req = [0]
	av = 0
	case+=1
	sm, sl = map(str, raw_input().split())
	#print sl
	sl = map(int, list(sl))
	#print sl
	for i in xrange(len(sl)):
		if sl[i]>0:
			req.append(i-sum(sl[:i]))
	#print req
	print "Case #%s: %s" %(case, max(req))
    
