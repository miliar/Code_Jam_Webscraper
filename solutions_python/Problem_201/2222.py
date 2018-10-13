#!/usr/bin/python
#coding=utf-8

def min(A, B):
	if A < B:
		return A
	return B

def max(A, B):
	if A > B:
		return A
	return B

def placerPersonne(intervalles, personnesLeft):
	#print intervalles
	(taille, nb) = intervalles[0]
	del(intervalles[0])
	if nb >= personnesLeft:
		return (taille, personnesLeft)
	personnesLeft = personnesLeft - nb
	if taille % 2 == 1:
		if taille != 1:
			intervalles.append((taille/2, 2 * nb))
	else:
		intervalles.append((taille/2, nb))
		if taille != 2:
			intervalles.append((taille/2 - 1, nb))

	intervalles.sort(reverse=True)

	return (-1, personnesLeft)

def traiterCas(nbSalles, nbPersonnes):
	intervalles = []

	nbSalles = int(nbSalles)
	nbPersonnes = int(nbPersonnes)

	personnesLeft = nbPersonnes

	intervalles.append((nbSalles, 1))
	#print intervalles

	while 1:
		(longueur, personnesLeft) = placerPersonne(intervalles, personnesLeft)
		if longueur != -1:
			if longueur % 2 == 1:
				return (longueur / 2, longueur / 2)
			else:
				return (longueur / 2, longueur / 2 - 1)

	return (-1, -1)

t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
	chaine = raw_input()
	(salles, personnes) = chaine.split()
	(res1, res2) = traiterCas(salles, personnes)
	print "Case #%d: %d %d" % (i, res1, res2)