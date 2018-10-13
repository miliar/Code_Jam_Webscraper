# !/usr/bin/python
# -*- coding: utf-8 -*-
import re
entree=open("input.txt","r")
sortie=open("output.txt","w")
entree.readline()
nb=0

for line in entree:
	valeurs=re.findall(r"\d+\b",line)
	A=int(valeurs[0])
	B=int(valeurs[1])
	nombre=A
	compteur=0
	dejafaits=[]
	while nombre<=B:
		
		chiffres=str(nombre)
		for i in range(0,len(str(nombre))):
			test=chiffres[i:]+chiffres[:i]
			toutChiffresEgaux=True
			for x in chiffres:
				if x!=chiffres[0]:
					toutChiffresEgaux=False
			#print chiffres+" "+str(toutChiffresEgaux)
			if (test[0]!="0" and int(test)>=A and int(test)<=B and (test!=chiffres ) and int(chiffres)<=int(test)):
				compteur+=1
				print chiffres+" "+test+" "+str(test in dejafaits)+" "+str(compteur)
				dejafaits.append(test)
				dejafaits.append(chiffres)
				#and (test in dejafaits)==False)
		nombre+=1
	nb+=1
	print compteur
	sortie.write("Case #"+str(nb)+": "+str(compteur)+"\n")
