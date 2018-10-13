def traiterCas(destination, chevaux):
	maxDuration = 0
	for (position, vitesse) in chevaux:
		temps = (float)(destination - position) / vitesse
		if temps > maxDuration:
			maxDuration = temps

	return destination / maxDuration

t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
	chaine = raw_input()
	(destination, nbChevaux) = (int(i) for i in chaine.split())
	chevaux = [];
	for k in range(0, nbChevaux):
		(position, vitesse) = (int(j) for j in raw_input().split())
		chevaux.append((position, vitesse))
	print "Case #%d: %f" % (i, traiterCas(destination, chevaux))