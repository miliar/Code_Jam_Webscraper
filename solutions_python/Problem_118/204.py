def fairsquares(n,m = 9, d = 1):
	if n == 0:
		yield []
		return
	if n == 1:
		while d*d <= m:
			for f in fairsquares(n-1,m-d*d,0):
				yield f[:n/2] + [d] + f[n/2:]
			d += 1
	else:
		while 2*d*d <= m:
			for f in fairsquares(n-2,m-2*d*d,0):
				yield [d] + f + [d]
			d += 1

everything = []
for i in range(1,52):
	for e in fairsquares(i,9):
		everything.append(int(''.join(map(str,e)))**2)

n_cases = input()
for case in range(1,n_cases+1):
	a,b = map(int,raw_input().split())
	count = 0
	for e in everything:
		if e > b:
			break
		elif e >= a:
			count += 1
	print 'Case #'+`case`+': '+`count`