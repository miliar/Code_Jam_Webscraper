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
ifile = Fichier("C-small-attempt0.in")
ofile = Fichier("output.in")
text = ifile.read()
inputs= text.split('\n')
# Fin lecture
##############################################

def permute(n,i):
	result = ""
	for j in range(len(n)):
		result=result+n[(j+i)%len(n)]
	return int(result)
	
	
N=int(inputs[0])
for cpt in range(1,N+1):
	already_done = []
	couples = 0
	data = inputs[cpt].split(" ")
	A = int(data[0])
	B = int(data[1])
	for n in range(A,B):
		number = str(n)
		for i in range(1,len(number)):
			if (number[i%len(number)] != '0'):
				permuted = permute(number,i)
				if not((n,permuted) in already_done) and (permuted <= B ) and (permuted >n) and not((permuted,n) in already_done):
					already_done.append((permuted,n))
					couples = couples + 1
					
	
	ofile.write("Case #"+str(cpt)+": "+str(couples))
	ofile.new_line()
	
