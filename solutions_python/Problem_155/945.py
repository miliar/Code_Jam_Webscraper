def nombre_ami(b):
	debout = 0
	ami = 0
	compteur = 0
	ami_en_plus = 0
	for chiffre in b:
		if compteur > debout:
			ami_en_plus = (compteur - debout)
			ami += ami_en_plus
			debout += ami_en_plus
		debout += int(chiffre)
		compteur += 1
	return str(ami)

def solution_jam1():
	source = open("D:/Download/test.txt","r")
	output = open("D:/Download/jam1long.txt","w")
	liste = source.readline()
	liste = liste.split('\n')
	for i in range(int(liste[0])):
		liste = source.readline()
		liste = liste.split()
		output.write('Case #'+str(i+1)+': '+nombre_ami(liste[1])+'\n')
	output.close()
	source.close()

solution_jam1()
