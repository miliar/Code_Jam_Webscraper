for casenum in xrange(1,1+int(raw_input())):
	[N, Pd, Pt] = [int(z) for z in raw_input().split()]
	ans1 = 'Broken'
	ans2 = 'Possible'
	ans = ans1
	for i in xrange(1,N+1):
		if (i * Pd) % 100 == 0 and (i * Pd) / 100 <= i:
			if Pt == 100:
				if Pd == 100:
					ans = ans2
					break
			else:
				if Pt == 0:
					if Pd == 0:
						ans = ans2
						break
					else:
						ans = ans1
						break
				else:	
					ans = ans2
					break			
	print ("Case #%d: " % casenum) + str(ans)		