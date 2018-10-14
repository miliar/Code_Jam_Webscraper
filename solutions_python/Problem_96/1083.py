# !/usr/bin/python
# -*- coding: utf-8 -*-

import re
entree=open("input.txt","r")
entree.readline()
solution=open("solution.out","w")
inc=1
def arrondir_dessus(x):
	retour=0.0
	if float(int(x))==x:
		retour=x
	else:
		retour=float(1+int(x))
	return retour

for line in entree:
	valeurs=re.findall(r"\d+\b",line)
	for i in range(len(valeurs)):
		valeurs[i]=float(valeurs[i])
	scoreMin=valeurs[2]
	etranges=valeurs[1]
	valeurs.remove(valeurs[0])
	valeurs.remove(valeurs[0])
	valeurs.remove(valeurs[0])
	valeurs_originales=[]
	for i in range(len(valeurs)):
		valeurs_originales.append(valeurs[i])
		valeurs[i]=(valeurs[i]/3)
		valeurs[i]=arrondir_dessus(valeurs[i])
	#print valeurs
	notes=[]
	notes_surprenantes=[]
	for i in range(12):
		notes.append(0)
		notes_surprenantes.append(0)
	for i in range(len(valeurs)):
		notes[int(valeurs[i])]+=1
	#print notes
	for i in range(len(valeurs_originales)):
		if valeurs_originales[i]>1.0:
			if arrondir_dessus(valeurs_originales[i]/3)-(valeurs_originales[i]/3)<0.5:
				if notes_surprenantes[int(arrondir_dessus(valeurs_originales[i]/3)+1.0)]<etranges:
					notes_surprenantes[int(arrondir_dessus(valeurs_originales[i]/3)+1.0)]+=1
	#print valeurs_originales
	print "##########"
	print notes
	print notes_surprenantes
	i=int(scoreMin)+1
	resultat=notes[int(scoreMin)]+notes_surprenantes[int(scoreMin)]
	print resultat
	while i < 11:
		resultat+=notes[i]
		'''print i
		print resultat
		print "/"'''
		i+=1
	print resultat
	
	solution.write("Case #"+str(inc)+": "+str(resultat)+"\n")
	inc+=1


