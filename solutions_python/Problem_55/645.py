t = int(raw_input())
for e in range(t):
	line = raw_input()
	l = [int(x) for x in line.split()]
	p = raw_input()
	ppl = [int(x) for x in p.split()]
	wynik = 0
	for x in range(l[0]):
		suma = 0
		newppl = []
		remain = []
		for gr in range(l[2]):
			if suma+ppl[gr]<=l[1]:
				suma+=ppl[gr]
				wynik+=ppl[gr]
				newppl.append(ppl[gr])
			elif suma+ppl[gr]>l[1]:
				remain = ppl[gr:]
				break
		for r in newppl:
			remain.append(r)
		ppl = remain[::]
	print "Case #%d: %d" % (e+1,wynik)


