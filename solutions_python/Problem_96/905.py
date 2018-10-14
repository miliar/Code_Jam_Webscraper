import os
# Classe Gestion de fichier
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

fichier=Fichier("in.in")
output=Fichier("output.txt")
r=fichier.read()
input=r.split("\n")



	
def traitement(input,line):
	
	nombre=0
	text=input[line]
	text=text.split(" ")
	output.write("Case #"+str(line)+": ")
	particip=text[0]
	surprise=int(text[1])
	note=int(text[2])
	u=note+(note-2)+(note-2)
	
	
	for i in range(3,len(text)):
		if (int(text[i]) >= note):
			if (int(text[i]) > u+1):
				nombre=nombre+1
			elif (int(text[i]) in [u,u+1]):
				if (surprise>0):
					surprise=surprise-1
					nombre=nombre+1
				
	
	print nombre
	
	
	
	
	
	output.write (nombre)
	output.new_line()
		
l=input[0]	
for i in range(1,int(l)+1):
	traitement(input,i)

	




