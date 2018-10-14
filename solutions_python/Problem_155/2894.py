def main(input_file, output_file):
	f = open(input_file, 'r')
	g = open(output_file, 'w')
	
	input = f.read()
	input = input.split('\n')

	nb_cases = int(input[0])
	
	for line in range(1, nb_cases+1):
		ligne_lue = input[line]
		ligne_lue = ligne_lue.split(' ')#ligne_lue est alors un tableau de string 
		print(ligne_lue)
		n = int(ligne_lue[0])
		personnes = [int(c) for c in ligne_lue[1]]
		
		necessaire = trouver_necessaire(n, personnes)
		g.write('Case #' + str(line) +  ': ' + str(necessaire) + '\n')		
		

def trouver_necessaire(n, personnes):
	n_1 = n+1 #Nombre de shyness = n + 1
	delta = [-personnes[0]]
	nb_personnes_prec = personnes[0]
	necessaires = 0
	for k in range(1, n_1): #si delta[k] <=0 alors il n'y a pas besoin de rajouter des gens
		a = k - nb_personnes_prec	
		delta.append(a)
		nb_personnes_prec += personnes[k]
		necessaires = max(necessaires, a)
	print(delta)
	return necessaires

main("A-large.in", "output.out")
