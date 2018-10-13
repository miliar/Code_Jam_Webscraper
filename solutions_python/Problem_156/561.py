T = int(raw_input())
for kase in range(1, T + 1):
	d = int(raw_input())
	p = map(int, raw_input().split())

	s = 1
	e = 1001
	ans = -1

	while s < e:
		mid = (s + e) / 2
		midAble = False
		for toStop in range(0, mid):
			left = toStop
			lim = mid - toStop
			isAble = True
			for v in p:
				req = (v - 1) / lim
				if req > left:
					isAble = False
					break
				left -= req
			if isAble:
				midAble = True
				break

		if midAble:
			e = ans = mid
		else:
			s = mid + 1
	
	print "Case #" + str(kase) + ": " + str(ans)
