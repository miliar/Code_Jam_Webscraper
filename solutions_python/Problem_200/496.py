
def integer_to_base(number,base):
	if(number<base): return [number]
	result=integer_to_base(number//base,base)
	result.append(number%base)
	return result

def base_to_integer(liste,base):
	if(len(liste)==0): return 0
	a=liste.pop()
	return a+base_to_integer(liste,base)*base

def calcul(N):
	for i in range(1,len(N)):
		if(N[i]<N[i-1]):
			for j in range(i,len(N)):
				N[j]=9
			j=i-1
			while(j>0 and N[j]==0):
				N[j]=9
				j-=1
			N[j]-=1
			return calcul(N)
	return N

def executer_calcul(entrees):
	N=calcul(integer_to_base(entrees[0],10))
	return str(base_to_integer(N,10))


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
		N=int(input[current_line])
		current_line+=1
		entrees.append([N,Case])
		Case=Case+1
	# Exécution des calculs
	results=['']*len(entrees)
	if (not multiprocessed):
		for case in range(len(entrees)):
			results[case]=executer_calcul(entrees[case])
	else:
		pool=Pool(3) # Décide du nombre de processus à faire tourner en parallèle
		results=pool.map(executer_calcul,entrees)
	# Impression des résultats dans un fichier de sortie
	with open('Output.txt','w') as output:
		for case in range(len(entrees)):
			output.write('Case #'+str(case+1)+': '+results[case]+'\n')



