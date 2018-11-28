T = int(raw_input())

for tc in range(T):
	numbers = map(int, raw_input().split())
	N = numbers[0]
	surprise = numbers[1]
	p = numbers[2]
	googlers = numbers[3:]
	
	count = 0
	min_score = 3 * p
	for googler in googlers:
		if googler < p:
			continue
		if googler >= min_score:
			count += 1
		else:
			rem = min_score - googler
			if rem > 4:
				continue

			if rem  in (3, 4) and surprise > 0:
				count += 1
				surprise -= 1
				continue
			
			if rem in (1, 2):
				count += 1
	print 'Case #%d: %d' %(tc+1, count)
