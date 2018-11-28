import os
# Classe Gestion de fichier

class file:
	def __init__(self,x):
		self.x = x
		self.file = None

	def open(self,option):
	
			self.file = open(self.x,option)
		

	def close(self):
		f.file.close()

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
		
		

def cyclic(v,le,a,b):
	l=list(str(v))
	increment=0
	
	for i in range(len(l)):
		s=l.pop()
		l.insert(0,s)
		entier = int(''.join(map(str,l)))
		
		if ((entier<=b) and (entier >=a) and not(entier in le) and (entier>v) ):
			if (not((entier,v) in le)  and not((v,entier) in le)):
				le.append((entier,v))
			
		
		


inc =0
f=file("input.in")
g=file("output.out")
t=f.read()
l=t.split("\n")

n=int(l[0])


for i in range(n):
	le=[]
	stri=l[i+1].split(" ")
	A=int(stri[0])
	B=int (stri[1])
	for j in range(A,B):
		cyclic(j,le,A,B)

	g.write("Case #")
	g.write(str(i+1))
	g.write(": ")
	g.write(str(len(le)))
	g.write("\n")