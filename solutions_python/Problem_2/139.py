# train timetable


for case in range(input()):
	tt = int(raw_input())
	na, nb = map(int, raw_input().split())
	abtrips = []
	for n in range(na):
		arrival, departure = raw_input().split()
		ah, am = map(int, arrival.split(":"))
		dh, dm = map(int, departure.split(":"))
		abtrips.append((ah * 60 + am, dh * 60 + dm + tt))
	abfirsts = [abtrips.index(t) for t in sorted(list(abtrips))]
	ablasts = [abtrips.index((b, a)) for (a, b) in  sorted(list([(b, a) for (a, b) in abtrips]))]
	
	batrips = []
	for n in range(nb):
		arrival, departure = raw_input().split()
		ah, am = map(int, arrival.split(":"))
		dh, dm = map(int, departure.split(":"))
		batrips.append((ah * 60 + am, dh * 60 + dm + tt))
	bafirsts = [batrips.index(t) for t in sorted(list(batrips))]
	balasts = [batrips.index((b, a)) for (a, b) in  sorted(list([(b, a) for (a, b) in batrips]))]
	
	# do it
	
	curab = 0
	for f in bafirsts:
		if curab == len(ablasts): break
		if abtrips[ablasts[curab]][1] <= batrips[f][0]:
			nb -= 1
			curab += 1
	
	curba = 0
	for f in abfirsts:
		if curba == len(balasts): break
		if batrips[balasts[curba]][1] <= abtrips[f][0]:
			na -= 1
			curba += 1
	
	print 'Case #%s: %s %s' % (case + 1, na, nb)
