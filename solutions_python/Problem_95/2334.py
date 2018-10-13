import os
# Classe Gestion de fichier
class file:
	def __init__(self,x):
		self.x = x
		self.file = None

	def open(self,option):
		
			self.file = open(self.x,option)
		

	def close(self):
		g.file.close()

	def read(self):
		self.open('r')
		text = self.file.read()
		self.close()
		return text

	def write(self,text):
		self.open('a')
		self.file.write(str(text))
		self.close()

	def new_line(self):
		self.write('\n')

listA=["y","n","f","i","c","w","l","b","k","u","o","m","x","s","e","v","z","p","d","r","j","g","t","h","a","q"]

listB=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


g=file("C:\Users\Fares-Juve\Desktop\input.in")
fich=file("C:\Users\Fares-Juve\Desktop\output.out")
t=g.read()
print t
l=t.split("\n")

n=int (l[0])

for j in range(n):
	stri=l[j+1]
	stri1=''
	for k in range(len(stri)):
		caractere=stri[k]
		if caractere == " ":
			stri1=stri1 + " "
		else:
			ind = listA.index(caractere)
			stri1=stri1 + listB[ind]
			
	print stri1
	fich.write("Case #")
	fich.write(str(j+1))
	fich.write(": ")
	fich.write(stri1)
	fich.write("\n")
		
		


