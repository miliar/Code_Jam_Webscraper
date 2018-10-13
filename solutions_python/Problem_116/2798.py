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


