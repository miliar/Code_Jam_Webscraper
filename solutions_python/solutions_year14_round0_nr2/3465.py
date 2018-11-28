def jouer(c = 500.0, f0 = 2.0, f = 4.0, x = 2000.0):
	n = 0
	ti = x / f0
	tf = ti
	while tf <= ti:
		tf = 0.0
		if tf != 0.0:
			ti = tf
		for i in range(n):
			tf = tf + c / (f * i + f0)
		tf = tf + x / (f * n + f0)
		if tf > ti:
			break
		else:
			ti = tf
		n = n + 1
	return ti

def fichierEnDictionnaire(nomFichier):
	with open(nomFichier, 'r') as fichier:
		contenu = fichier.read()
		listMatrice = list()
		listJeux = list()
		i = 1
		listJeux = contenu.split("\n")
		end = int(listJeux[0])
		bl = list()
		while i < (end + 1):
			l = list()
			l = listJeux[i].split(' ')
			bl.append(l)
			i = i + 1
		return bl

def demarrer(nomFichier):
	b = list()
	b = fichierEnDictionnaire(nomFichier)
	i = 0
	while i < len(b):
		tmp = jouer(float(b[i][0].replace(',', '.')), 2.0, float(b[i][1].replace(',', '.')), float(b[i][2].replace(',', '.')))
		with open("output", 'a') as output:
			output.write("Case #{}: {}\n".format(i + 1, tmp))
		i = i + 1
