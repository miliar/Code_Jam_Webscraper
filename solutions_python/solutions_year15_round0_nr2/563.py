T = int(raw_input())

for c in range(1, T+1):
	raw_input()
	plates = sorted(map(int, raw_input().split()), reverse=True)
	answer = 1000
	for eating_minutes in range(1, 1000):
		total = eating_minutes
		for plate in plates:
			if plate > eating_minutes:
				total += ((plate-1)/eating_minutes)
		answer = min(total, answer)
	print "Case #%d: %d" % (c, answer)
		   
			

