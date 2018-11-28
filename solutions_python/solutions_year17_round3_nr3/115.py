
def executer_calcul(entrees):
	N=entrees[0]
	K=entrees[1]
	U=entrees[2]
	P=entrees[3]
	Case=entrees[4]
	P.sort()
	if(K!=N): print('Erreur')
	P.append(1)
	i=0
	while(U>1e-15):
		if(Case==75):
			print(P)
			print(len(P))
			print(U)
		if(U>=(P[i+1]-P[i])*(i+1)):
			U-=(P[i+1]-P[i])*(i+1)
			P[i]=P[i+1]
		else:
			P[i]+=U/(i+1)
			U=0
		i+=1
	if(i==0): prob=1
	else: prob=P[i-1]**i
	for k in range(i,N):
		prob=prob*P[k]
	return str(prob)


# Main : lecture du fichier input, appel à la fonction executer_calcul et impression des résultats dans un fichier output
multiprocessed=False # Décide si l'on parallélise les calculs pour gagner du temps
if (multiprocessed): from multiprocessing import Pool
if ((not multiprocessed) or __name__ == '__main__'):
	# Lecture du fichier input
	with open("Input.txt", "r") as input_file:
		input=input_file.readlines()
	# Exploitation du fichier ainsi enregistré
	T=int(input[0])
	current_line=1
	entrees=[]
	Case=1
	while(current_line<len(input)):
		N,K=map(int,input[current_line].split(' '))
		current_line+=1
		U=float(input[current_line].rstrip())
		current_line+=1
		P=list(map(float,input[current_line].split(' ')))
		current_line+=1
		entrees.append([N,K,U,P,Case])
		Case=Case+1
	# Exécution des calculs
	results=['']*len(entrees)
	if (not multiprocessed):
		for case in range(len(entrees)):
			results[case]=executer_calcul(entrees[case])
	else:
		pool=Pool() # Décide du nombre de processus à faire tourner en parallèle
		results=pool.map(executer_calcul,entrees)
	# Impression des résultats dans un fichier de sortie
	with open('Output.txt','w') as output:
		for case in range(len(entrees)):
			output.write('Case #'+str(case+1)+': '+results[case]+'\n')



