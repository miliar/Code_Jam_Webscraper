import os
#  Classe Gestion de fichier
class Fichier:
	def __init__(self,path):
		self.path = path
		self.fichier = None
		
	def open(self,option):
		try:
			self.fichier = open(self.path,option)
		except:
			print("Error File doesn't exist !!!")
	
	def close(self):
		self.fichier.close()
	
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
# Fin classe
##############################################
# Lecture fichier
ifile = Fichier("B-large.in")
ofile = Fichier("output.in")
text = ifile.read()
inputs= text.split('\n')
# Fin lecture
##############################################

N=int(inputs[0])
for cpt in range(1,N+1):
	num_part = 0
	data = inputs[cpt].split(" ")
	number = int(data[0])
	weird = int(data[1])
	p = int(data[2])
	min = 3*p - 4
	for i in range(3,number+3):
		val = int(data[i])
		if (val >= p):
			if (val == min) or (val == (min + 1)):
				if weird > 0:
					num_part = num_part + 1
					weird= weird - 1
					
			elif (val > min +1):
				num_part = num_part + 1
			
	ofile.write("Case #"+str(cpt)+": "+str(num_part))
	ofile.new_line()
	
