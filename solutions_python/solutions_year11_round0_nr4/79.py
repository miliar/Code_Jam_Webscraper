for T in range(int(raw_input())):
	raw_input()
	
	r = 0
	for i, e in enumerate(raw_input().split(' ')):
		if i + 1 != int(e):
			r += 1
			
	print 'Case #%d: %d.000000' % (T + 1, r)

