
def executer_calcul(entrees):
	N=entrees[0]
	R=entrees[1]
	O=entrees[2]
	Y=entrees[3]
	G=entrees[4]
	B=entrees[5]
	V=entrees[6]
	Case=entrees[7]
	if(max(B,R,Y)==B): return calcul(N,B,R,Y,'B','R','Y')
	if(max(B,R,Y)==R): return calcul(N,R,B,Y,'R','B','Y')
	if(max(B,R,Y)==Y): return calcul(N,Y,R,B,'Y','R','B')
	return ''

def calcul(N,B,N_R,N_Y,b,r,y):
	R=N_R
	Y=N_Y
	if(2*B>N): return 'IMPOSSIBLE'
	L=['a']*N
	for i in range(B):
		L[2*i]=b
	j=2*i+1
	while(j<N):
		if(R>=Y):
			L[j]=r
			R-=1
			j+=1
			if(j<N):
				L[j]=y
				Y-=1
				j+=1
		else:
			L[j]=y
			Y-=1
			j+=1
			if(j<N):
				L[j]=r
				R-=1
				j+=1
	for k in range(B-1):
		if(R>0):
			L[2*k+1]=r
			R-=1
		else:
			L[2*k+1]=y
			Y-=1
	accu=''
	for i in range(N):
		accu+=L[i]
	return accu

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
		N,R,O,Y,G,B,V=map(int,input[current_line].split(' '))
		current_line+=1
		entrees.append([N,R,O,Y,G,B,V,Case])
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



