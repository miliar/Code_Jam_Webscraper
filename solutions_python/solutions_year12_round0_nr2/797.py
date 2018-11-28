tc = int(raw_input())
for index in range(tc):
	# Read Input
	scores = [int(x) for x in raw_input().split()]
	n = scores.pop(0)
	s = scores.pop(0)
	p = scores.pop(0)

	googlers = 0

	for x in scores:
		surprising = 0
		if x:
			rem = x%3
			if rem == 0:
				maximum = int(x/3) + 1
				surprising = 1
			elif rem == 1:
				maximum = int(x/3) + 1
			else:
				maximum = int(x/3) + 2
				surprising = 1
		else:
			maximum = 0

		if maximum >= p:
			if not surprising or maximum-1 >= p:
				googlers += 1
			elif s:
				s -= 1
				googlers += 1

	print 'Case #' + str(index+1) + ': ' + str(googlers)
