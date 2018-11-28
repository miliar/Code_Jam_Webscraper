import os
from math import*
# Classe Gestion de fichier
class fichier:
	def __init__(self,path):
		self.path = path
		self.fichier = None

	def open(self,option):
		try:
			self.fichier = open(self.path,option)
		except:
			print("Error File doesn't exist !!!")

	def close(self):
		f.fichier.close()

	def read(self):
		self.open('r')
		text = self.fichier.read()
		self.close()
		return text

	def write(self,text):
		self.open('a')
		self.fichier.write(str(text))
		self.close()

	def new_line(self):
		self.write('\n')
		
		
		
f=fichier("C-small-attempt0.in")
fout=fichier("outsmall.out")
t=f.read()
l=t.split("\n")



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
		
	
	
	



	
	


