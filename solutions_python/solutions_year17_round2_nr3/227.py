
class Noeud:
	def __init__(self,n):
		self.n=n
		self.arcs=[]
class Arc:
	def __init__(self,A,B,d):
		self.A=A
		self.B=B
		self.dist=d
		self.A.arcs.append(self)

def recherche_liste_triee(v,L,a,b):
	if(a==b):
		return a
	if(b-a==1):
		if(v.dist<L[a].dist): return a
		else: return b
	if(b<len(L) and L[a].dist==L[b].dist): return a
	p=(b-a)//2+a
	if(v.dist<L[p].dist): return recherche_liste_triee(v,L,a,p)
	else: return recherche_liste_triee(v,L,p+1,b)

def insertion_liste_triee(v,L):
	L.insert(recherche_liste_triee(v,L,0,len(L)),v)
def suppression_liste_triee(v,L):
	i=recherche_liste_triee(v,L,0,len(L))
	if(i<len(L) and v.n==L[i].n): L.pop(i)


def distances_villes(N,E,D):
	nodes=[]
	for i in range(N):
		nodes.append(Noeud(i))
	for i in range(N):
		for j in range(N):
			if(D[i][j]>=0): Arc(nodes[i],nodes[j],D[i][j])
	F=[[-1]*N for i in range(N)]
	for i in range(N):
		for j in range(N):
			nodes[j].visited=False
			nodes[j].dist=-1
		noeuds_a_parcourir=[nodes[i]]
		nodes[i].dist=0
		while(len(noeuds_a_parcourir)>0):
			A=noeuds_a_parcourir.pop(0)
			if(A.dist>E[i]): break
			F[i][A.n]=A.dist
			A.visited=True
			for arc in A.arcs:
				if(not arc.B.visited):
					if(arc.B.dist<0):
						arc.B.dist=A.dist+arc.dist
						insertion_liste_triee(arc.B,noeuds_a_parcourir)
					elif(arc.B.dist>A.dist+arc.dist):
						suppression_liste_triee(arc.B,noeuds_a_parcourir)
						arc.B.dist=A.dist+arc.dist
						insertion_liste_triee(arc.B,noeuds_a_parcourir)
	return F

	
def temps_entre_villes(N,S,F):
	nodes=[]
	for i in range(N):
		nodes.append(Noeud(i))
	for i in range(N):
		for j in range(N):
			if(F[i][j]>=0 and i!=j): Arc(nodes[i],nodes[j],F[i][j]/S[i])
	H=[[-1]*N for i in range(N)]
	for i in range(N):
		for j in range(N):
			nodes[j].visited=False
			nodes[j].dist=-1
		noeuds_a_parcourir=[nodes[i]]
		nodes[i].dist=0
		while(len(noeuds_a_parcourir)>0):
			A=noeuds_a_parcourir.pop(0)
			H[i][A.n]=A.dist
			A.visited=True
			for arc in A.arcs:
				if(not arc.B.visited):
					if(arc.B.dist<0):
						arc.B.dist=A.dist+arc.dist
						insertion_liste_triee(arc.B,noeuds_a_parcourir)
					elif(arc.B.dist>A.dist+arc.dist):
						suppression_liste_triee(arc.B,noeuds_a_parcourir)
						arc.B.dist=A.dist+arc.dist
						insertion_liste_triee(arc.B,noeuds_a_parcourir)
	return H


def executer_calcul(entrees):
	N=entrees[0]
	Q=entrees[1]
	E=entrees[2]
	S=entrees[3]
	D=entrees[4]
	U=entrees[5]
	V=entrees[6]
	Case=entrees[7]
	F=distances_villes(N,E,D)
	H=temps_entre_villes(N,S,F)
	accu=''
	for i in range(Q):
		accu=accu+' '+str(H[U[i]-1][V[i]-1])
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
		N,Q=map(int,input[current_line].split(' '))
		current_line+=1
		E=[0]*N
		S=[0]*N
		for i in range(N):
			E[i],S[i]=map(int,input[current_line].split(' '))
			current_line+=1
		D=[[0]*N for i in range(N)]
		for i in range(N):
			D[i]=list(map(int,input[current_line].split(' ')))
			current_line+=1
		U=[0]*Q
		V=[0]*Q
		for i in range(Q):
			U[i],V[i]=map(int,input[current_line].split(' '))
			current_line+=1
		entrees.append([N,Q,E,S,D,U,V,Case])
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



