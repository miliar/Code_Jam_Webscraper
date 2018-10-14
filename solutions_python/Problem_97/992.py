import os
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
		
		

def cyclic(v,le,a,b):
	l=list(str(v))
	increment=0
	#print "-----------------------"
	#print a
	#print b
	for i in range(len(l)):
		s=l.pop()
		l.insert(0,s)
		entier = int(''.join(map(str,l)))
		#print v,")-->",entier
		if ((entier<=b) and (entier >=a) and not(entier in le) and (entier>v) ):
			if (not((entier,v) in le)  and not((v,entier) in le)):
				le.append((entier,v))
				#print "(",v,",",entier,")"
		
		


inc =0
f=fichier("C-small-attempt1.in")
fout=fichier("out.out")
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

	fout.write("Case #")
	fout.write(str(i+1))
	fout.write(": ")
	fout.write(str(len(le)))
	fout.write("\n")