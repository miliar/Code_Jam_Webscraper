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

def rotation(v,A,B):
	l=list(str(v))
	w=int(v)
	tab=[]
	
	res=0
	
		
	for i in range(len(l)):
		
		s=l.pop()
		l.insert(0,s)
		
		entier = int(''.join(map(str,l)))
		
		if (entier <= B and w <entier ):
			if (not (entier in tab)):
				res=res+1
				tab.append(entier)
	return (res)
			
		
		
		

	
def traitement(input,line):
	resultat=0
	v=0
	text=input[line]
	text=text.split(" ")
	output.write("Case #"+str(line)+": ")
	A=int(text[0])
	B=int(text[1])
	#print B
	v=A
	#print B-A
	for i in range(B-A):
		resultat+=rotation(v,A,B)
		v=v+1
		
		
	
	print resultat
	
	

	
	output.write (resultat)
	output.new_line()
		
l=input[0]	
for i in range(1,int(l)+1):
	
	traitement(input,i)
	


	




