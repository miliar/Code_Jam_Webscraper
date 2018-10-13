def inverse(x):
	if x == '-':
		return '+'
	else:
		return '-'

def jeanmicheloutput(a,i,largeur):
	res = ''
	l = len(a)
	for j in range(i):
		res = res + a[j]
	for j in range(i,i+largeur):
		res = res + inverse(a[j])
	for j in range(i+largeur,l):
		res = res + a[j]
	return res

print(jeanmicheloutput('---------',3,4))

def check(a,longueur,largeur):
	res = 1
	for i in range(longueur-largeur+1,longueur):
		if a[i] == '-':
			res = 0
	return res

def function(liste):
	[a,b] = liste
	largeur = int(b)
	longueur = len(a)
	compteur = 0
	for i in range(longueur-largeur+1):
		if a[i] == '-':
			a = jeanmicheloutput(a,i,largeur)
			compteur += 1
			print(a)
	if check(a,longueur,largeur):
		return str(compteur)
	else:
		return 'IMPOSSIBLE'

def solution_jam():
	source = open("D:/Programmation/Google/QualifJamCode17/A-large.in","r")
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