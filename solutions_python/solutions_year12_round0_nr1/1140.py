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
ifile = Fichier("A-small-attempt0.in")
ofile = Fichier("output.in")
text = ifile.read()
inputs= text.split('\n')
# Fin lecture
##############################################

G_Table = ['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q']
S_Table = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print(S_Table.index('x'))
	


N=int(inputs[0])
for cpt in range(1,N+1):
	G = inputs[cpt]
	result = ""
	for i in range(len(G)):
		if G[i] == " ":
			result = result+" " 
		else:
			result= result+S_Table[G_Table.index(G[i])]	
	S = result
	ofile.write("Case #"+str(cpt)+": "+S)
	ofile.new_line()
	
