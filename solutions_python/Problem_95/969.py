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

fichier=Fichier("a.in")
output=Fichier("output.txt")
r=fichier.read()
input=r.split("\n")




def trans(char):
	trans=[' ','y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q']
	ind1=trans.index(char)
	if (ind1 !=0):
		return chr(ind1+96)
	else:
		return " "
	
def traitement(input,line):
	
	
	text=input[line]
	output.write("Case #"+str(line)+": ")
	print text
	for i in  range(len(text)):
		output.write (trans(text[i]))
	output.new_line()
		
l=input[0]	
for i in range(1,int(l)+1):
	traitement(input,i)

	




