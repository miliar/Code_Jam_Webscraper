def tour(nomFichier):
	l = fichierEnDictionnaire(nomFichier)
	i = 0
	lig_list1 = list()
	lig_list2 = list()
	i = 0
	cpt = 1
	while i < len(l):
		lig1 = int(l[i])
		lig1 = lig1 - 1
		lig_list1 = list_ligne(l[i + 1], lig1)
		lig2 = int(l[i + 2])
		lig2 = lig2 - 1
		lig_list2 = list_ligne(l[i + 3], lig2)
		result = compare(lig_list1, lig_list2)
		with open("output", 'a') as output:
			output.write("Case #{}: {}\n".format(cpt, result))
		cpt = cpt + 1
		i = i + 4

def list_ligne(matrice1, lig1):
	i = lig1
	j = 0
	lig_list = list()
	while j >= 0:
		if not matrice1.__contains__((i, j)):
			break
		else:
			lig_list.append(matrice1[i, j])
		j = j + 1
	return lig_list

def compare(lig_list1, lig_list2):
	i = 0
	cpt = 0
	while i < len(lig_list1):
		j = 0
		while j < len(lig_list2):
			if lig_list1[i] == lig_list2[j]:
				element = lig_list1[i]
				cpt = cpt + 1
			j = j + 1
		i = i + 1
	if cpt == 0:
		return "Volunteer cheated!"
	elif cpt > 1:
		return "Bad magician!"
	elif cpt == 1:
		return element

def fichierEnDictionnaire(nomFichier):
	with open(nomFichier, 'r') as fichier:
		contenu = fichier.read()
		listMatrice = list()
		listJeux = list()
		i = 1
		listJeux = contenu.split("\n")
		while i < len(listJeux):
			debut = i + 1
			if len(listJeux[i]) == 1:
				t = 0
				matrice = dict()
				listMatrice.append(listJeux[i])
				while len(listJeux[debut]) > 1:
					j = 0
					l = listJeux[debut].split(' ')
					while j < len(l):
						matrice[t, j] = l[j]
						j = j + 1
					debut = debut + 1
					t = t + 1
				listMatrice.append(matrice)
			i = debut
		return listMatrice
