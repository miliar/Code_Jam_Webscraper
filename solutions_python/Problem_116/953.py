import os
#===========================================================================
#                                                Classe Fichier
#===========================================================================
class Fichier:
	def __init__(self,path):
		self.path = path
		self.fichier = None

	def open(self,option):
		try:
			self.fichier = open(self.path,option)
		except:
			print("Error File doesn't exist !!!")

	def read(self):
		self.open('r')
		text = self.fichier.read()
		self.fichier.close()
		return text

	def write(self,text):
		self.open('a')
		self.fichier.write(str(text))
		self.fichier.close()
		
	def new_line(self):
		self.write('\n')
		
	def delete(self):
		self.open('w')
		self.fichier.close()


#===========================================================================
#                                                Traitement
#===========================================================================		

def traitement(input,i,fin):
	resultat=0
	
	a=input[i]
	b=input[i+1]
	c=input[i+2]
	d=input[i+3]
	print a
	print b
	print c
	print d
	stop=0
	resultat = 'Draw'
	for i in (a,b,c,d):
		res=int(i[0])*int(i[1])*int(i[2])*int(i[3])
		#print res
		if res == 0:
			resultat = 'Game has not completed'
		elif res== 8 or res == 16: #X Won
			resultat = 'X won'
			stop=1
			break
		elif res== 81 or res == 27: #Y Won
			resultat = 'O won'
			stop=1
			break
		
	if stop ==0:
		for i in range(4):
			res=int(a[i])*int(b[i])*int(c[i])*int(d[i])
			#print res
			if res == 0:
				resultat = 'Game has not completed'
			elif res== 8 or res == 16: #X Won
				resultat = 'X won'
				stop=1
				break
			elif res== 81 or res == 27: #Y Won
				resultat = 'O won'
				stop=1
				break
	
	if stop  ==0:
		res=int(a[0])*int(b[1])*int(c[2])*int(d[3])
		#print res
		if res == 0:
			resultat = 'Game has not completed'
		elif res== 8 or res == 16: #X Won
			resultat = 'X won'
			stop=1
			
		elif res== 81 or res == 27: #Y Won
			resultat = 'O won'
			stop=1
			
		
	if stop  ==0:
		res=int(a[3])*int(b[2])*int(c[1])*int(d[0])
		#print res
		if res == 0:
			resultat = 'Game has not completed'
		elif res== 8 or res == 16: #X Won
			resultat = 'X won'
			stop=1
	
		elif res== 81 or res == 27: #Y Won
			resultat = 'O won'
			stop=1
				
		
	print resultat


			

	

	# Ecriture dans l'output
	
	output.write (resultat)
	output.new_line()




#===========================================================================
#                                                 Main program 
#===========================================================================


file=Fichier("input.in")                            # Ouverture du fichier Input
output=Fichier("output.in")               # Ouverture du fichier Ouput
output.delete()                                    # On efface le contenu du Ouput
r=file.read()    

r=r.replace('X','2')
r=r.replace('.','0')
r=r.replace('T','1')
r=r.replace('O','3')

input=r.split("\n")	
l=int(input[0])   	      # nombre de cas a traiter


debut_cas=1
cas=1
while (cas <= l):
	
	output.write("Case #"+str(cas)+": ")

	traitement(input,debut_cas,5)
	debut_cas=debut_cas+5 # Debut du cas suivant
	cas=cas+1
	


	







	




