f = open('A.in', 'r')

T = int(f.readline()[:-1])
for case_no in range(1, T + 1):
	N = int(f.readline()[:-1])
	S = list()
	WP = list()
	F = list()
	OWP = list()
	OOWP = list()
	RPI = list()
	for i in range(N):
		S.append(list(f.readline()[:-1]))
	for team in S:
		win = 0.0
		fight = N
		for result in team:
			if result == '1':
				win += 1
			elif result == '.':
				fight -= 1
		WP.append(win/fight)
		F.append(fight)
	for team in S:
		ow = 0.0
		fight = N
		for i, result in enumerate(team):
			if result == '0':
				ow += (WP[i] * F[i] - 1) / (F[i] - 1)
			elif result == '1':
				ow += (WP[i] * F[i]) / (F[i] - 1)
			else:
				fight -= 1
		OWP.append(ow / fight)
	for team in S:
		oow = 0.0
		fight = N
		for i, result in enumerate(team):
			if result == '1' or result == '0':			
				oow += OWP[i]
			else:
				fight -= 1
		OOWP.append(oow / fight)
	for i in range(N):
		RPI.append(0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i])
	print "Case #%s:" % (case_no)
	for rpi in RPI:
		print rpi
