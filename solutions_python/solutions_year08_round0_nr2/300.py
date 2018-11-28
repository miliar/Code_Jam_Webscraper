#!/usr/bin/env pythonw
# -*- coding:Utf-8 -*-

import sys

#Tri selon la première colonne
def sortTab(T):
	N = len(T[0])
	j = 1
	while j != N:
		i = j - 1
		tmp0 = T[0][j]	
		tmp1 = T[1][j]	
		while i > -1 and T[0][i] > tmp0:
			T[0][i+1] = T[0][i]
			T[1][i+1] = T[1][i]
			i = i - 1
		T[0][i+1] = tmp0
		T[1][i+1] = tmp1
		j = j + 1
 	return T

file = open ("a2.dat","r")
f = open("out.dat","w")

N = int(file.readline())
for y in range(0,N):
	NTA = 0
	NTB = 0
	NAM = 0
	NBM = 0
	L = 0
	oldTime = -1
	T = int(file.readline())
	ligne = file.readline()
	d = ligne.split()
	NA = int(d[0])
	NB = int(d[1])
	L = NA+NB
	TA = 2*[0]
	TB = 2*[0]
	for i in range(len(TA)):	TA[i] = (NA+NB)*[0] #
	for i in range(len(TB)):	TB[i] = (NA+NB)*[0] #

	#De A à B
	for i in range(0,NA):
		ligne = file.readline()
		d = ligne.split()
		dep = d[0]
		arr = d[1]
		timed = dep.split(':')
		timea = arr.split(':')
		timeA = int(timed[0])*60+int(timed[1])
		timeB = int(timea[0])*60+int(timea[1])+T
		TA[0][i] = timeA
		TB[0][i] = timeB
		TA[1][i] = -1
		TB[1][i] = 1
	i = i + 1
	#De B à A
	for j in range(0,NB):
		ligne = file.readline()
		d = ligne.split()
		dep = d[0]
		arr = d[1]
		timed = dep.split(':')
		timea = arr.split(':')
		timeB = int(timed[0])*60+int(timed[1])
		timeA = int(timea[0])*60+int(timea[1])+T
		TA[0][i+j] = timeA
		TB[0][i+j] = timeB
		TA[1][i+j] = 1
		TB[1][i+j] = -1
	
	#On tri le tout
	TA = sortTab(TA)
	TB = sortTab(TB)
	

	#On fait nos comptes
	if NA == 0 :
		NAM = 0
	else:
		oldTime = TA[0][0]
		NAM = 0
		for i in range (0, L):
			if oldTime != TA[0][i]:
				NAM = min(NTA, NAM)
				oldTime = TA[0][i]
			NTA = NTA + TA[1][i]
		NAM = min(NTA, NAM)

	if NB == 0 :
		NBM = 0
	else :
		oldTime = TB[0][0]
		NBM = 0
		for i in range (0, L):
			if oldTime != TB[0][i]:
				NBM = min(NTB, NBM)
				oldTime = TB[0][i]
			NTB = NTB + TB[1][i]
		NBM = min(NTB, NBM)
						
	#Et on prie pour que se soit bon cette fois :(
	print "Case #"+str(y+1)+": "+ str(abs(NAM)) + " " + str(abs(NBM))
	f.write("Case #"+str(y+1)+": "+ str(abs(NAM)) + " " + str(abs(NBM))+"\n")

#Oublié dans le code précédent...
f.close()