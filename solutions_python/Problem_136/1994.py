t = int(raw_input())

for qq in xrange(1, t + 1):
	[c, f, x] = map(float, raw_input().split())
	rate = 2.0
	if x <= c:
		print "Case #{0}: {1}".format(qq, x / rate)
		continue
	time = c / rate
	while True:
		time1 = (x - c) / rate
		time2 = x / (rate + f)
		if time1 < time2:
			print "Case #{0}: {1}".format(qq, round(time + time1, 7))
			break
		else:
			rate += f
			time += c / rate
		
