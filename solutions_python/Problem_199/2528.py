def traiterCas(chaine, longueur):
	liste = list(chaine)
	longueur = int(longueur)
	flips = 0

	while '-' in liste:
		#Premier pancake mal mis
		i=0
		for elt in liste:
			if elt == '-':
				break
			i = i+1

		#On flippe
		if i <= len(liste) - longueur:
			flips = flips + 1
			for j in range(0, longueur):
				if liste[i + j] == '+':
					liste[i+j] = '-'
				else:
					liste[i+j] = '+'
		else:
			return "IMPOSSIBLE"

	return str(flips)	

t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
	chaine = raw_input()
	(chaine, longueur) = chaine.split()
	print "Case #%d: %s" % (i, traiterCas(chaine, longueur))