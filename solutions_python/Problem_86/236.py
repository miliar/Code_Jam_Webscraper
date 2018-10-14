num = input()
for round in xrange(num):

	N, L, H = map(int, raw_input().split())
	others = map(int, raw_input().split())

	ans = -1
	jeff = L
	if L == 1:
		ans = 1
	else:
		while jeff <= H:
			finish = 1
			for other in others:
				if jeff == other:
					donothing = 1
					#finish = 0
					#break
				elif jeff > other:
					#print 'more', jeff, other
					if jeff % other != 0:
						finish = 0
						break
				else:
					#print 'less', other, jeff
					if other % jeff != 0:
						finish = 0
						break
			if finish == 1:
				ans = jeff
				break
	
	
			jeff += 1
	
	if ans == -1:
		print 'Case #%d: NO' % (round + 1)
	else:
		print 'Case #%d: %d' % (round + 1, ans)
