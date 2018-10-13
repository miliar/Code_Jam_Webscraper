#coding=utf-8

def changements(intervalles):
	retour = 0
	for i in range(0, 1440):
		if intervalles[i-1] != intervalles[i]:
			retour = retour + 1

	return retour

def traiterCas(intervalles, Cleft, Jleft):
	sens = 0 #0 = etendre avant, 1 = etendre apres

	if intervalles[0] == 'C':
		sens = 1

	index = 0
	modif = 1

	#premiere passe pour relier des activites
	for i in range(0, 1440):
		if intervalles[i] == 'C' and intervalles[i-1] == '':
			#On regarde si on pourrait relier des activites
			current = i-2
			longueur = 1
			while intervalles[current] == '':
				current = current - 1
				longueur = longueur + 1
			if intervalles[current] == 'J':
				continue
			if longueur <= Cleft:
				current = current + 1
				while intervalles[current] == '':
					intervalles[current] = 'C'
					Cleft = Cleft - 1
					current = current + 1


	while 1:
		index = index + 1
		if index >= 1440:
			modif = 0
			index = index % 1440
		if sens == 1:
			if intervalles[index] != 'C':
				sens = 0
				i = index
				while intervalles[i] == '' and Cleft > 0:
					modif = 1
					intervalles[i] = 'C'
					i = (i + 1) % 1440
					Cleft = Cleft - 1
				if Cleft == 0:
					break

		if sens == 0:
			if intervalles[index] == 'C':
				sens = 1
				i = index - 1
				while intervalles[i] == '' and Cleft > 0:
					modif = 1
					intervalles[i] = 'C'
					i = i - 1
					Cleft = Cleft - 1
				if Cleft == 0:
					break

		if modif == 0 and index == 1339:
			break

	if Cleft == 0:
		#On remplit tout de J
		for i in range(0, 1440):
			if intervalles[i] == '':
				intervalles[i] = 'J'

		return changements(intervalles)

	#Sinon on étend les J avant de remplir de C

	sens = 0 #0 = etendre avant, 1 = etendre apres

	if intervalles[0] == 'J':
		sens = 1

	index = 0
	modif = 1

	#premiere passe pour relier des activites
	for i in range(0, 1440):
		if intervalles[i] == 'J' and intervalles[i-1] == '':
			#On regarde si on pourrait relier des activites
			current = i-2
			longueur = 1
			while intervalles[current] == '':
				current = current - 1
				longueur = longueur + 1
			if intervalles[current] == 'C':
				continue
			if longueur <= Jleft:
				current = current + 1
				while intervalles[current] == '':
					intervalles[current] = 'J'
					Jleft = Jleft - 1
					current = current + 1

	while 1:
		index = index + 1
		if index >= 1440:
			modif = 0
			index = index % 1440
		if sens == 1:
			if intervalles[index] != 'J':
				sens = 0
				i = index
				while intervalles[i] == '' and Jleft > 0:
					modif = 1
					intervalles[i] = 'J'
					i = (i + 1) % 1440
					Jleft = Jleft - 1
				if Jleft == 0:
					break

		if sens == 0:
			if intervalles[index] == 'J':
				sens = 1
				i = index - 1
				while intervalles[i] == '' and Jleft > 0:
					modif = 1
					intervalles[i] = 'J'
					i = i - 1
					Jleft = Jleft - 1
				if Jleft == 0:
					break

		if modif == 0 and index == 1339:
			break

	for i in range(0, 1440):
		if intervalles[i] == '':
			intervalles[i] = 'C'

	return changements(intervalles)

t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
	chaine = raw_input()
	(Ac, Aj) = (int(i) for i in chaine.split())
	intervalles = []
	Cleft = 720
	Jleft = 720
	for k in range(0, 1440):
		intervalles.append('')
	for k in range(0, Ac):
		(debut, fin) = (int(j) for j in raw_input().split())
		Cleft = Cleft - (fin - debut)
		for l in range(debut, fin):
			intervalles[l] = 'C'
	for k in range(0, Aj):
		(debut, fin) = (int(j) for j in raw_input().split())
		Jleft = Jleft - (fin - debut)
		for l in range(debut, fin):
			intervalles[l] = 'J'
	print "Case #%d: %d" % (i, traiterCas(intervalles, Cleft, Jleft))