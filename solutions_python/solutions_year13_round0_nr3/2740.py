#!/usr/bin/env python
import sys
sys.path.append("../")
import fileHandler
from math import*

##################################################
# Lecture fichier
f = fileHandler.Fichier("C-small-attempt0.in")
fout = fileHandler.Fichier("C-small-attempt0.out")
t=f.read()
l=t.split("\n")
# Fin lecture
##################################################

for j in range(int (l[0])):
	num=l[j+1].split(" ")
	
	a=int(num[0])
	b=int(num[1])
	i =a -1
	compteur =0

	while (i<b):
		i=i+1
		s = str(i)
		sr= "".join(reversed(s))
		
		if (s==sr) :
			sq = int(sqrt(i))
			if (sq*sq == i):
				sqq = str(sq)
				sqr= "".join(reversed(sqq))
				if (sqr == sqq):
					#~ print i
					compteur =compteur+1


	print compteur	
	fout.write("Case #")
	fout.write(j+1)
	fout.write(": ")
	fout.write(compteur)
	fout.write("\n")
		
	
	
	



	
	


