def traiterCas(n, k, u, probas):
	probas.sort()
	i = 0
	while u > 0:
		if i == len(probas) - 1:
			for k in range(0, len(probas)):
				probas[k] += u/len(probas)
			u = 0
		else:
			if probas[i] < probas[i+1]:
				diff = probas[i + 1] - probas[i]
				if u >= diff*(i+1):
					for k in range(0, i+1):
						probas[k] += diff
						u -= diff
					i = i+1
				else:
					for k in range(0, i+1):
						probas[k] += u/(i+1)
					u = 0
			else:
				i += 1

	produit = probas[0]

	for i in range(1, len(probas)):
		produit *= probas[i]

	return produit

t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
	chaine = raw_input()
	(n, k) = (int(l) for l in chaine.split())
	chevaux = [];
	u = float(raw_input())
	chaine = raw_input()
	probas = chaine.split()
	listeProbas = []
	for p in probas:
		listeProbas.append(float(p))
	print "Case #%d: %f" % (i, traiterCas(n, k, u, listeProbas))