cases = int(input())

for casenum in range(1,cases+1):
	Ac, Aj = ( int(x) for x in input().split() )

	times = []

	for i in range(Ac):
		beg, end = (int(x) for x in input().split())
		data = (beg, end, 'C')
		times.append(data)
	for i in range(Aj):
		beg, end = (int(x) for x in input().split())
		data = (beg, end, 'J')
		times.append(data)

	res = 0

	times.sort(key=lambda x: x[0])

	prev = times[-1]

	waitsJ = []
	waitsC = []
	timesJ = 0
	timesC = 0

	for time in times:
		duration = time[1]-time[0]
		if time[2] == 'C':
			timesC += duration
		else:
			timesJ += duration

		if prev[2] == time[2]:
			wait = time[0] - prev[1]
			if wait < 0:
				wait += 1440
			if time[2] == 'C':
				waitsC.append(wait)
			else:
				waitsJ.append(wait)
		else:
			res += 1
		prev = time

	waitsJ.sort()
	waitsC.sort()

	if timesJ + sum(waitsJ) > 720:
		i = 1
		while timesJ + sum(waitsJ[:-i]) > 720:
			i += 1
		res += 2*i
	elif timesC + sum(waitsC) > 720:
		i = 1
		while timesC + sum(waitsC[:-i]) > 720:
			i += 1
		res += 2*i

	print("Case #", casenum, ": ", res, sep="")

