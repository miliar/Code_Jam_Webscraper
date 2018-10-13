
import math

def executer_calcul(entrees):
	N=entrees[0]
	K=entrees[1]
	R=entrees[2]
	H=entrees[3]
	Case=entrees[4]
	Aire_max=0
	# Aires obtenues en considérant le pancake i à la base
	for i in range(N):
		A=[]
		for j in range(N):
			if(i!=j and R[j]<=R[i]): A.append(R[j]*H[j])
		if(len(A)>=K-1):
			A.sort()
			A.reverse()
			Aire=R[i]**2+2*R[i]*H[i]
			for j in range(K-1):
				Aire+=2*A[j]
			if(Aire>Aire_max): Aire_max=Aire
	return str(math.pi*Aire_max)


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
		R=[0]*N
		H=[0]*N
		for i in range(N):
			R[i],H[i]=map(int,input[current_line].split(' '))
			current_line+=1
		entrees.append([N,K,R,H,Case])
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



