cases = input()

for t in range( 1, cases + 1 ):
	n = input()
	m = raw_input()
	
	m = m.split()
	m = map(int, m)
	
	ans1 = 0
	ans2 = 0
	rate = 0
	for i in range( 1, len(m) ):		
		if m[i-1] > m[i]:
			ans1 += ( m[i-1] - m[i] )
		rate = max(rate, ( m[i-1] - m[i] ))
		
	rate = abs(rate)
	for i in range( len(m) - 1 ):
		ans2 += min(rate, m[i])		
	
	print "Case #" + repr(t) + ":",
	print ans1, ans2
	