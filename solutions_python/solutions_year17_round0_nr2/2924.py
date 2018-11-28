def check(nombre):
	chaine = str(nombre)
	for i in range(len(chaine)-1):
		if int(chaine[i+1])<int(chaine[i]):
			return 1
	return 0

def jeanmicheloutput(nombre):
	compteur = 0
	dizaine = 1
	longueur = len(str(nombre))
	while check(nombre):
		chaine = str(nombre)
		sub = int(chaine[longueur-1-compteur])+1
		compteur += 1
		nombre = nombre - sub*dizaine
		dizaine = 10*dizaine
	return nombre

def function(liste):
	nombre = int(liste[0])
	return str(jeanmicheloutput(nombre))

def solution_jam():
	source = open("D:/Programmation/Google/QualifJamCode17/B-large.in","r")
	output = open("D:/Programmation/Google/QualifJamCode17/solution.txt","w")
	liste = source.readline()
	# print(liste)
	liste = liste.split('\n')
	# print(liste[0])
	for i in range(int(liste[0])):
		liste = source.readline()
		liste = liste.split(' ')
		print(liste)
		output.write('Case #'+str(i+1)+': '+function(liste)+'\n')
	output.close()
	source.close()

solution_jam()