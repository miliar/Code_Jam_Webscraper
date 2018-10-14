t = int(raw_input())
for i in range(t):
	smax, s = raw_input().split()
	
	smax = int(smax)+1
	s_sum,cum_sum = 0,int(s[0])
	for j in range(1, smax):
		s_sum += int(s[j])
		if j > cum_sum:
			cum_sum += j - cum_sum
		cum_sum += int(s[j])
		#~ print s[j], cum_sum
			
	print 'Case #%d: %d' % (i+1, cum_sum - s_sum - int(s[0]))
			 
			
