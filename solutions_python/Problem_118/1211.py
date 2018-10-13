import os
import math
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
def ispalindrome(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return ispalindrome(word[1:-1])

def traitement(input,i):
	resultat=0
	u=input[i].split(" ")
	a=int(u[0])
	b=int(u[1])

	for i in range(a,b+1):
		number=math.sqrt(i)
		if int(number)-number == 0 :
			
			if ispalindrome(str(int(number))):
				if ispalindrome(str(i)):
					resultat=resultat+1
					
		

				
	
	# Ecriture dans l'output

	output.write (resultat)
	
	



#===========================================================================
#                                                 Main program 
#===========================================================================


file=Fichier("input.in")                            # Ouverture du fichier Input
output=Fichier("output.in")               # Ouverture du fichier Ouput
output.delete()                                    # On efface le contenu du Ouput
r=file.read()                                        
input=r.split("\n")	
l=input[0]   	
for i in range(1,int(l)+1):
	output.write("Case #"+str(i)+": ")
	traitement(input,i)
	output.new_line()
	
print 'yesssssss'

	




