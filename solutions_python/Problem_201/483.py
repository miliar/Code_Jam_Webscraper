
def log2(n):
	if(n==1): return 0
	else: return log2(n//2)+1

def executer_calcul(entrees):
	N=entrees[0]
	K=entrees[1]
	Case=entrees[2]
	k=log2(K)
	I1=(N-2**k+1)//2**k
	I2=I1+1
	nI2=(N-2**k+1)%2**k
	if(K-2**k+1<=nI2):
		z=(I2-1)//2
		if(I2%2==0): y=z+1
		else: y=z
	else:
		z=(I1-1)//2
		if(I1%2==0): y=z+1
		else: y=z
	return str(y)+' '+str(z)


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
		entrees.append([N,K,Case])
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



