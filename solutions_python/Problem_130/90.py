def Ans1(twopN, P):
	print 'H', twopN, P
	if twopN == 1:
		return 0
	if P <= twopN/2:
		return 0
	else:
		return 1 + (Ans1(twopN/2, P-twopN/2)*2)

T = int(raw_input())

for t in xrange(1, T+1):
	N, P = map(int, raw_input().split())
	twopN = 2**N
	
	count = twopN
	Max = twopN-1
	step = 1
	while count > P:
		count /= 2
		Max -= step
		step *= 2
	Ans2 = Max
	
	results = [] #results of last team winning prize
	tmp = twopN
	Ptmp = P
	while tmp > 1:
		if Ptmp <= tmp/2:
			results.append('W')
			tmp /= 2
		else:
			results.append('L')
			tmp /= 2
			Ptmp -= tmp
	countL = len(''.join(results).split('W')[0])
	if countL == N:
		Ans1 = twopN-1
	else:
		Ans1 = (2**(countL+1)) - 2
	print 'Case #%d: %d %d' % (t, Ans1, Ans2)
