#coding=utf-8

def updateDistances(distances, graphe, index, currentDistance):
	for i in range(0, len(graphe[index])):
		if i == index:
			continue
		if graphe[index][i] == -1:
			continue
		if distances[i] > currentDistance + graphe[index][i]:
			distances[i] = currentDistance + graphe[index][i]

def plusCourt(graphe, debut, arrivee):
	distMax = 100000000000
	distances = []
	sommetsRestants = []
	for i in range(0, len(graphe)):
		sommetsRestants.append(i)
		if i == debut:
			distances.append(0)
		else:
			distances.append(distMax)

	while 1:
		#On cherche la distance minimale
		minIndex = -1
		minDist = distMax
		for index in sommetsRestants:
			if distances[index] < minDist:
				minIndex = index
				minDist = distances[index]

		if minIndex == arrivee:
			return minDist

		#On met à jour les distances
		updateDistances(distances, graphe, minIndex, minDist)

		sommetsRestants.remove(minIndex)

def updateGraphe(graphe, villeDepart, currentVille, currentTemps, endurance, vitesse, connexions):
	#On regarde toutes les connexions possibles
	index = 0
	for connexion in connexions[currentVille]:
		if connexion != -1 and endurance >= connexion:
			temps = float(connexion) / vitesse + currentTemps
			if graphe[villeDepart][index] == -1 or graphe[villeDepart][index] > temps:
				graphe[villeDepart][index] = temps
			updateGraphe(graphe, villeDepart, index, temps, endurance - connexion, vitesse, connexions)
		index += 1

def traiterCas(villes, connexions, paires):
	retour = ""

	#Pré calcul du graphe
	graphe = []
	index = 0
	for ville in villes:
		graphe.append([])
		for ville2 in villes:
			graphe[index].append(-1) #Pas d'arête
		index += 1

	for i in range(0, len(villes)):
		updateGraphe(graphe, i, i, 0, villes[i][0], villes[i][1], connexions)

	for (depart, arrivee) in paires:
		val = plusCourt(graphe, depart - 1, arrivee - 1)
		if retour != "":
			retour += " "
		retour += str(val)

	return retour

t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
	(villes, paires) = (int(l) for l in raw_input().split())
	listVilles = []
	for ville in range(0, villes):
		(distance, vitesse) = (int(l) for l in raw_input().split())
		listVilles.append((distance, vitesse))
	connexions = []
	for ville in range(0, villes):
		connexion = raw_input().split()
		newConnexion = []
		for c in connexion:
			newConnexion.append(int(c))
		connexions.append(newConnexion)
		listPaires = []
	for paire in range(0, paires):
		(debut, fin) = (int(l) for l in raw_input().split())
		listPaires.append((debut, fin))
	print "Case #%d: %s" % (i, traiterCas(listVilles, connexions, listPaires))