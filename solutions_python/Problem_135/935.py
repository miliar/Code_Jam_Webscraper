T = input()
for cas in xrange(1, T+1):
	T -= 1
	r1 = input()
	a1 = [map(int, raw_input().split()) for i in xrange(4)]
	r2 = input()
	a2 = [map(int, raw_input().split()) for i in xrange(4)]
	ans = set(a1[r1-1])&set(a2[r2-1])
	if (len(ans) > 1):
		print 'Case #'+str(cas)+': Bad magician!'
	elif (len(ans) == 1):
		print 'Case #'+str(cas)+': '+str(list(ans)[0])
	else:
		print 'Case #'+str(cas)+': Volunteer cheated!'
